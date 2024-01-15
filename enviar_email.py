import smtplib
from email.message import EmailMessage


def obter_token_email() -> str:
    with open('token_email.txt', 'r') as file:
        email, token = file.readlines()
    email = email.split('\n')[0]
    return email, token


EMAIL, TOKEN = obter_token_email()
