import requests
from save_data import save_data
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import os
import datetime
import json


class Search:

    make = ""
    model = ""
    zip_code = ""
    log_file = ""

    def __init__(self, make, model, zip_code, log_file):
        self.make = make
        self.model = model
        self.zip_code = zip_code
        self.itemId = -1
        self.log_file = log_file
        self.log = ""

    def hr(self):
        print("--------------------------------------")

    def search_items(self):

        self.log = open(self.log_file, "a")

        with open("config.json", "r") as obj:
            config = json.load(obj)

        try:

            url = "https://www.cargurus.com/Cars/inventorylisting/ajaxFetchSubsetInventoryListing.action?sourceContext=carGurusHomePageModel"
            params = {}
            params["zip"] = self.zip_code
            params["selectedEntity"] = self.model

            result = requests.post(url=url, params=params).json()

            listings = result["listings"]
            browser = webdriver.Chrome()

            for index, item in enumerate(listings):
                self.hr()
                print("Current group progress: " +
                      str(index + 1) + "/" + str(len(listings)))
                self.hr()

                if item["noPhotos"] or os.path.exists("./data_files_imgs/" + str(item["id"])) or os.path.exists(config["google_drive_path"] + str(item["id"])):
                    print("Item ", str(item["id"]),
                          " with no images or already installed")
                    continue

                item["imgUrls"] = []
                self.itemId = item["id"]
                browser.get("https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=" +
                            self.model + "&zip="+self.zip_code+"#listing=" + str(item["id"]))
                browser.minimize_window() 
                browser.maximize_window()
                
                browser.execute_script(open("delete_svg.js").read())
                sleep(2)

                try:
                    item["dealerDescription"] = browser.find_element_by_id(
                        "#description").text
                except NoSuchElementException:
                    item["dealerDescription"] = ""

                slider = browser.find_element_by_class_name("detailsClickable")

                try:
                    slider.click()
                except WebDriverException:
                    continue

                flag = True
                add_item = True

                while flag:
                    sleep(1)
                    try:
                        image_container = browser.find_element_by_class_name(
                            "fancybox-image")
                        img_url = image_container.get_attribute("src")
                    except NoSuchElementException:
                        try:
                            image_container = browser.find_element_by_xpath(
                                '//*[local-name()="image"]')
                            img_url = image_container.get_attribute(
                                "xlink:href")
                        except NoSuchElementException:
                            add_item = False
                            break

                    if img_url in item["imgUrls"]:
                        flag = False
                        sleep(2)
                        close_button = browser.find_element_by_xpath(
                            '//*[@class="fancybox-item fancybox-close"]')
                        close_button.click()
                    else:
                        item["imgUrls"].append(img_url)
                        try:
                            next_button = browser.find_element_by_xpath(
                                '//*[@class="fancybox-nav fancybox-next"]')
                            next_button.click()
                        except NoSuchElementException:
                            flag = False
                            sleep(2)
                            close_button = browser.find_element_by_xpath(
                                '//*[@class="fancybox-item fancybox-close"]')
                            close_button.click()

                if add_item:
                    s = save_data(item)
                    s.save()

            browser.quit()
        except:
            self.log.write("-----------------------------\n")
            self.log.write(str(datetime.datetime.now()))
            self.log.write(str("\nError happened at make : " + str(self.make)))
            self.log.write(
                str("\nError happened at model : " + str(self.model)))
            self.log.write(str("\nitem id : " + str(self.itemId)))
            self.log.write("\n-----------------------------\n")
