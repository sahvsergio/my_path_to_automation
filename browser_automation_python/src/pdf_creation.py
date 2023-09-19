from create_directory i import output_sales
def sales_to_pdf():
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
    # base xpath for sales table
    sales_table = driver.find_element(
        By.XPATH, '//*[@id="sales-results"]/table')

    # xpath for table headers , it returns a list of webdriver elements
    table_header = driver.find_elements(
        By.XPATH, '//*[@id="sales-results"]/table/thead/tr/th')
    # xpath for name rows
    name_rows = driver.find_elements(
        By.XPATH, '//*[@id="sales-results"]/table/tbody/tr[position() mod 2!=0]/td[1]')

    # xpath for target
    target_rows = driver.find_elements(
        By.XPATH, "// *[@id='sales-results']/table/tbody/tr/td[2]")
    # regular_table_rows=
    result_rows = driver.find_elements(
        By.XPATH, "// *[@id='sales-results']/table/tbody/tr/td[3]")
    difference_rows = driver.find_elements(
        By.XPATH, "// *[@id='sales-results']/table/tbody/tr/td[4]")

    performance_rows = driver.find_elements(
        By.XPATH, "//*[@id = 'sales-results']/table/tbody/tr/td/span[@class='performance']")

    # create a new empty list to store  text from webdriver elements in table_header
    header_text = []
    # loop through the table_header and the performance_rows
    name_texts = []
    target_texts = []
    results_texts = []
    difference_texts = []
    performance_texts = []

    for header_title in table_header:
        # extract text from  each individual webdriver elements in table_header
        header_title_text = header_title.text
        # append each text to the empty list table_header_text
        header_text.append(header_title_text)

    for name in name_rows:
        name_text = name.text
        name_texts.append(name_text)

    for target_row in target_rows:
        target_text = (target_row.text)
        target_texts.append(target_text)

    for result in result_rows:
        result_text = (result.text)
        results_texts.append(result_text)

    for difference in difference_rows:
        difference_text = (difference.text)
        difference_texts.append(difference_text)

    for performance_row in performance_rows:
        performance_row_text = performance_row.text
        performance_texts.append(performance_row_text)

    # create df
    df = pd.DataFrame(columns=header_text)
    df['Name'] = name_texts

    # insert values into each column of the dataframe
    df['Target'] = target_texts
    df['Result'] = results_texts
    df['Difference'] = difference_texts

   # add new dataframe column Performance
    df['Performance'] = performance_texts

    # style the dataframe

    properties = {"border": "4px solid black", "color": "black",
                  "font-size": "16px", 'text-align': 'center', 'align': 'center'}
    df_header_styles = {
        'selector': 'th:not(.index_name)',
        'props': [('border', '5px,solid,black'), ('background-color', 'green'), ('padding', 'auto')]
    }
    styled_df = df.style.set_properties(
        **properties).hide(axis='index').set_table_styles([df_header_styles])

    # df.to_html('table.html',index=False,col_space=20)

    # turn  df into html
    styled_df.to_html('table.html', header=False, index=False, col_space=20,)

    css = """
        table {
          margin:auto,auto;
        }
    """

    # create pdf out of html file
    pdfkit.from_file('table.html', 'table.pdf',)


def order_pdf():
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
    today = datetime.date.today().strftime(' %d-%m-%Y')
    pdf_file = 'order.pdf'

    # filepaths for both pictures
    image_filepath1 = f'../orders-{today}/receipt_pic.png'
    image_filepath2 = f'../orders-{today}/robot_screenshot.png'
    # opening both pictures
    image_1 = Image.open(image_filepath1)
    image_2 = Image.open(image_filepath2)
    # calculating the pdf with and height based on images  height
    pdf_width = max(image_1.width, image_2.width)
    pdf_height = image_1.height+image_2.height

    # create blank picture
    pdf = Image.new('RGB', (pdf_width, pdf_height), (255, 255, 255))
    # pasting both images one after the other stacked vertically
    pdf.paste(image_1, (0, 0))
    pdf.paste(image_2, (0, image_1.height))
    # saving the canvas as pdf
    pdf.save(pdf_file, save_all=True)
