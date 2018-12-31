import base64
import requests
import json

class save_data:

    data_obj = {}
    data={}
    cars=[]
    def __init__(self, data_obj):
        self.data_obj = data_obj


    def save(self):
        print("save data here")

    def image_to_base64(self,img_url):
        img_bs4 = base64.b64encode(requests.get(img_url).content)
        return base64.encodebytes(img_bs4).decode('ascii')

    def base64_to_image(self,img_base64):
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.decodebytes(img_base64))

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


