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

    driver.implicitly_wait(50)

    notification.notify(title='Sign in completed', message='Sign in completed',
                   timeout=10)