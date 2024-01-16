from acesso_site import *
from interface import obter_email
import PySimpleGUI as sg 
from threading import Thread
from queue import Queue



resultado_queue = Queue()

cria_nova_planilha_ = Thread(target=cria_nova_planilha, 
    args=(resultado_queue,), daemon=True)

cria_nova_planilha_.start()

driver, wait = acessa_site()

cria_nova_planilha_.join()
workbook, sheet = resultado_queue.get()

window = obter_email()
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    elif event == 'Iniciar':
        email = values['email'].strip()
        window['email'].update('')

        if email.find('@') == -1 and email.find('.com') == -1:
            window['invalid_email'].\
                update("Email inválido. Digite um e-mail válido")
        else:
            window['Iniciar'].update(disabled=True) 
            print(f'O relatório será enviado para o e-mail: {email}\n')
            extrai_dados_ = Thread(target=extrai_dados, 
                args=(driver, wait, email, sheet, workbook, window), daemon=True)
            extrai_dados_.start()
    elif event == 'programa_finalizado':
        sg.popup('Programa finalizado.')
        window.close()
        break
            




