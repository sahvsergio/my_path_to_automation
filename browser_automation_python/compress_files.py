def create_zip():
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
    filename = os.path.expanduser(os.path.join(os.pardir, 'zipped_orders'))
    format = 'zip'
    directory = f"{os.path.join(os.pardir,f'orders-{today}')}"
    shutil.make_archive(filename, format, directory)
    notification.notify(title='order completed',
                        message='excellent', timeout=10)
