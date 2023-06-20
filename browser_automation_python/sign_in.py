def sign_in(driver)


driver.implicitly_wait(10)
# enter info on fields
username_field.send_keys(str(robospare_user))
driver.implicitly_wait(10)
password_field.send_keys(str(robospare_pass))
button_click = login_button.click()


def get_order_page(driver=driver):
    driver.get(
        'https://robotsparebinindustries.com/?firstname=Vincenty&lastname=Stannering&salesresult=109884#/robot-order')

    # order_page = driver.find_element(By.XPATH, '//*[@id="root"]/header/div/ul/li[2]/a')
    # order_page.click()
    driver.implicitly_wait(20)
    alert_button = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[1]')

    alert_button.click()
