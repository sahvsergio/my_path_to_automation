import os
import datetime
from speaker import UbuntuTTS


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

    # download sales file
    today = datetime.date.today().strftime(' %d-%m-%Y')

    try:
        os.mkdir(f'sales-{today}')
        os.mkdir(f'orders-{today}')
        os.chdir(f'sales-{today}')
    except FileExistsError:
        os.chdir(f'sales-{today}')


if __name__ == '__main__':
    
    tts = UbuntuTTS()
    message = 'The files are being created'
    tts.speak(message)
    create_directory()
