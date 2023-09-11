def create_directory():
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
    tts.speak('the directories are being created')

    # download sales file
    today = datetime.date.today().strftime(' %d-%m-%Y')

    try:
        os.mkdir(f'sales-{today}')
        os.mkdir(f'orders-{today}')
        os.chdir(f'sales-{today}')
    except FileExistsError:
        os.chdir(f'sales-{today}')
