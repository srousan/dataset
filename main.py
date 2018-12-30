import json
from search import Search


with open("data/make.json", "r") as obj:
        make_list = json.load(obj)

with open("data/input_m&m.json", "r") as obj:
        input = json.load(obj)

makes_ids = list(make_list.keys())
#print(makes_ids[0])
print(make_list[makes_ids[0]])

#print(input[0]["Name"])
#s = Search("Toyota", "Camry" , "38002")
#s.search_items()