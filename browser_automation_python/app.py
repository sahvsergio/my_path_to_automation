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

#Image processing
from PIL import Image


options = Options()

# remove the message of it being controlled by automation software
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('detach', True)


# creating an  instance of the webdriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()


def sign_in(driver=driver):
    # opening the website
    driver.get('https://robotsparebinindustries.com/')
    # environment variables
    robospare_user = os.environ.get('robospare_user')
    robospare_pass = os.environ.get('robospare_pass')
    

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


def create_directory():

    # download sales file
    try:
        os.mkdir('sales')
        os.mkdir('orders')
        os.chdir('sales')
    except FileExistsError:
        os.chdir('sales')


def download_sales_file():
    sales_url = 'https://robotsparebinindustries.com/SalesData.xlsx'
    my_sales_file = pd.read_excel(sales_url)
    excel_sales = my_sales_file.to_excel('SalesData.xlsx')
    df_sheet = pd.read_excel('SalesData.xlsx')
    return df_sheet


def enter_sales(driver=driver):
    df_sheet = download_sales_file()
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
    # base xpath for sales table
    sales_table = driver.find_element(
        By.XPATH, '//*[@id="sales-results"]/table')

    # xpath for table headers , it returns a list of webdriver elements
    table_header = driver.find_elements(
        By.XPATH, '//*[@id="sales-results"]/table/thead/tr/th')
    # xpath for name rows
    name_rows = driver.find_elements(
        By.XPATH, '//*[@id="sales-results"]/table/tbody/tr[position() mod 2!=0]/td[1]')

    # xpath for target
    target_rows = driver.find_elements(
        By.XPATH, "// *[@id='sales-results']/table/tbody/tr/td[2]")
    # regular_table_rows=
    result_rows = driver.find_elements(
        By.XPATH, "// *[@id='sales-results']/table/tbody/tr/td[3]")
    difference_rows = driver.find_elements(
        By.XPATH, "// *[@id='sales-results']/table/tbody/tr/td[4]")

    performance_rows = driver.find_elements(
        By.XPATH, "//*[@id = 'sales-results']/table/tbody/tr/td/span[@class='performance']")

    # create a new empty list to store  text from webdriver elements in table_header
    header_text = []
    # loop through the table_header and the performance_rows
    name_texts = []
    target_texts = []
    results_texts = []
    difference_texts = []
    performance_texts = []

    for header_title in table_header:
        # extract text from  each individual webdriver elements in table_header
        header_title_text = header_title.text
        # append each text to the empty list table_header_text
        header_text.append(header_title_text)

    for name in name_rows:
        name_text = name.text
        name_texts.append(name_text)

    for target_row in target_rows:
        target_text = (target_row.text)
        target_texts.append(target_text)

    for result in result_rows:
        result_text = (result.text)
        results_texts.append(result_text)

    for difference in difference_rows:
        difference_text = (difference.text)
        difference_texts.append(difference_text)

    for performance_row in performance_rows:
        performance_row_text = performance_row.text
        performance_texts.append(performance_row_text)

    # create df
    df = pd.DataFrame(columns=header_text)
    df['Name'] = name_texts

    # insert values into each column of the dataframe
    df['Target'] = target_texts
    df['Result'] = results_texts
    df['Difference'] = difference_texts

   # add new dataframe column Performance
    df['Performance'] = performance_texts
    
    #style the dataframe
    
    properties = {"border": "2px solid black", "color": "black", "font-size": "16px",'text-align':'center','align':'center'}
    df_header_styles={
        'selector':'th:not(.index_name)',
        'props':[('border','5px,solid,black'),('background-color','green'), ('padding', 'auto')]
    }
    styled_df=df.style.set_properties(**properties).hide(axis='index').set_table_styles([df_header_styles])
    
    
    #df.to_html('table.html',index=False,col_space=20)

    #turn  df into html
    styled_df.to_html('table.html',header=False,index=False,col_space=20,)
    
    css = """
        table {
          margin: 0 auto;
        }
    """

    


    # create pdf out of html file
    pdfkit.from_file('table.html','table.pdf',)


def download_orders_file():

    os.chdir('../orders')
    order_url = 'https://robotsparebinindustries.com/orders.csv'
    csv_df = pd.read_csv(order_url)
    csv_df.set_index('Order number', inplace=True)
    csv_file = csv_df.to_csv('orders.csv')
    return csv_df


