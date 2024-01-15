

def obter_token_email() -> str:
    with open('token_email.txt', 'r') as file:
        TOKEN = file.read()
    return TOKEN


