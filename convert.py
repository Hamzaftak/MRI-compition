import os
import pathlib
import dicom2nifti
import shutil
# import pdb

parent_dir = pathlib.Path("D:/MRI/train/train")
subjects = parent_dir.iterdir()
for subject in subjects:
    if os.path.isdir(subject):
        images = subject.iterdir()
        for image in images:
            if os.path.isdir(image):
                try:
                    dicom2nifti.dicom_series_to_nifti(image, image.parts[-1], reorient_nifti=True)
                    file_name = image.parts[-1] + ".nii"
                    source = file_name
            #source = image / file_name
#            pdb.set_trace()
                    shutil.move(str(source),str(subject))
                    shutil.rmtree(image)
                except:
                    print("Error in" + str(subject))
            

    