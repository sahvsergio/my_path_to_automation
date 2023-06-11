def download_sales_file():
    sales_url = 'https://robotsparebinindustries.com/SalesData.xlsx'
    my_sales_file = pd.read_excel(sales_url)

    excel_sales = my_sales_file.to_excel('SalesData.xlsx')
    df_sheet = pd.read_excel('SalesData.xlsx')
    notification.notify(title='Sales Download', message='Sales file downloaded',
                       timeout=10)

    return df_sheet


def download_orders_file():

    os.chdir('../orders')
    order_url = 'https://robotsparebinindustries.com/orders.csv'
    csv_df = pd.read_csv(order_url)
    csv_df.set_index('Order number', inplace=True)
    csv_file = csv_df.to_csv('orders.csv')
    notification.notify(title='order file', message='Order file downloaded successfully',
                       timeout=10)
    return csv_df
