import PySimpleGUI as sg 

def obter_email() -> sg.Window:
    layout = [
        [sg.Text('Digite o e-mail para o qual o relatório deve ser enviado:')],
        [sg.Input(key='email', size=(39,1))],
        [sg.Text(key='invalid_email', text_color='black')],
        [
            sg.Button('Iniciar',size=(8,1), button_color='green'), 
            sg.Button('Cancelar', size=(8,1), button_color='red')
        ],
        [sg.Output(size=(37,7))]
    ]

    window = sg.Window('Extração de Dados:', layout=layout)
    return window

