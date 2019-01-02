from search import Search

class InputList:

    input_list_make = []
    input_list_model = []
    input_list_zip_code = []
    
    def __init__(self, input_list_make, input_list_model, input_list_zip_code):
        self.input_list_make = input_list_make
        self.input_list_model = input_list_model
        self.input_list_zip_code = input_list_zip_code

    def run_item(self):
        for make in self.input_list_make:
            for model in self.input_list_model[make]: 
                for zip_code in self.input_list_zip_code:
                    s = Search(self.input_list_make[make], model["modelId"], zip_code)
                    s.search_items()