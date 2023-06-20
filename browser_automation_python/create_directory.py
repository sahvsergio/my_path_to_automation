def create_directory():

   
    try:
        os.mkdir('sales')
        os.mkdir('orders')
        os.chdir('sales')
    except FileExistsError:
        os.chdir('sales')