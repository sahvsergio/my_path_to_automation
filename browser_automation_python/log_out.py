def log_out(driver=driver):
    log_out_button = driver.find_element(By.ID, 'logout')
    log_out_button.click()
    driver.quit()
    notification.notify(title='Sales Completed', message='All orders have been completed',
                        timeout=10)
