# copied from https://www.dicomlibrary.com/dicom/modality/


OPEN_DICOM_SERVERS = ['https://dicomcloud.azurewebsites.net',
                      'http://dev-demo.sectra.se']


DICOM_MODALITIES = {
'AR': 'Autorefraction',
'AS': 'Angioscopy',             # retired
'ASMT': 'Content Assessment Results',
'AU': 'Audio',
'BDUS': 'Bone Densitometry (ultrasound)',
'BI': 'Biomagnetic imaging',
'BMD': 'Bone Densitometry (X-Ray)',
'CD': 'Color flow Doppler',     # retired
'CF': 'Cinefluorography',       # retired
'CP': 'Colposcopy',             # retired
'CR': 'Computed Radiography',
'CS': 'Cystoscopy',             # retired
'CT': 'Computed Tomography',
'DD': 'Duplex Doppler',         # retired
'DF': 'Digital fluoroscopy',    # retired
'DG': 'Diaphanography',
'DM': 'Digital microscopy',     # retired
'DOC': 'Document',
'DS': 'Digital Subtraction Angiography',  # retired
'DSA': 'Digital Subtraction Angiography',  # retired
'DX': 'Digital Radiography',
'EC': 'Echocardiography',       # retired
'ECG': 'Electrocardiography',
'EPS': 'Cardiac Electrophysiology',
'ES': 'Endoscopy',
'FA': 'Fluorescein angiography',  # retired
'FID': 'Fiducials',
'FS': 'Fundoscopy',             # retired
'GM': 'General Microscopy',

'HC': 'Hard Copy',
'HD': 'Hemodynamic Waveform',
'IO': 'Intra-Oral Radiography',
'IOL': 'Intraocular Lens Data',
'IVOCT': 'Intravascular Optical Coherence Tomography',
'IVUS': 'Intravascular Ultrasound',
'KER': 'Keratometry',
'KO': 'Key Object Selection',
'LEN': 'Lensometry',
'LP': 'Laparoscopy',            # retired
'LS': 'Laser surface scan',
'MA': 'Magnetic resonance angiography',  # retired
'MG': 'Mammography',
'MR': 'Magnetic Resonance',
'MS': 'Magnetic resonance spectroscopy',  # retired
'NM': 'Nuclear Medicine',
'OAM': 'Ophthalmic Axial Measurements',
'OCT': 'Optical Coherence Tomography (non-Ophthalmic)',
'OP': 'Ophthalmic Photography',
'OPM': 'Ophthalmic Mapping',
'OPR': 'Ophthalmic Refraction',  # retired
'OPT': 'Ophthalmic Tomography',
'OPV': 'Ophthalmic Visual Field',
'OSS': 'Optical Surface Scan',
'OT': 'Other',

'PLAN': 'Plan',
'PR': 'Presentation State',
'PT': 'Positron emission tomography (PET)',
'PET': 'Positron emission tomography (PET)',
'PX': 'Panoramic X-Ray',
'REG': 'Registration',
'RESP': 'Respiratory Waveform',
'RF': 'Radio Fluoroscopy',
'RG': 'Radiographic imaging (conventional film/screen)',
'RTDOSE': 'Radiotherapy Dose',
'RTIMAGE': 'Radiotherapy Image',
'RTPLAN': 'Radiotherapy Plan',
'RTRECORD': 'RT Treatment Record',
'RTSTRUCT': 'Radiotherapy Structure Set',
'RWV': 'Real World Value Map',
'SEG': 'Segmentation',
'SM': 'Slide Microscopy',
'SMR': 'Stereometric Relationship',
'SR': 'SR Document',
'SRF': 'Subjective Refraction',
'ST': 'Single-photon emission computed tomography (SPECT)',  # retired
'STAIN': 'Automated Slide Stainer',
'TG': 'Thermography',
'US': 'Ultrasound',
'VA': 'Visual Acuity',
'VF': 'Videofluorography',      # retired
'XA': 'X-Ray Angiography',
'XC': 'External-camera Photography',
}


