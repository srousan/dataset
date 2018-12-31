import json
from search import Search

with open("data/make.json", "r") as obj:
        make_list = json.load(obj)

with open("data/model.json", "r") as obj:
        model_list = json.load(obj)

with open("data/zip_code.json", "r") as obj:
        zip_code_list = json.load(obj)

for make in make_list:
    for model in model_list[make]: 
        for zip_code in zip_code_list:
            s = Search(make_list[make], model["modelId"], zip_code)
            s.search_items()
            break
        break
    break

