#!/usr/bin/env python3
import requests
import os
import glob
from PIL import Image
# This example shows how a file can be uploaded using
# The Python Requests module
user = os.getenv('USER')
url = "http://localhost/upload/"
src_dir  = '/home/{}/supplier-data/images'.format(user)

for images in glob.iglob(f'{src_dir}/*.jpeg'):
    img = Image.open(images)
    with open(img.filename, 'rb') as opened:
       r = requests.post(url, files={'file': opened})
