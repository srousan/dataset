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
        print(self.make + " " + self.model + " " + self.zip_code)
