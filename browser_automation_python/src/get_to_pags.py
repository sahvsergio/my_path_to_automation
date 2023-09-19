import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
driver.maximize_window() """



def sign_in(driver: selenium.webdriver.chrome.webdriver.WebDriver = webdriver):
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

    options.add_argument('--disable-save-password-bubble')
    return driver


def get_order_page(driver=webdriver):
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
    try:
        prder_robot = driver.find_element(
            By.LINK_TEXT, 'Order your robot!').click()

        # order_page = driver.find_element(By.XPATH, '//*[@id="root"]/header/div/ul/li[2]/a')
        # order_page.click()
        driver.implicitly_wait(20)
        alert_button = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[1]')

        alert_button.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        ok_button = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[1]')
        wait = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(ok_button)).click()


def log_out(driver=webdriver):
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

    notification.notify(title='Bye',
                        message='it\'s time to say goodbye', timeout=10)
    driver.quit()
