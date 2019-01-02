import json
from input_list import InputList

def hr():
        print("--------------------------------------")

with open("data/make.json", "r") as obj:
        make_list = json.load(obj)

with open("data/model.json", "r") as obj:
        model_list = json.load(obj)

with open("data/zip_code.json", "r") as obj:
        zip_code_list = json.load(obj)

hr()    
print("commands:")
print("1-10 : for range of indexes")
print("1,3,8 : for selected indexes")
print("all : for the whole list")
hr()

hr()
for index, zip in enumerate(zip_code_list):
        print(str(index) + " : " +  zip)
hr()

flag = True
while flag:

        zip_code = input("Enter zip code/s:")

        if zip_code.lower() == "all":
                flag = False
                range = []
                for index, zip in enumerate(zip_code_list):
                        range.append(index)

        elif "-" in zip_code:
                range = zip_code.split("-")
                try: 
                        start = int(range[0])
                        end = int(range[1])
                        range = []
                        while start <= end:
                                range.append(start)
                                start += 1

                        flag = False
                except:
                        print("Value entered not valid")
                        hr()

        elif "," in zip_code:

                range = zip_code.split(",")
                try:
                        for index, r in enumerate(range):
                                range[index] = int(range[index])
                        flag = False
                except:
                        print("Value entered not valid")
                        hr()
        else: 
                range = []
                try:
                        range.append(int(zip_code))
                        flag = False
                except:
                        print("Value entered not valid")
                        hr()

hr()

zip_code_list_param = []

for item in range:
        zip_code_list_param.append(zip_code_list[item])

temp_make_list = []
for index, make in enumerate(make_list):
        print(index, make, make_list[make])
        obj = {}
        obj[make] = make_list[make]
        temp_make_list.append(obj) 

hr()

flag = True
range = []

while flag:
        make = input("Enter make/s:")

        if make.lower() == "all":
                flag = False
                for index, make in enumerate(make_list):
                        range.append(index)
        elif "-" in make:

                range = make.split("-")
                try: 
                        start = int(range[0])
                        end = int(range[1])
                        range = []
                        while start <= end:
                                range.append(start)
                                start += 1
                        flag = False
                except:
                        print("Value entered not valid")
                        hr()

        elif "," in make:

                range = make.split(",")
                try:
                        for index, r in enumerate(range):
                                range[index] = int(range[index])
                        flag = False
                except:
                        print("Value entered not valid")
                        hr()
        else: 
                range = []
                try:
                        range.append(int(make))
                        flag = False
                except:
                        print("Value entered not valid")
                        hr()

make_list_param = {}

for item in range:
        make_list_param.update(temp_make_list[item])  

hr()
print("Your inputs as below: ")
hr()
print("Zipcodes:")
print(zip_code_list_param)     
hr()
print("Makes:")
print(make_list_param)
hr()
input("Enter to start ... ")

input_ist = InputList(make_list_param,model_list,zip_code_list_param)
input_ist.run_item()

