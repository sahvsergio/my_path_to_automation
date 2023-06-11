def sales_screenshot(driver=driver):
    sales_summary = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]')
    #driver.get_screenshot_as_file('../hello.png')
    
    sales_screenshot = sales_summary.screenshot(f'./sales-summary.png')
    notification.notify(title='Screenshot', message='Screenshot for sales completed',
                       timeout=10)
    
def order_screenshot():
    ordered_robots = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div/div")
        
        

        
        ordered_robots.screenshot('order-screenshot.png')
    notification.notify(title='order completed',
                        message='excellent', timeout=10)