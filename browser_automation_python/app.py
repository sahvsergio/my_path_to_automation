



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
    df_string = df_html.to_html()
    # creating the pdf
    pdfkit.from_string(df_string, 'table.pdf')


def download_orders_file():

    os.chdir('../orders')
    order_url = 'https://robotsparebinindustries.com/orders.csv'
    csv_df = pd.read_csv(order_url)
    csv_df.set_index('Order number', inplace=True)
    csv_file = csv_df.to_csv('orders.csv')
    return csv_df


def get_order_page(driver=driver):
    driver.get(
        'https://robotsparebinindustries.com/?firstname=Vincenty&lastname=Stannering&salesresult=109884#/robot-order')

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
    
    #legs field
    legs_field = driver.find_element(
        By.XPATH, '/html/body/div/div/div[1]/div/div[1]/form/div[3]/input')
    
    # address
    address_field=driver.find_element(By.ID,'address')
    #preview button 
    preview_button=driver.find_element(By.ID, 'preview')
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
        #preview robot
        
        preview_button.click()
        #show order
        order_butotn=driver.find_element(By.ID, 'order')
        order_button.click()
        
        
        
        #html receipt
        receipt=driver.find_element(By.ID,'receipt')
        receipt_html=receipt.get_attribute('outerHTML')
        with open('receipt.html','w') as f:
            f.write(receipt_html)
        #prepare for pdf
        
     
    
        #create pdf
        pdfkit.from_file('receipt.html','order.pdf')
        
        #screenshot
        ordered_robots = driver.find_element(
            By.ID, 'robot-preview')
        ordered_robots.screenshot('order-screenshot.png')
        
        
        
            
        
        
        
     
    
        
        
def order_pdf():
    pdf_file='order.pdf'
        
    #filepaths for both pictures
    image_filepath1=f'../orders/receipt_pic.png'
    image_filepath2='../orders/robot_screenshot.png'
    #opening both pictures
    image_1=Image.open(image_filepath1)
    image_2=Image.open(image_filepath2)
    #calculating the pdf with and height based on images  height
    pdf_width=max(image_1.width,image_2.width)
    pdf_height=image_1.height+image_2.height
        
        
        
        
        
    notification.notify(title='order completed',
                        message='excellent', timeout=10)
        
        


def log_out(driver=driver):
    log_out_button = driver.find_element(By.ID, 'logout')
    log_out_button.click()
    driver.quit()
    notification.notify(title='Sales Completed', message='All orders have been completed',
                        timeout=10)


# paautopep8sign_in()
create_directory()
# enter_sales()
# sales_screenshot()
# sales_to_pdf()
download_orders_file()
get_order_page()
create_orders()
# log_out()

"""
https://robotsparebinindustries.com/#/robot-order"""
