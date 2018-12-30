import requests
import soup as soup
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Search:

    make = ""
    model = ""
    zip_code = ""

    def __init__(self, make, model, zip_code):
        self.make = make
        self.model = model
        self.zip_code = zip_code

    def search_items(self):
        browser = webdriver.Chrome()
        root_url = 'https://www.cargurus.com/'
        browser.get(root_url)
        browser.maximize_window()

        maker = browser.find_element_by_id("carPickerUsed_makerSelect")
        maker.send_keys(self.make)

        model = browser.find_element_by_id("carPickerUsed_modelSelect")
        model.send_keys(self.model)

        zip = browser.find_element_by_name("zip")
        zip.clear()
        zip.send_keys(self.zip_code)

        browser.find_element_by_id("dealFinderForm_0").click()

        current_url = browser.current_url
        responce = requests.post(current_url)

        print(responce.text)
