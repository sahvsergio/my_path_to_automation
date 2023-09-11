import pandas as pd
import


def enter_sales(driver:Webdriver=driver,):
    """
    Signup

    This path operation register a user in the app
    Parameters: 
    - Request body parameter
            - user: UserRegister

    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
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


def create_orders():
    """
    Signup

    This path operation register a user in the app
    Parameters: 
    - Request body parameter
            - user: UserRegister

    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """

    # get the dataframe from the function  to be used
    csv_df = download_orders_file()

    # selectors
    # head field
    try:
        head_field = driver.find_element(By.ID, 'head')
        select_head = Select(head_field)

        # body field
        body_fields = driver.find_elements(
            By.CSS_SELECTOR, '.form-check-input')

        # legs field
        legs_field = driver.find_element(
            By.XPATH, '/html/body/div/div/div[1]/div/div[1]/form/div[3]/input')

        # address
        address_field = driver.find_element(By.ID, 'address')

        # fill out the order

        for head, body_type, legs, address in zip(csv_df['Head'], csv_df['Body'], csv_df['Legs'], csv_df['Legs']):
            select_head.select_by_value(str(head))
            for field in body_fields:
                field = field
                if field.get_attribute('value') == str(body_type):
                    field.click()

            legs_field.send_keys(legs)
            address_field.send_keys(address)

            wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
                                 StaleElementReferenceException, NoSuchElementException])

            order_screenshot()
            order_pdf()
            order_another = driver.find_element(By.ID, 'order-another')
            order_another.click()
            get_order_page()

    except StaleElementReferenceException:

        create_orders()

    finally:
        create_zip()
