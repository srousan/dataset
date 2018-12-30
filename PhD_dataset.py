

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
# browser.find_element_by_xpath("//*[@class='nextPageElement js-go-to-next-page ']").click()
url_result =browser.current_url
print(url_result)

m= browser.find_elements_by_xpath("//*[@id='featuredResults']")
c= m[0].find_elements_by_xpath(".//*")


for div in c:
    if div.get_attribute('src') != None:
        print(div.get_attribute('src'))
        print("------------------------------")
    if re.search('featured_listing',div.get_attribute('id'), re.IGNORECASE):
        print(div.get_attribute('id'))
        print(div.text)

        div.click()
        break
print(browser.current_url)
response = requests.get(browser.current_url)
page = BeautifulSoup(response.text, 'html.parser')


listing_summary = browser.find_elements_by_class_name("cg-listingDetail-specsWrap")
print(listing_summary[0].text)

print('***********************')
description = browser.find_elements_by_class_name("cg-listingDetail-moreDetails")
print(description[0].text)

print('***********************')


imgs = browser.find_elements_by_class_name("cg-listingStub-bodySection")
for img in imgs:
    print(img.get_attribute('class'))
    # print(img.find_elements_by_xpath(".//*")[3].text)



# m= browser.find_elements_by_xpath("//*[@id='searchResultsContainer2']")
# c= m[0].find_elements_by_xpath(".//*")
# for div in c:
#     if div.get_attribute('src') != None:
#         print(div.get_attribute('src'))
#         print("------------------------------")
#     if re.search('listing_',div.get_attribute('id')):
#         print(div.get_attribute('id'))
#         print(div.text)
#         print("------------------------------")