def create_sales_pdf():
    pdf_file= pdfkit.from_string(df_string, 'table.pdf')
    print(pdf_file)
    notification.notify(title='Sales pdf', message='Sales PDf created'),
                       #timeout=10)


def create_order_pdf():
    pdfkit.from_file('receipt.html','order.pdf')