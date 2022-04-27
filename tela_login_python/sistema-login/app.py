import PySimpleGUI as sg 

# Criação do layout
layout = [
     [sg.Text('USER: ')],
     [sg.Input(key='usuario')],
     [sg.Text('PASSWORD: ')],
     [sg.Input(key='senha')],
     [sg.Button('login')],
     [sg.Text('', key='mensagem')],
 ]

# Código criação da janela de login 
window = sg.Window('Login', layout=layout)

# Processamento da lógica do programa
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '123456'
        usuario_correto = 'user_test'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Usuário ou senha incorreto.')


        