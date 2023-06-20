def sales_to_pdf():
    # getting the outer html from table
    sales_table = driver.find_element(
        By.XPATH, '//*[@id="sales-results"]/table')
    table_html = sales_table.get_attribute('outerHTML')

    # writing table_html to an html file
    with open('table.html', 'w') as f:
        f.write(table_html)

    # reading the html as panda string of pandas dataframes
    df_html = pd.read_html('table.html')
    # slicing the 1st dataframe, which contains the text
    df_string = df_html.to_html()
    # creating the pdf
    pdfkit.from_string(df_string, 'table.pdf')
    
      #html receipt
     receipt = driver.find_element(By.ID, 'receipt')
      receipt_html = receipt.get_attribute('outerHTML')
       with open('receipt.html', 'w') as f:
            f.write(receipt_html)
        # prepare for pdf

        # create pdf
        pdfkit.from_file('receipt.html', 'order.pdf')
