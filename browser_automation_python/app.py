import os
import time


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
import numpy as np

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
driver.maximize_window()


base_url=https://robotsparebinindustries.com/










   


    # reading the html as panda string of pandas dataframes
    #df_html = pd.read_html('table.html', header=0)
    
    
 
   
    
    
    
    
    #print(df_html)
    # slicing the 1st dataframe, which contains the text
    #df_string = df_html[0].to_html()
    
    #
#jjorders






        #html receipt
       
        #prepare for pdf
        
     
    
        #create pdf
       
        
        #screenshot
      
        
        
        





sign_in()
create_directory()
download_sales_file
enter_sales()
sales_screenshot()
sales_to_pdf()
#download_orders_file()
#get_order_page()
#create_orders()
#log_out()

"""
https://robotsparebinindustries.com/#/robot-order

Only the robot is allowed to get the orders file. You may not save the file manually on your computer.
The robot should save each order HTML receipt as a PDF file.
The robot should save a screenshot of each of the ordered robots.
The robot should embed the screenshot of the robot to the PDF receipt.
"""
