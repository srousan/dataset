import json
import requests
import base64
import os
import urllib.request

class save_data:

    data_obj = {}
    data={}
    cars=[]
    def __init__(self, data_obj):
        self.data_obj = data_obj

    def extract_urls_to_files(self,dir):
        img_urls = self.data_obj.get("imgUrls")
        counter = 1
        for url in img_urls:
            full_path =dir+ '/img_'+ str(counter) + '.png'
            bs64=self.image_to_base64(url)
            self.base64_to_image(bs64,full_path)
            counter = counter + 1 

    def save(self):
        directory='data_files_imgs'
        id = self.data_obj.get("id")
        directory = directory + '/' + str(id)
        img_directory = directory+ '/imgs'

        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(img_directory):
            os.makedirs(img_directory) 
       
        self.extract_urls_to_files(img_directory) 
        self.data['cars']=self.data_obj
        with open(directory+'/one_car.json', 'w') as outfile:
            json.dump(self.data, outfile)

    def image_to_base64(self,img_url):
        img_bs4 = base64.b64encode(requests.get(img_url).content)
        return img_bs4
        # return base64.encodebytes(img_bs4).decode('ascii')

    def base64_to_image(self,img_base64,full_path):
        with open(full_path, "wb") as fh:
            fh.write(base64.decodebytes(img_base64))
            # fh.write(base64.decodebytes(img_base64))

    def text_to_dic(self,text,discription,img_urls):
        dic_car={}
        lines = str(text).splitlines()
        for line in lines:
            dic_line=line.split(':')
            dic_car[dic_line[0]]=dic_line[1]
        dic_car['description'] = discription
        dic_car['imgs_urls']=img_urls
        dic_car['imgs_urls'] = list(map(self.image_to_base64, img_urls))
        print(list(map(self.image_to_base64, img_urls)))
        self.cars.append(dic_car)
        print(dic_car)

    def save_to_jason(self):
        self.data['cars']=self.cars
        with open('data_bs4.json', 'w') as outfile:
            json.dump(self.data, outfile)


