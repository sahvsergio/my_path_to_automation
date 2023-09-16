def sales_screenshot(driver=driver):
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
    sales_summary = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]')
    sales_screenshot = sales_summary.screenshot(f'./sales-summary.png')


def order_screenshot(driver=driver):
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

   # robot preview
    preview_button = driver.find_element(By.ID, 'preview')
    # order_button = driver.find_element(By.XPATH, '//*[@id="order"]')
    wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
                         StaleElementReferenceException, NoSuchElementException])
    preview_button.click()
    wait = WebDriverWait(driver, timeout=30, poll_frequency=5, ignored_exceptions=[
                         StaleElementReferenceException, NoSuchElementException])
    robots = driver.find_element(
        By.XPATH, "//div[@id='robot-preview']")
    wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
        StaleElementReferenceException, NoSuchElementException])

    robots.screenshot(f'robot_screenshot.png')
    wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
        StaleElementReferenceException, NoSuchElementException])
    # order receipt
    order_button = driver.find_element(By.XPATH, '//*[@id="order"]')
    wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
        StaleElementReferenceException, NoSuchElementException])
    order_button.click()

    receipt = driver.find_element(By.ID, 'receipt')
    wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[
        StaleElementReferenceException, NoSuchElementException])
    receipt_screenshot = receipt.screenshot(f'receipt_pic.png')
