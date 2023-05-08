# os handling operations
import os


# selenium and its import
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

#getting the files
import requests

#read data 
import pandas as pd
#transform data into pdf
import pdfkit

#desktop notification
from plyer import notification

options = Options()
options.add_experimental_option('detach', True)
# creating an  instance of the webdriver
driver = webdriver.Chrome(options=options)

def sign_in(driver=driver):
    driver.get('https://robotsparebinindustries.com/')
    robospare_user =os.environ.get('robospare_user')
    robospare_pass =os.environ.get('robospare_pass')
    
    # #opening the website
    driver.implicitly_wait(10)

    # Indentify fields
    username_field = driver.find_element(By.ID, 'username')

    password_field = driver.find_element(By.ID, 'password')

    login_button = driver.find_element(By.CLASS_NAME, 'btn-primary')

    driver.implicitly_wait(10)
    # enter info on fields
    username_field.send_keys(str(robospare_user))
    driver.implicitly_wait(10)
    password_field.send_keys(str(robospare_pass))
    button_click = login_button.click()

    driver.implicitly_wait(50)
    


def create_directory():
    # download sales file
    try:
        os.mkdir('sales')
        os.mkdir('orders')
        os.chdir('sales')
    except FileExistsError:
        os.chdir('sales')
        print(os.getcwd())
    


def download_sales_file():
    sales_url = 'https://robotsparebinindustries.com/SalesData.xlsx'
    my_sales_file = pd.read_excel(sales_url)
    excel_sales = my_sales_file.to_excel('SalesData.xlsx')
    df_sheet = pd.read_excel('SalesData.xlsx')
    return df_sheet


def enter_sales(driver=driver):
    df_sheet=download_sales_file()
    # identifying all fields of sales form

    first_name_field = driver.find_element(By.ID, 'firstname')
    last_name_field = driver.find_element(By.ID, 'lastname')
    sales_target_select = driver.find_element(By.ID, 'salestarget')
    select = Select(sales_target_select)
    sales_result_field = driver.find_element(By.ID, 'salesresult')

    submit_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    # iterate dataframe to enter the content of rows into the form fields
    for first_name, last_name, sales_target, sales in zip(df_sheet['First Name'], df_sheet['Last Name'], df_sheet['Sales Target'], df_sheet['Sales']):
        # entering data for the first time in the form
        first_name_field.send_keys(f'{first_name}')
        last_name_field.send_keys(f'{last_name}')
        select.select_by_value(str(sales_target))
        sales_result_field.send_keys(f'{sales}')
        sales_click = submit_button.click()
        performance_button = driver.find_element(
            By.XPATH, '//*[@id = "root"]/div/div/div/div[2]/div[3]/button[1]')
        perfomance_button_click = performance_button.click()
        # Fluently waiting for  elements to be available
        wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
                             StaleElementReferenceException, NoSuchElementException])

        # finding the elements again after detachment from DOM to handle Stalement of element
        first_name_field = driver.find_element(
            By.XPATH, '//*[@id="firstname"]')
        last_name_field = driver.find_element(By.XPATH, '//*[@id="lastname"]')
        sales_target_select = driver.find_element(
            By.XPATH, '//*[@id="salestarget"]')
        select = Select(sales_target_select)
        sales_result_field = driver.find_element(
            By.XPATH, '//*[@id="salesresult"]')
        submit_button = driver.find_element(
            By.XPATH, '//*[@id="sales-form"]/button')


def sales_screenshot(driver=driver):
    sales_summary = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]')
    sales_screenshot = sales_summary.screenshot(f'./sales-summary.png')


def sales_to_pdf():
    # getting the outer html from table
    sales_table = driver.find_element(
        By.XPATH, '//*[@id="sales-results"]/table')
    table_html = sales_table.get_attribute('outerHTML')

    # writing table_html to an html file
    with open('table.html', 'w') as f:
        f.write(table_html)

    # reading the html as panda string of pandas dataframes
    df_html = pd.read_html('table.html')
    # slicing the 1st dataframe, which contains the text
    df_string = df_html[0].to_html()
    # creating the pdf
    pdfkit.from_string(df_string, 'table.pdf')

def log_out(driver=driver):
    log_out_button=driver.find_element(By.ID,'logout')
    log_out_button.click()
    driver.quit()
    notification.notify( title='Sales Completed', message='All orders have been completed',
                            timeout=10)
    
def download_orders_file():
    orders_url = 'https://robotsparebinindustries.com/orders.csv'
    my_order_file = pd.read_csv(order_url)
    excel_orders = my_sales_file.to_excel('SalesData.csv')
    df_sheet = pd.read_excel('SalesData.xlsx')
    return df_sheet

def notify():
    while True:
        notification.notify( title='Hello', message='Can we get whitney',
                            timeout=10)
def get_order_page(driver=driver):
    order_page=driver.find_element(
        By.XPATH, '//*[@id="root"]/header/div/ul/li[2]/a')
    order_page.click()



sign_in()
get_order_page()
    
"""
https://robotsparebinindustries.com/#/robot-order

Only the robot is allowed to get the orders file. You may not save the file manually on your computer.
The robot should save each order HTML receipt as a PDF file.
The robot should save a screenshot of each of the ordered robots.
The robot should embed the screenshot of the robot to the PDF receipt.
"""

