def get_order_page(driver=driver):
    order_url= '/firstname=Vincenty&lastname=Stannering&salesresult=109884#/robot-order'
    driver.get('')
        

    # order_page = driver.find_element(By.XPATH, '//*[@id="root"]/header/div/ul/li[2]/a')
    # order_page.click()
    driver.implicitly_wait(20)
    alert_button = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[1]')

    alert_button.click()
    notification.notify(title='order page', message='Order page visited successfully',
                       timeout=10)

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
        order_buttn=driver.find_element(By.ID, 'order')
        driver.implicitly_wait(10)
        order_button.click()
        
        
        