import smtplib
from email.message import EmailMessage



def obter_token_email() -> str:
    with open('token_email.txt', 'r') as file:
        email, token = file.readlines()
    email = email.split('\n')[0]
    return email, token



def anexar_arquivo(arquivo, email: EmailMessage):
    with open(arquivo, 'rb') as file:
        dados = file.read()
        filename = file.name
        email.add_attachment(dados, maintype="application", subtype='octet-stream', filename=filename)



def email_setting(EMAIL:str, email_destino: str) -> EmailMessage:

    email = EmailMessage()

    email['Subject'] = 'Seu Relatório de Preços'
    anexar_arquivo('valores_celulares_importados.xlsx', email)
    mensagem = 'Baixe seu relatório de preços de celular agora!'

    email['From'] = EMAIL
    email['To'] = email_destino

    email.add_header('Content-Type', 'text/html')
    email.payload(mensagem.encode('utf-8'))

    return email



def enviar_email(email_destino: str):
    EMAIL, TOKEN = obter_token_email()
    email = email_setting(EMAIL, email_destino)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:
        mail.login(EMAIL, TOKEN)
        mail.send_message(email)

