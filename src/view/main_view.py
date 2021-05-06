import PySimpleGUI as sg
class TelaSistemaView:

    def __init__(self, posto):
        self.__posto = posto

    def menu_principal(self):
        layout =[
                [sg.Text("---- Posto de Saúde " + self.__posto.nome + "----")],
                [sg.Button('Cadastrar Paciente')],
                [sg.Button('Cadastro do Enfermeiro')],
                [sg.Button('Cadastro de Vacinas')],
                [sg.Button('Agendamentos')],
                [sg.Button('Gerar Relatório Geral')],
                [sg.Button('Alterar nome do Posto')],
                [sg.Button('Sair')],
                ]
        window = sg.Window('Tela de Sistema').Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]
