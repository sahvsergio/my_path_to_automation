def create_sales_html()
    sales_table = driver.find_element(
        By.XPATH, '//*[@id="sales-results"]/table')
    sales_headers = driver.find_element(
        By.XPATH, '//*[@id="sales-results"]/table/thead')
    #sales_rows = driver.find_elements(By.XPATH,)
    performances = driver.find_elements(By.XPATH, "//*[@id='sales-results']/table/tbody/tr/td/span[@class='performance']")

   # /html/body/div/div/div/div/div[2]/div[2]/table
    table_html = pd.read_html(sales_table.get_attribute('outerHTML'),header=0)
    print()
    df=table_html[0]
    
    #if df.get_attribute('class')==''
    
    #df=table_html[0]       
    
        
    # writing table_html to an html file
    sales_headers=sales_headers
    with open('table.html', 'w') as f:
        f.write(f"""
                <table>
                   <thead>
                   <th>
                   {sales_headers.text +' Performance'}
                   </th>
                   <tbody>
                   {for row in }
                   
                   
                   </thead>
                   
                <table>
                   
                    
                    
                        
                    
                    """)   
        #f.write(table_html)
        #f.write(df)
        

def create_order_html():
 receipt=driver.find_element(By.ID,'receipt')
        receipt_html=receipt.get_attribute('outerHTML')
        with open('receipt.html','w') as f:
            f.write(receipt_html)