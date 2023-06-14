import os


import selenium
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# waits
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
# exceptions from browser
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
# scrolling into view
from selenium.webdriver.common.action_chains import ActionChains

# getting the files
import requests

# read data in tables
import pandas as pd
# read data in  regular html
from bs4 import BeautifulSoup
# transform  into pdf
import pdfkit

# desktop notification
from plyer import notification

options = Options()
options.add_experimental_option('detach', True)
# creating an  instance of the webdriver
driver = webdriver.Chrome(options=options)
