import os
import datetime
from speaker import tts,commands


def create_directory():
    """
    create_directory

    This function creates the  folders where the data andd output files will be located in
    Parameters: 
    - 
    Returns a tuple with the paths for each of the locations as strings: 
        - orders_data:str
          sales_data:str
          output_sale:str
          output_orders:srt
        
    """

    # establish today's date
    today = datetime.date.today().strftime(' %d-%m-%Y')
    tts.speak(commands['directories-created'])
    try:
        # input paths
        
        sales_data = os.path.join(os.pardir, 'data', f'sales{today}')
        orders_data = os.path.join(os.pardir, 'data', f'orders{today}')
        #output paths
        output_sales = os.path.join(os.pardir, 'output', f'orders{today}')

        output_orders=os.path.expanduser(os.path.join(os.pardir,'output',f'sales{today}'))

        # create the data directories
       
        os.makedirs(f'{sales_data}')
        os.makedirs(f'{orders_data}')
        # create the output  directories
        
        
        os.makedirs(f'{output_sales}')
        os.makedirs(f'{output_orders}')

        os.chdir(f'{sales_data}')
    except FileExistsError:
        os.chdir(f'{sales_data}')
    finally:
        tts.speak(commands['folder-success'])
    return orders_data,sales_data, output_sales,output_orders