# Keys are possible values of 00020010 (0002,0010) Transfer Syntax UID
# copied from https://www.dicomlibrary.com/dicom/transfer-syntax/
DICOM_TRANSFER_SYNTAXES = {
'1.2.840.10008.1.2': 'Implicit VR Endian: Default Transfer Syntax for DICOM',
'1.2.840.10008.1.2.1': 'Explicit VR Little Endian',
'1.2.840.10008.1.2.1.99': 'Deflated Explicit VR Little Endian',
'1.2.840.10008.1.2.2': 'Explicit VR Big Endian',

'1.2.840.10008.1.2.4.50': 'JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8-bit Image Compression',
'1.2.840.10008.1.2.4.51': 'JPEG Baseline (Processes 2 & 4): Default Transfer Syntax for Lossy JPEG 12-bit Image Compression (Process 4 only)',
'1.2.840.10008.1.2.4.52': 'JPEG Extended (Processes 3 & 5)',  # retired
'1.2.840.10008.1.2.4.53': 'JPEG Spectral Selection, Nonhierarchical (Processes 6 & 8)',  # retired
'1.2.840.10008.1.2.4.54': 'JPEG Spectral Selection, Nonhierarchical (Processes 7 & 9)',  # retired
'1.2.840.10008.1.2.4.55': 'JPEG Full Progression, Nonhierarchical (Processes 10 & 12)',  # retired
'1.2.840.10008.1.2.4.56': 'JPEG Full Progression, Nonhierarchical (Processes 11 & 13)',  # retired
'1.2.840.10008.1.2.4.57': 'JPEG Lossless, Nonhierarchical (Processes 14)',
'1.2.840.10008.1.2.4.58': 'JPEG Lossless, Nonhierarchical (Processes 15)',  # retired
'1.2.840.10008.1.2.4.59': 'JPEG Extended, Hierarchical (Processes 16 & 18)',  # retired
'1.2.840.10008.1.2.4.60': 'JPEG Extended, Hierarchical (Processes 17 & 19)',  # retired
'1.2.840.10008.1.2.4.61': 'JPEG Spectral Selection, Hierarchical (Processes 20 & 22)',  # retired
'1.2.840.10008.1.2.4.62': 'JPEG Spectral Selection, Hierarchical (Processes 21 & 23)',  # retired
'1.2.840.10008.1.2.4.63': 'JPEG Full Progression, Hierarchical (Processes 24 & 26)',  # retired
'1.2.840.10008.1.2.4.64': 'JPEG Full Progression, Hierarchical (Processes 25 & 27)',  # retired
'1.2.840.10008.1.2.4.65': 'JPEG Lossless, Nonhierarchical (Process 28)',  # retired
'1.2.840.10008.1.2.4.66': 'JPEG Lossless, Nonhierarchical (Process 29)',  # retired
'1.2.840.10008.1.2.4.70': 'JPEG Lossless, Nonhierarchical, First- Order Prediction (Processes 14 [Selection Value 1]): Default Transfer Syntax for Lossless JPEG Image Compression',
'1.2.840.10008.1.2.4.80': 'JPEG-LS Lossless Image Compression',
'1.2.840.10008.1.2.4.81': 'JPEG-LS Lossy (Near- Lossless) Image Compression',
'1.2.840.10008.1.2.4.90': 'JPEG 2000 Image Compression (Lossless Only)',
'1.2.840.10008.1.2.4.91': 'JPEG 2000 Image Compression',
'1.2.840.10008.1.2.4.92': 'JPEG 2000 Part 2 Multicomponent Image Compression (Lossless Only)',
'1.2.840.10008.1.2.4.93': 'JPEG 2000 Part 2 Multicomponent Image Compression',

'1.2.840.10008.1.2.4.94': 'JPIP Referenced',
'1.2.840.10008.1.2.4.95': 'JPIP Referenced Deflate',
'1.2.840.10008.1.2.5': 'RLE Lossless',
'1.2.840.10008.1.2.6.1': 'RFC 2557 MIME Encapsulation',

'1.2.840.10008.1.2.4.100': 'MPEG2 Main Profile Main Level',
'1.2.840.10008.1.2.4.102': 'MPEG-4 AVC/H.264 High Profile / Level 4.1',
'1.2.840.10008.1.2.4.103': 'MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1',
}


