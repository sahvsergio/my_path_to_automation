import datetime
import os
import pandas as pd
from pandas.core.frame import DataFrame
from create_directory import orders_data,sales_data



def download_sales_file(sales_data: str = sales_data, sales_url: str = 'https://robotsparebinindustries.com/SalesData.xlsx') -> DataFrame:
    """
    download_sales_file
    This function downloads an excel file with the xlsx extension
    Parameters: 
    - sales files url:
            - user: UserRegister

    Returns a dataframe with the sales information for each salesperson: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    sales_url = sales_url
    my_sales_file = pd.read_excel(sales_url)
    excel_sales = my_sales_file.to_excel(f'SalesData.xlsx')
    df_sheet = pd.read_excel('SalesData.xlsx')
   
    return df_sheet


def download_orders_file(order_url: str = 'https://robotsparebinindustries.com/orders.csv', orders_data :str = orders_data) -> DataFrame:
    """
    download_orders_file

    this function downloads a csv file
    Parameters: 
    - order_url:str
      order_data:str

    Returns a Dataframe with the basic user order: 
        - csv_df:Dataframe
    """
    
    csv_df = pd.read_csv(order_url)
    csv_df.set_index('Order number', inplace=True)
    csv_file = csv_df.to_csv(os.path.expanduser(os.path.join(os.pardir,orders_data,'orders.csv')))
    
    return csv_df

