import glob
from PIL import Image



# get the path/directory
src_dir  = '/home/student-01-26cc9823f863/supplier-data/images'



# iterate over files in
# that directory
for images in glob.iglob(f'{src_dir}/*.tiff'):
    img = Image.open(images)
    filename = img.filename[50:-5]
    img.resize((600,400)).convert('RGB').save('/home/student-01-26cc9823f863/supplier-data/images/'+str(filename)+'.jpeg')
