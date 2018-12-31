

import requests
import soup as soup
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from save_data import save_data

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

img_urls=['https://static.cargurus.com/images/forsale/2018/11/05/20/54/2015_toyota_camry-pic-2578532806027757717-1024x768.jpeg','https://static.cargurus.com/images/forsale/2018/11/05/20/54/2015_toyota_camry-pic-2578532806027757717-1024x768.jpeg']
s=save_data("")

print('***********************')
description = browser.find_elements_by_class_name("cg-listingDetail-moreDetails")
print(description[0].text)

print('***********************')
s.text_to_dic(listing_summary[0].text,description[0].text,img_urls)
s.text_to_dic(listing_summary[0].text,description[0].text,img_urls)
s.save_to_jason()



imgs= browser.find_elements_by_xpath("//*[@id='listingDetailFauxPage']/div[5]/div[3]/div[2]/div[1]/div[1]")
main_images=imgs[0].find_elements_by_xpath(".//*")
for img in main_images:
    if img.get_attribute('src') != None:
        print(img.get_attribute('src'))

imgs= browser.find_elements_by_xpath("//*[@id='listingDetailFauxPage']/div[5]/div[3]/div[2]/div[1]/div[2]")
main_images=imgs[0].find_elements_by_xpath(".//*")
main_images[4].click()


imgs= browser.find_elements_by_xpath("//*[@id='listingDetailFauxPage']/div[5]/div[3]/div[2]/div[1]/div[1]")
main_images=imgs[0].find_elements_by_xpath(".//*")
for img in main_images:
    if img.get_attribute('src') != None:
        print(img.get_attribute('src'))


# for img in main_images:
#     print(img.get_attribute('class'))
#     print(img.get_attribute('style'))




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