#! /usr/bin/env python3
import os
import requests
user = os.getenv('USER')
path = "/home/{}/supplier-data/descriptions".format(user)
dic = {}
txtlist = os.listdir(path)
for file in txtlist:
    with open(path+'/'+file, 'r') as txtfile:
        lines = txtfile.readlines()
        # get data individually
        dic['name'] = lines[0].strip()
        weight =  lines[1].strip().strip("lbs")
        dic['weight'] =  int(weight)
        dic['description'] = lines[2].strip()
        dic['image_name'] =os.path.splitext(file)[0]+'.jpeg'

    response = requests.post("http://34.74.15.104/fruits/",data = dic)

