from acesso_site import *
from interface import obter_email
import PySimpleGUI as sg 
from threading import Thread
from inicializar import GoogleChrome
from queue import Queue





""" 
def interagir_com_usuario() -> str:
    window = obter_email()
    while True:
        event, values = window.read()

        if event in(sg.WINDOW_CLOSED, 'Cancelar'):
            break

        elif event == 'Iniciar':

            email = values['email'].strip()
            window['email'].update('')

            if email.find('@') == -1 and email.find('.com') == -1:
                window['invalid_email'].\
                    update("Email inválido. Digite um e-mail válido")
            else:
                window['Iniciar'].update(disabled=True) 
            #print(f'O relatório será enviado para o e-mail: {usuario_email}\n') """

resultado_queue = Queue()

cria_nova_planilha_ = Thread(target=cria_nova_planilha, 
    args=(resultado_queue,), daemon=True)

acessa_site_ = Thread(target=acessa_site, 
    args=(resultado_queue,), daemon=True)

cria_nova_planilha_.start()
acessa_site_.start()

cria_nova_planilha_.join()
workbook, sheet = resultado_queue.get()

acessa_site_.join()
driver, wait = resultado_queue.get()





