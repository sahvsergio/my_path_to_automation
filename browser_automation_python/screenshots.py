def sales_screenshot(driver=driver):
    sales_summary = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]')
    sales_screenshot = sales_summary.screenshot(f'./sales-summary.png')


def order_screenshot(driver):
    ordered_robots = driver.find_element(By.ID, 'robot-preview')
    ordered_robots.screenshot('order-screenshot.png')
