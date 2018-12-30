

import requests
import soup as soup
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='/Users/Suhaib/Downloads/9781789133806_Python_Automation_Code/Chapter03/chromedriver')
root_url='https://www.cargurus.com/'


browser.get(root_url)
browser.maximize_window()

maker = browser.find_element_by_id("carPickerUsed_makerSelect")
maker.send_keys("Toyota")

model = browser.find_element_by_id("carPickerUsed_modelSelect")
model.send_keys("Camry")

zip = browser.find_element_by_name("zip")
zip.clear()
zip.send_keys("38002")

browser.find_element_by_id("dealFinderForm_0").click()

for i in range(10):
    browser.find_element_by_xpath("//*[@class='nextPageElement js-go-to-next-page ']").click()