def get_order_page(driver=driver):
    driver.find_element(By.LINK_TEXT, 'Order your robot!').click()

    # order_page = driver.find_element(By.XPATH, '//*[@id="root"]/header/div/ul/li[2]/a')
    # order_page.click()
    driver.implicitly_wait(20)
    alert_button = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[1]')

    alert_button.click()


def create_orders():

    # get the dataframe from the function  to be used
    csv_df = download_orders_file()

    # selectors
    # head field
    head_field = driver.find_element(By.ID, 'head')
    select_head = Select(head_field)

    # body field
    body_fields = driver.find_elements(By.CSS_SELECTOR, '.form-check-input')

    # legs field
    legs_field = driver.find_element(
        By.XPATH, '/html/body/div/div/div[1]/div/div[1]/form/div[3]/input')

    # address
    address_field = driver.find_element(By.ID, 'address')
    # preview button
    preview_button = driver.find_element(By.ID, 'preview')
    order_button = driver.find_element(By.XPATH, '//*[@id="order"]')

    # fill out the order

    for head, body_type, legs, address in zip(csv_df['Head'], csv_df['Body'], csv_df['Legs'], csv_df['Legs']):

        driver.implicitly_wait(10)

        select_head.select_by_value(str(head))
        for field in body_fields:
            field = field
            if field.get_attribute('value') == str(body_type):
                field.click()

        legs_field.send_keys(legs)
        address_field.send_keys(address)
        wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
            StaleElementReferenceException, NoSuchElementException])        
        

        preview_button.click()
        # show order
        order_button = driver.find_element(By.ID, 'order')
        wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
           StaleElementReferenceException, NoSuchElementException])  
        order_button.click()

        # html receipt
       
        
        receipt = driver.find_element(By.ID, 'receipt') 
        
        wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
           StaleElementReferenceException, NoSuchElementException])       
        receipt_screenshot = receipt.screenshot('receipt_pic.png')
        
        #robot preview       
        robots = driver.find_element(
            By.XPATH, "//div[@id='robot-preview']")
        wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
            StaleElementReferenceException, NoSuchElementException])  
        #driver.execute_script("document.body.style.zoom='90%'")
        
        robots.screenshot('robot_screenshot.png')
        #name for the final pdf
        pdf_file='order.pdf'
        
        #filepaths for both pictures
        image_filepath1='../orders/receipt_pic.png'
        image_filepath2='../orders/robot_screenshot.png'
        #opening both pictures
        image_1=Image.open(image_filepath1)
        image_2=Image.open(image_filepath2)
        #calculating the pdf with and height based on images  height
        pdf_width=max(image_1.width,image_2.width)
        pdf_height=image_1.height+image_2.height
        
        #create blank picture
        pdf=Image.new('RGB',(pdf_width,pdf_height),(255,255,255))
        #pasting both images one after the other stacked vertically
        pdf.paste(image_1,(0,0))
        pdf.paste(image_2,(0,image_1.height))
        #saving the canvas as pdf
        pdf.save(pdf_file, save_all=True)
        
        
        
        
        
        order_another=driver.find_element(By.ID,'order-another')
        order_another.click()
        image_file.save(image_pdf,save_all=True,append_images=image_file)
        """
        
        # prepare for pdf

        # create pdf
        # pdfkit.from_file('receipt.html', 'order.pdf')

        # screenshot

        

        driver.execute_script("document.body.style.zoom='90%'")
        ordered_robots.screenshot()
        order_another_button=driver.find_element(By.ID, 'order-another')
        order_another_button.click()
        
        pdfkit.from_file(
            ['receipt_pic.png', 'robot_screenshot.png'], 'order-pdf.pdf')
        wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
            StaleElementReferenceException, NoSuchElementException])
       
        

    # notification.notify(title='order completed',
        # message='excellent', timeout=10)


def log_out(driver=driver):
    pass
"""

sign_in()
create_directory()
enter_sales()
sales_screenshot()
sales_to_pdf()
download_orders_file()
get_order_page()
create_orders()
# log_out()

"""
https://robotsparebinindustries.com/#/robot-order
""""""

Only the robot is allowed to get the orders file. You may not save the file manually on your computer.
The robot should save each order HTML receipt as a PDF file.
The robot should save a screenshot of each of the ordered robots.
The robot should embed the screenshot of the robot to the PDF receipt.
"""