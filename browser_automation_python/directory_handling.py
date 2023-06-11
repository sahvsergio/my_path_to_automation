
def create_directory():

    # download sales file
    try:
        os.mkdir('sales')
        os.mkdir('orders')
        os.chdir('sales')
        notification.notify(title='Directory creation', message='Directories created',
                           timeout=10)
    except FileExistsError:
        os.chdir('sales')
        notification.notify(title='Moving to directory', message='moved to the sales directory',
                       timeout=10)