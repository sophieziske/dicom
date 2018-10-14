#!/usr/bin/env python3

# command line interface (CLI) parsing
import requests
import argparse
import datetime
import time
import datetime
from pprint import pprint

# graphical user interface (GUI)
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject
from gi.repository import GLib
from gi.repository.GdkPixbuf import Pixbuf, Colorspace # for images
from gi.repository import Gio
from io import BytesIO

# DICOM
from dicomweb_client.api import DICOMwebClient

# this directory
from dicom_tables import *


def try_get_attr(data, tag, default_value=None):
    '''Try get attribute indexed by TAG in DICOM data DATA or return DEFAULT_VALUE
upon failure.'''
    try:
        value = data[tag]['Value'][0]
        if data[tag]['vr'] == 'US':  # unsigned int
            return value             # return integer
        elif data[tag]['vr'] == 'DA':  # date
            return datetime.date(int(value[0 : 4]),
                                 int(value[4 : 6]),
                                 int(value[6 : 8]))
        elif data[tag]['vr'] == 'TM':  # time (of day)
            return datetime.time(int(value[0 : 2]),
                                 int(value[2 : 4]),
                                 int(value[4 : 6]))
        else:
            return value            # as is
    except:
        return default_value


def try_get_attr_alphabetic(data, tag, default_value=None):
    try:
        return try_get_attr(data, tag, default_value)['Alphabetic']
    except:
        return default_value


class StudyStore(Gtk.ListStore):
    '''Gtk.ListStore of DICOM studies (model).'''
    def __init__(self, client):
        Gtk.ListStore.__init__(self, str, str, str, str, str)  # TODO GDate, GTime
        self.client = client
        studies = self.client.search_for_studies()
        for study in studies:
            study_instance_uid = try_get_attr(study, '0020000D')  # TODO wrap in DicomUID when 'vr': 'UI'
            if study_instance_uid is None:
                continue        # skip because http://dev-demo.sectra.se contains lots of such entries
            study_name = try_get_attr(study, '00100020')  # TODO decode string when 'vr': 'LO'
            person_name = try_get_attr_alphabetic(study, '00100010')  # TODO decode Person Name string when 'vr': 'PN'
            study_date = str(try_get_attr(study, '00080020'))          # TODO GDate
            study_time = str(try_get_attr(study, '00080030'))          # TODO GTime
            # studies_id = try_get_attr(study, '00020010')  # TODO 'vr' : 'UI'. same for all elements in `studies`
            # study = client.retrieve_study(study_instance_uid)   # retrieve same thing again
            self.append((study_instance_uid, study_name, person_name, study_date, study_time))


class SeriesStore(Gtk.ListStore):
    '''Gtk.ListStore of DICOM serieses (model).'''
    def __init__(self, client):
        Gtk.ListStore.__init__(self, str, str)
        self.client = client

    def update_using_study(self, study_instance_uid):
        self.study_instance_uid = study_instance_uid
        self.serieses = self.client.search_for_series(study_instance_uid)
        for series in self.serieses:
            series_instance_uid = try_get_attr(series, '0020000E')  # Series Instance UID
            series_modality = DICOM_MODALITIES[try_get_attr(series, '00080060')]  # Modality being either CR, OT, MR, XA, CT, US
            self.append((series_instance_uid, series_modality))


class InstanceStore(Gtk.ListStore):
    '''Gtk.ListStore of DICOM instances (model).'''
    def __init__(self, client):
        Gtk.ListStore.__init__(self, str, str)
        self.client = client

    def update_using_study_and_series(self, study_instance_uid, series_instance_uid):
        instances = self.client.search_for_instances(study_instance_uid,
                                                     series_instance_uid)
        for instance in instances:
            sop_class_uid = try_get_attr(instance, '00080016')  # SOP Class UID
            try:
                sop_name = SOP_UID_NAMES[sop_class_uid]  # lookup SOP name from UID
            except:
                sop_name = sop_class_uid  # if fails use UID
            sop_instance_uid = try_get_attr(instance, '00080018')  # SOP Instance UID
            self.append((sop_instance_uid, sop_name))