# SOPs
# https://www.dicomlibrary.com/dicom/sop/
SOP_UID_NAMES = {
'1.2.840.10008.1.1': 'Verification SOP Class',
'1.2.840.10008.1.20.1': 'Storage Commitment Push Model SOP Class',
'1.2.840.10008.1.20.2': 'Storage Commitment Pull Model SOP Class',  # retired
'1.2.840.10008.1.3.10': 'Media Storage Directory Storage',
'1.2.840.10008.1.40': 'Procedural Event Logging SOP Class',
'1.2.840.10008.1.9': 'Basic Study Content Notification SOP Class',  # retired

'1.2.840.10008.3.1.2.1.1': 'Detached Patient Management SOP Class',  # retired
'1.2.840.10008.3.1.2.1.4': 'Detached Patient Management Meta SOP Class',  # retired
'1.2.840.10008.3.1.2.2.1': 'Detached Visit Management SOP Class',         # retired
'1.2.840.10008.3.1.2.3.1': 'Detached Study Management SOP Class',         # retired
'1.2.840.10008.3.1.2.3.2': 'Study Componenet Management SOP Class',       # retired
'1.2.840.10008.3.1.2.3.3': 'Modality Performed Procedure Step SOP Class',
'1.2.840.10008.3.1.2.3.4': 'Modality Performed Procedure Step Retrieve SOP Class',
'1.2.840.10008.3.1.2.3.5': 'Modality Performed Procedure Step Notification SOP Class',
'1.2.840.10008.3.1.2.5.1': 'Detached Results Management SOP Class',  # retired
'1.2.840.10008.3.1.2.5.4': 'Detached Results Management Meta SOP Class',  # retired
'1.2.840.10008.3.1.2.5.5': 'Detached Study Management Meta SOP Class',    # retired
'1.2.840.10008.3.1.2.6.1': 'Detached Interpretation Management SOP Class',  # retired

'1.2.840.10008.4.2': 'Storage Service Class',

'1.2.840.10008.5.1.1.1': 'Basic Film Session SOP Class',
'1.2.840.10008.5.1.1.14': 'Print Job SOP Class',
'1.2.840.10008.5.1.1.15': 'Basic Annotation Box SOP Class',
'1.2.840.10008.5.1.1.16': 'Printer SOP Class',
'1.2.840.10008.5.1.1.16.376': 'Printer Configuration Retrieval SOP Class',
'1.2.840.10008.5.1.1.18': 'Basic Color Print Management Meta SOP Class',
'1.2.840.10008.5.1.1.18.1': 'Referenced Color Print Management Meta SOP Class',  # retired
'1.2.840.10008.5.1.1.2': 'Basic Film Box SOP Class',
'1.2.840.10008.5.1.1.22': 'VOI LUT Box SOP Class',
'1.2.840.10008.5.1.1.23': 'Presentation LUT SOP Class',
'1.2.840.10008.5.1.1.24': 'Image Overlay Box SOP Class',  # retired
'1.2.840.10008.5.1.1.24.1': 'Basic Print Image Overlay Box SOP Class',  # retired
'1.2.840.10008.5.1.1.26': 'Print Queue Management SOP Classs',          # retired
'1.2.840.10008.5.1.1.27': 'Stored Print Storage SOP Class',             # retired
'1.2.840.10008.5.1.1.29': 'Hardcopy Grayscale Image Storage SOP Class',  # retired
'1.2.840.10008.5.1.1.30': 'Hardcopy Color Image Storage SOP Class',      # retired
'1.2.840.10008.5.1.1.31': 'Pull Print Request SOP Class',                # retired
'1.2.840.10008.5.1.1.32': 'Pull Stored Print Management Meta SOP Class',  # retired
'1.2.840.10008.5.1.1.33': 'Media Creation Management SOP Class UID',
'1.2.840.10008.5.1.1.4': 'Basic Grayscale Image Box SOP Class',
'1.2.840.10008.5.1.1.4.1': 'Basic Color Image Box SOP Class',
'1.2.840.10008.5.1.1.4.2': 'Referenced Image Box SOP Class',  # retired
'1.2.840.10008.5.1.1.9': 'Basic Grayscale Print Management Meta SOP Class',
'1.2.840.10008.5.1.1.9.1': 'Referenced Grayscale Print Management Meta SOP Class',  # retired

'1.2.840.10008.5.1.4.1.1.1': 'CR Image Storage',
'1.2.840.10008.5.1.4.1.1.1.1': 'Digital X-Ray Image Storage ? for Presentation',
'1.2.840.10008.5.1.4.1.1.1.1.1': 'Digital X-Ray Image Storage ? for Processing',
'1.2.840.10008.5.1.4.1.1.1.2': 'Digital Mammography X-Ray Image Storage ? for Presentation',
'1.2.840.10008.5.1.4.1.1.1.2.1': 'Digital Mammography X-Ray Image Storage ? for Processing',
'1.2.840.10008.5.1.4.1.1.1.3': 'Digital Intra ? oral X-Ray Image Storage ? for Presentation',
'1.2.840.10008.5.1.4.1.1.1.3.1': 'Digital Intra ? oral X-Ray Image Storage ? for Processing',
'1.2.840.10008.5.1.4.1.1.10': 'Standalone Modality LUT Storage',  # retired
'1.2.840.10008.5.1.4.1.1.104.1': 'Encapsulated PDF Storage',
'1.2.840.10008.5.1.4.1.1.11': 'Standalone VOI LUT Storage',  # retired
'1.2.840.10008.5.1.4.1.1.11.1': 'Grayscale Softcopy Presentation State Storage SOP Class',
'1.2.840.10008.5.1.4.1.1.11.2': 'Color Softcopy Presentation State Storage SOP Class',
'1.2.840.10008.5.1.4.1.1.11.3': 'Pseudocolor Softcopy Presentation Stage Storage SOP Class',
'1.2.840.10008.5.1.4.1.1.11.4': 'Blending Softcopy Presentation State Storage SOP Class',
'1.2.840.10008.5.1.4.1.1.12.1': 'X-Ray Angiographic Image Storage',
'1.2.840.10008.5.1.4.1.1.12.1.1': 'Enhanced XA Image Storage',
'1.2.840.10008.5.1.4.1.1.12.2': 'X-Ray Radiofluoroscopic Image Storage',
'1.2.840.10008.5.1.4.1.1.12.2.1': 'Enhanced XRF Image Storage',
'1.2.840.10008.5.1.4.1.1.12.3': 'X-Ray Angiographic Bi-plane Image Storage',  # retired
'1.2.840.10008.5.1.4.1.1.128': 'Positron Emission Tomography Curve Storage',  # retired
'1.2.840.10008.5.1.4.1.1.129': 'Standalone Positron Emission Tomography Curve Storage',  # retired
'1.2.840.10008.5.1.4.1.1.2': 'CT Image Storage',
'1.2.840.10008.5.1.4.1.1.2.1': 'Enhanced CT Image Storage',
'1.2.840.10008.5.1.4.1.1.20': 'NM Image Storage',
'1.2.840.10008.5.1.4.1.1.3': 'Ultrasound Multiframe Image Storage',  # retired
'1.2.840.10008.5.1.4.1.1.3.1': 'Ultrasound Multiframe Image Storage',
'1.2.840.10008.5.1.4.1.1.4': 'MR Image Storage',
'1.2.840.10008.5.1.4.1.1.4.1': 'Enhanced MR Image Storage',
'1.2.840.10008.5.1.4.1.1.4.2': 'MR Spectroscopy Storage',

'1.2.840.10008.5.1.4.1.1.481.1': 'Radiation Therapy Image Storage',
'1.2.840.10008.5.1.4.1.1.481.2': 'Radiation Therapy Dose Storage',
'1.2.840.10008.5.1.4.1.1.481.3': 'Radiation Therapy Structure Set Storage',
'1.2.840.10008.5.1.4.1.1.481.4': 'Radiation Therapy Beams Treatment Record Storage',
'1.2.840.10008.5.1.4.1.1.481.5': 'Radiation Therapy Plan Storage',
'1.2.840.10008.5.1.4.1.1.481.6': 'Radiation Therapy Brachy Treatment Record Storage',
'1.2.840.10008.5.1.4.1.1.481.7': 'Radiation Therapy Treatment Summary Record Storage',
'1.2.840.10008.5.1.4.1.1.481.8': 'Radiation Therapy Ion Plan Storage',
'1.2.840.10008.5.1.4.1.1.481.9': 'Radiation Therapy Ion Beams Treatment Record Storage',

'1.2.840.10008.5.1.4.1.1.5': 'NM Image Storage',  # retired

'1.2.840.10008.5.1.4.1.1.6': 'Ultrasound Image Storage',  # retired
'1.2.840.10008.5.1.4.1.1.6.1': 'Ultrasound Image Storage',
'1.2.840.10008.5.1.4.1.1.66': 'Raw Data Storage',
'1.2.840.10008.5.1.4.1.1.66.1': 'Spatial Registration Storage',
'1.2.840.10008.5.1.4.1.1.66.2': 'Spatial Fiducials Storage',
'1.2.840.10008.5.1.4.1.1.66.3': 'Deformable Spatial Registration Storage',
'1.2.840.10008.5.1.4.1.1.66.4': 'Segmentation Storage',
'1.2.840.10008.5.1.4.1.1.67': 'Real World Value Mapping Storage',

'1.2.840.10008.5.1.4.1.1.7': 'Secondary Capture Image Storage',
'1.2.840.10008.5.1.4.1.1.7.1': 'Multiframe Single Bit Secondary Capture Image Storage',
'1.2.840.10008.5.1.4.1.1.7.2': 'Multiframe Grayscale Byte Secondary Capture Image Storage',
'1.2.840.10008.5.1.4.1.1.7.3': 'Multiframe Grayscale Word Secondary Capture Image Storage',
'1.2.840.10008.5.1.4.1.1.7.4': 'Multiframe True Color Secondary Capture Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1': 'VL (Visible Light) Image Storage',  # retired
'1.2.840.10008.5.1.4.1.1.77.1.1': 'VL endoscopic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.1.1': 'Video Endoscopic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.2': 'VL Microscopic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.2.1': 'Video Microscopic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.3': 'VL Slide-Coordinates Microscopic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.4': 'VL Photographic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.4.1': 'Video Photographic Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.5.1': 'Ophthalmic Photography 8-Bit Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.5.2': 'Ophthalmic Photography 16-Bit Image Storage',
'1.2.840.10008.5.1.4.1.1.77.1.5.3': 'Stereometric Relationship Storage',
'1.2.840.10008.5.1.4.1.1.77.2': 'VL Multiframe Image Storage',  # retired

'1.2.840.10008.5.1.4.1.1.8': 'Standalone Overlay Storage',  # retired
'1.2.840.10008.5.1.4.1.1.88.11': 'Basic Text SR',
'1.2.840.10008.5.1.4.1.1.88.22': 'Enhanced SR',
'1.2.840.10008.5.1.4.1.1.88.33': 'Comprehensive SR',
'1.2.840.10008.5.1.4.1.1.88.40': 'Procedure Log Storage',
'1.2.840.10008.5.1.4.1.1.88.50': 'Mammography CAD SR',
'1.2.840.10008.5.1.4.1.1.88.59': 'Key Object Selection Document',
'1.2.840.10008.5.1.4.1.1.88.65': 'Chest CAD SR',
'1.2.840.10008.5.1.4.1.1.88.67': 'X-Ray Radiation Dose SR',

'1.2.840.10008.5.1.4.1.1.9': 'Standalone Curve Storage',  # retired
'1.2.840.10008.5.1.4.1.1.9.1.1': '12-lead ECG Waveform Storage',
'1.2.840.10008.5.1.4.1.1.9.1.2': 'General ECG Waveform Storage',
'1.2.840.10008.5.1.4.1.1.9.1.3': 'Ambulatory ECG Waveform Storage',
'1.2.840.10008.5.1.4.1.1.9.2.1': 'Hemodynamic Waveform Storage',
'1.2.840.10008.5.1.4.1.1.9.3.1': 'Cardiac Electrophysiology Waveform Storage',
'1.2.840.10008.5.1.4.1.1.9.4.1': 'Basic Voice Audio Waveform Storage',

'1.2.840.10008.5.1.4.1.2.1.1': 'Patient Root Query/Retrieve Information Model ? FIND',
'1.2.840.10008.5.1.4.1.2.1.2': 'Patient Root Query/Retrieve Information Model ? MOVE',
'1.2.840.10008.5.1.4.1.2.1.3': 'Patient Root Query/Retrieve Information Model ? GET',
'1.2.840.10008.5.1.4.1.2.2.1': 'Study Root Query/Retrieve Information Model ? FIND',
'1.2.840.10008.5.1.4.1.2.2.2': 'Study Root Query/Retrieve Information Model ? MOVE',
'1.2.840.10008.5.1.4.1.2.2.3': 'Study Root Query/Retrieve Information Model ? GET',
'1.2.840.10008.5.1.4.1.2.3.1': 'Patient/Study Only Query/Retrieve Information Model ? FIND',  # retired
'1.2.840.10008.5.1.4.1.2.3.2': 'Patient/Study Only Query/Retrieve Information Model ? MOVE',  # retired
'1.2.840.10008.5.1.4.1.2.3.3': 'Patient/Study Only Query/Retrieve Information Model ? GET',  # retired

'1.2.840.10008.5.1.4.31': 'Modality Worklist Information Model ? FIND',
'1.2.840.10008.5.1.4.32': 'General Purpose Worklist Management Meta SOP Class',
'1.2.840.10008.5.1.4.32.1': 'General Purpose Worklist Information Model ? FIND',
'1.2.840.10008.5.1.4.32.2': 'General Purpose Scheduled Procedure Step SOP Class',
'1.2.840.10008.5.1.4.32.3': 'General Purpose Performed Procedure Step SOP Class',
'1.2.840.10008.5.1.4.33': 'Instance Availability Notification SOP Class',
'1.2.840.10008.5.1.4.37.1': 'General Relevant Patient Information Query',
'1.2.840.10008.5.1.4.37.2': 'Breast Imaging Relevant Patient Information Query',
'1.2.840.10008.5.1.4.37.3': 'Cardiac Relevant Patient Information Query',
'1.2.840.10008.5.1.4.38.1': 'Hanging Protocol Storage',
'1.2.840.10008.5.1.4.38.2': 'Hanging Protocol Information Model ? FIND',
'1.2.840.10008.5.1.4.38.3': 'Hanging Protocol Information Model ? MOVE',
}
