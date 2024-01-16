import PySimpleGUI as sg 

def obter_email() -> sg.Window:
    layout = [
        [sg.Text('Digite seu e-mail:')],
        [sg.Input(key='email', size=(33,1))],
        [sg.Text(key='invalid_email', text_color='red')],
        [
        sg.Button('Iniciar',size=(8,1), button_color='green'), 
        sg.Button('Cancelar', size=(8,1), button_color='red')],
        [sg.Output(size=(31,7))]
    ]

    window = sg.Window('Extração de Dados:', layout=layout)
    return window.read()

