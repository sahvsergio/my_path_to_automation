

import random
import shutil


#import selenium
#from selenium import webdriver
# from selenium.webdriver import Keys, ActionChains
# #from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# # waits
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# # exceptions from browser
# from selenium.webdriver.support.expected_conditions import staleness_of
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import NoSuchElementException
# # scrolling into view
# from selenium.webdriver.common.action_chains import ActionChains

# getting the files
import requests

# read data in tables
#import pandas as pd
# read data in  regular html
from bs4 import BeautifulSoup
# transform  into pdf
import pdfkit

# handle pc processes


# desktop notification



# Image processing
from PIL import Image


#import from files
from speaker import tts,commands
from create_directory import create_directory
from get_to_pags import sign_in





""" 

options = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}

# remove the message of it being controlled by automation software
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('detach', True)
options.add_experimental_option('prefs', prefs)


# creating an  instance of the webdriver
driver = webdriver.Chrome(options=options)
print(type(driver))
driver.maximize_window()
 """







if __name__=='__main__':
    tts.speak('file-started')
    orders_data,sales_data, output_sales,output_orders=create_directory()
    sign_in()
    
        
    
    