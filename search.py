import requests
from save_data import save_data


class Search:

    make = ""
    model = ""
    zip_code = ""

    def __init__(self, make, model, zip_code):
        self.make = make
        self.model = model
        self.zip_code = zip_code

    def search_items(self):
        url = "https://www.cargurus.com/Cars/inventorylisting/ajaxFetchSubsetInventoryListing.action?sourceContext=carGurusHomePageModel"
        params = {
            zip: self.zip_code
        }
        result = requests.post(url=url, params=params).json()

        listings = result["listings"]

        for item in listings:
            url = "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=" + self.model + "&zip="+self.zip_code+"#listing=" + str(item["id"])
            result = requests.post(url=url)
            print(str(result))
            break