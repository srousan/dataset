import json
from input_list import InputList
import os


def hr():
    print("--------------------------------------")


def get_model(model_list, make):
    hr()
    flag = True
    while flag:
        models = input("Enter model/s for " + make_list[make] + " / " + make + " :")
        if models.lower() == "all":
            flag = False
            return model_list

        elif "-" in models:
            range = models.split("-")
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
        elif "," in models:
            range = models.split(",")
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
                range.append(int(models))
                flag = False
            except:
                print("Value entered not valid")
                hr()

    model_list_param = []
    for item in range:
            model_list_param.append(model_list[item])
    
    return model_list_param


with open("data/make.json", "r") as obj:
    make_list = json.load(obj)

with open("data/model.json", "r") as obj:
    model_list = json.load(obj)

with open("data/zip_code.json", "r") as obj:
    zip_code_list = json.load(obj)

if os.path.exists("log.txt"):
    os.remove("log.txt")
    open("log.txt", "x")
else:
    open("log.txt", "x")

hr()
print("commands:")
print("1-10 : for range of indexes")
print("1,3,8 : for selected indexes")
print("all : for the whole list")
hr()

hr()
for index, zip in enumerate(zip_code_list):
    print(str(index) + " : " + zip)
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
model_list_param = {}
for make in make_list_param:
    for index, model in enumerate(model_list[make]):
        print(index, model["modelName"], model["modelId"])
    model_list_param[make] = get_model(model_list[make], make)

hr()
print("Your inputs as below: ")
hr()
print("Zipcodes:")
print(zip_code_list_param)
hr()
print("Makes:")
print(make_list_param)
hr()
print("Models:")
print(model_list_param)
hr()
input("Enter to start ... ")

input_ist = InputList(make_list_param,model_list_param,zip_code_list_param)
input_ist.run_item()