class DICOMWindow(Gtk.Window):

    def __init__(self, title="DICOM Viewer"):

        self.client = DICOMwebClient(url='http://dev-demo.sectra.se',
                                     qido_url_prefix='SectraQidoRs/mrnissuers/all',
                                     wado_url_prefix='SectraWadoRs/mrnissuers/all',
                                     stow_url_prefix='SectraStowRs/mrnissuers/all')


        # construct top window
        Gtk.Window.__init__(self,
                            title=title,
                            vexpand=True, hexpand=True,
                            border_width=0,
                        )
        self.set_border_width(1)
        self.set_default_size(1200, 600)
        
        

        # create top grid
        self.grid = Gtk.Grid(vexpand=True, hexpand=True,
                             column_homogeneous=True,
                             row_homogeneous=True)
        self.add(self.grid)     # add it to parent window

        # STUDIES
        self.study_store = StudyStore(client=self.client)
        self.current_study_filter = None
        self.study_filter = self.study_store.filter_new()
        self.study_filter.set_visible_func(self.study_view_filter_func)
        self.study_view = Gtk.TreeView.new_with_model(self.study_filter)
        self.study_view.connect("row-activated", self.on_study_view_row_activated)  # upon double-click or return press
        self.study_selection = self.study_view.get_selection()
        self.study_selection.set_mode(Gtk.SelectionMode.MULTIPLE)
        self.study_selection.connect("changed", self.on_study_selection_changed)
        for i, column_title in enumerate(["Study UID", "Study Name", "Person Name", "Study Date", "Study Time",]):
            if i == 0:
                continue        #skip "Study UID"
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_sort_column_id(i) #trying to make columns sortable
            self.study_view.append_column(column)
        self.study_view_scroller = Gtk.ScrolledWindow(vexpand=True,
                                                      hexpand=True)
        self.study_view_scroller.add(self.study_view)
        self.grid.attach(self.study_view_scroller,
                         left=0, top=0, width=1, height=1)

        # SERIESES
        self.series_store = SeriesStore(client=self.client)
        self.current_series_filter = None
        self.series_filter = self.series_store.filter_new()
        self.series_filter.set_visible_func(self.series_view_filter_func)
        self.series_view = Gtk.TreeView.new_with_model(self.series_filter)
        self.series_view.connect("row-activated", self.on_series_view_row_activated)  # upon double-click or return press
        self.series_selection = self.series_view.get_selection()
        self.series_selection.set_mode(Gtk.SelectionMode.MULTIPLE)
        self.series_selection.connect("changed", self.on_series_selection_changed)
        for i, column_title in enumerate(["Series UID", "Series Modality"]):
            if i == 0:
                continue        # skip "Series UID"
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.series_view.append_column(column)
        self.series_view_scroller = Gtk.ScrolledWindow(vexpand=True,
                                                       hexpand=True)
        self.series_view_scroller.add(self.series_view)
        self.grid.attach(self.series_view_scroller,
                         left=1, top=0, width=1, height=1)

        # INSTANCES
        self.instance_store = InstanceStore(client=self.client)
        self.current_instance_filter = None
        self.instance_filter = self.instance_store.filter_new()
        self.instance_filter.set_visible_func(self.instance_view_filter_func)
        self.instance_view = Gtk.TreeView.new_with_model(self.instance_filter)
        self.instance_view.connect("row-activated", self.on_instance_view_row_activated)  # upon double-click or return press
        self.instance_selection = self.instance_view.get_selection()
        self.instance_selection.set_mode(Gtk.SelectionMode.MULTIPLE)
        self.instance_selection.connect("changed", self.on_instance_selection_changed)
        for i, column_title in enumerate(["SOP Instance UID", "SOP Class"]):
            if i == 0:
                continue        # skip "SOP Instance UID"
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.instance_view.append_column(column)
        self.instance_view_scroller = Gtk.ScrolledWindow(vexpand=True,
                                                         hexpand=True)
        self.instance_view_scroller.add(self.instance_view)
        self.grid.attach(self.instance_view_scroller,
                         left=2, top=0, width=1, height=1)

        self.image_view = Gtk.Image()
        self.image_view_scroller = Gtk.ScrolledWindow(vexpand=True,
                                                      hexpand=True)
        self.image_view_scroller.add(self.image_view)
        self.grid.attach(self.image_view_scroller,
                         left=0, top=1, width=3, height=3)

        self.show_all()


    def on_study_view_row_activated(self, view, row_index, column):
        print("on_study_view_row_activated:", view, " row_index:", row_index)

        # clear in reverse order
        self.clear_current_image_and_pixel_data()
        self.clear_current_instance_store_and_view()
        self.clear_current_series_store_and_view()

        model, treeiter = view.get_selection().get_selected_rows()
        self.study_instance_uid = model[row_index][0]
        self.series_store.update_using_study(study_instance_uid=self.study_instance_uid)


    def on_study_selection_changed(self, selection):
        # clear in reverse order
        self.clear_current_image_and_pixel_data()
        self.clear_current_instance_store_and_view()
        self.clear_current_series_store_and_view()
        # print('on_study_selection_changed: seletion:{}, selection_count={}'.format(selection,
        #                                                                            selection.count_selected_rows()))
        # TODO visually present:
        # study_metadata = self.client.retrieve_study_metadata(self.study_instance_uid)


    def on_series_view_row_activated(self, view, row_index, column):
        print("on_series_view_row_activated:", view, " row_index:", row_index)

        # clear in reverse order
        self.clear_current_image_and_pixel_data()
        self.clear_current_instance_store_and_view()

        model, treeiter = view.get_selection().get_selected_rows()
        self.series_instance_uid = model[row_index][0]
        self.instance_store.update_using_study_and_series(study_instance_uid=self.study_instance_uid,
                                                          series_instance_uid=self.series_instance_uid)


    def on_series_selection_changed(self, selection):
        '''This is function is called too often so we cannot do any heavy work here.'''
        # print('on_series_selection_changed: seletion:{}, selection_count={}'.format(selection,
        #                                                                            selection.count_selected_rows()))

        # clear in reverse order
        self.clear_current_image_and_pixel_data()
        self.clear_current_instance_store_and_view()

        # TODO visually present:
        # series_metadata = self.client.retrieve_series_metadata(self.series_instance_uid)


    def on_instance_view_row_activated(self, view, row_index, column):
        print("on_instance_view_row_activated:", view, " row_index:", row_index)

        # clear in reverse order
        self.clear_current_image_and_pixel_data()

        model, treeiter = view.get_selection().get_selected_rows()
        self.sop_instance_uid = model[row_index][0]
        if True:
            # TODO visually present more parts of:
            instance_metadata = self.client.retrieve_instance_metadata(study_instance_uid=self.study_instance_uid,
                                                                       series_instance_uid=self.series_instance_uid,
                                                                       sop_instance_uid=self.sop_instance_uid)[0]
            self.image_height = try_get_attr(instance_metadata, '00280010')  # rows
            self.image_width = try_get_attr(instance_metadata, '00280011')  # columns
            self.image_bits_per_pixel = try_get_attr(instance_metadata, '00280100')  # bits per pixel
            self.frame_count = try_get_attr(instance_metadata, '00280008', '1')  # only present for multi-frame image instances so default to 1
            transfer_syntax_uid = try_get_attr(instance_metadata, '00020010')
            if transfer_syntax_uid is not None:
                transfer_type = DICOM_TRANSFER_SYNTAXES[transfer_syntax_uid]

            image_format = None  # possible values are None (uncompressed/raw), 'jpeg', or 'jp2'
            try:
                start = time.time()
                frames = self.client.retrieve_instance_frames(study_instance_uid=self.study_instance_uid,
                                                              series_instance_uid=self.series_instance_uid,
                                                              sop_instance_uid=self.sop_instance_uid,
                                                              frame_numbers=[1],
                                                              image_format=image_format)
                stop = time.time()
                print("Retrieving frame took {}".format(stop - start))
            except requests.exceptions.HTTPError:
                frames = []     # no frames
                pass

            # need to store frames because Pixbuf.new_from_data doesn't keep own
            # reference to data so Python will destroy it without Gtk knowing about it
            self.rgb_frames = len(frames)*[None]

            for image_index, frame in enumerate(frames):
                pixel_count = (self.image_width* self.image_height)
                rgb_frame_temp = bytearray(3*pixel_count)  # pre-allocate RGB pixels

                if image_format is None:  # raw pixels
                    start = time.time()
                    if self.image_bits_per_pixel == 8:
                        for j in range(0, pixel_count):
                            grey8 = frame[j]
                            rgb_frame_temp[3*j + 0] = grey8
                            rgb_frame_temp[3*j + 1] = grey8
                            rgb_frame_temp[3*j + 2] = grey8
                    if self.image_bits_per_pixel == 16:
                        for j in range(0, pixel_count):
                            # 16-bit grey pixel value
                            grey16 = (256*frame[2*j + 1] +
                                          frame[2*j + 0])
                            grey8 = int(grey16/128)  # 16-bit to 8-bit conversion
                            rgb_frame_temp[3*j + 0] = grey8
                            rgb_frame_temp[3*j + 1] = grey8
                            rgb_frame_temp[3*j + 2] = grey8
                    else:
                        raise Exception("Cannot handle bits_per_pixel being" +
                                        str(self.image_bits_per_pixel))
                    stop = time.time()
                    print("Converting frame to grey-scale RGB-image took {}".format(stop - start))

                    # Ref: https://lazka.github.io/pgi-docs/#GdkPixbuf-2.0/classes/Pixbuf.html#GdkPixbuf.Pixbuf.new_from_data
                    # this better than `Pixbuf.new_from_bytes` which requires
                    # the data parameter to be wrapped in a GLib.Bytes object

                    # WARNING: be aware of that `new_from_data` is buggy. See for instance:
                    # https://stackoverflow.com/questions/29501835/gtk3-gdk-pixbuf-new-from-data-gives-segmentation-fault-core-dumped-error-13
                    start = time.time()
                    self.rgb_frames[image_index] = bytes(rgb_frame_temp)  # bytearray needs to be wrapped in a `bytes` and store here in order to enot loose ref
                    pixbuf = Pixbuf.new_from_data(self.rgb_frames[image_index],  # data
                                                  Colorspace.RGB, # colorspace
                                                  False,  # has_alpha
                                                  8,  # bits_per_sample
                                                  self.image_width,  # width
                                                  self.image_height,  # height
                                                  self.image_width*3,  # rowstride, 3 because RGB has 3 bytes per pixel
                                                  None, None)  # rely on Python for deallocation
                    if image_index == 0:
                        self.image_view.set_from_pixbuf(pixbuf)
                    stop = time.time()
                    print("Display image took {}".format(stop - start))
                elif image_format == 'jp2':
                    print("TODO Decode jp2 image...")
                    if False:
                        input_stream = Gio.MemoryInputStream.new_from_data(frame, None)
                        pixbuf = Pixbuf.new_from_stream(input_stream, None)
                        if image_index == 0:
                            self.image_view.set_from_pixbuf(pixbuf)


    def on_instance_selection_changed(self, selection):
        '''This is function is called too often so we cannot do any heavy work here.'''
        pass
        # print('on_instance_selection_changed: seletion:{}, selection_count={}'.format(selection,
        #                                                                             selection.count_selected_rows()))
        # TODO visually present:
        # instance_metadata = self.client.retrieve_instance_metadata(self.instance_instance_uid)


    def clear_current_series_store_and_view(self):
        self.series_view.get_selection().unselect_all()
        self.series_store.clear()


    def clear_current_instance_store_and_view(self):
        self.instance_view.get_selection().unselect_all()
        self.instance_store.clear()


    def clear_current_image_and_pixel_data(self):
        self.image_view.clear()  # remove image before
        self.rgb_frames = None   # drop pixel data


    def study_view_filter_func(self, model, iter, data):
        return True # accept everything for now


    def series_view_filter_func(self, model, iter, data):
        return True # accept everything for now


    def instance_view_filter_func(self, model, iter, data):
        return True # accept everything for now






if __name__ == '__main__':
    win = DICOMWindow()
    win.connect("destroy", Gtk.main_quit)  # make close button window work
    win.show_all()                         # show everything
    Gtk.main()                             # start event loop
