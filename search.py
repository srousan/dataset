import requests
from save_data import save_data
from selenium import webdriver
from time import sleep 
from selenium.common.exceptions import NoSuchElementException

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
        params = {}
        params["zip"] = self.zip_code
        params["selectedEntity"] = self.model
        
        result = requests.post(url=url, params=params).json()

        listings = result["listings"]
        browser = webdriver.Chrome()

        for item in listings:

            if item["noPhotos"]:
                continue

            item["imgUrls"] = []
            browser.get("https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=" + self.model + "&zip="+self.zip_code+"#listing=" + str(item["id"]))
            browser.maximize_window()
            browser.execute_script(open("delete_svg.js").read())
            sleep(2)

            item["dealerDescription"] = browser.find_element_by_id("#description").text

            slider = browser.find_element_by_class_name("detailsClickable")
            slider.click()
            flag = True

            while flag:
                sleep(1)
                try:
                    image_container = browser.find_element_by_class_name("fancybox-image")
                except NoSuchElementException:
                    next_button = browser.find_element_by_xpath('//*[@class="fancybox-nav fancybox-next"]')
                    next_button.click()
                    continue

                img_url = image_container.get_attribute("src")

                if img_url in item["imgUrls"]:
                    flag = False
                    close_button = browser.find_element_by_xpath('//*[@class="fancybox-item fancybox-close"]')
                    close_button.click()
                else:
                    item["imgUrls"].append(img_url)
                    next_button = browser.find_element_by_xpath('//*[@class="fancybox-nav fancybox-next"]')
                    next_button.click()

            s = save_data(item)
            s.save()

        browser.quit()

         