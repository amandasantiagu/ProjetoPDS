import PySimpleGUI as sg
class TelaSistemaView:

    def __init__(self, posto):
        self.__posto = posto

    def menu_principal(self):
        layout =[
                [sg.Text("---- Posto de Saúde " + self.__posto.nome + "----")],
                [sg.Button('Paciente')],
                [sg.Button('Enfermeiro')],
                [sg.Button('Vacinas')],
                [sg.Button('Agendamentos')],
                [sg.Button('Relatório Geral - Não Implementado')],
                [sg.Button('Alterar Nome do Posto')],
                [sg.Button('Sair')],
                ]
        window = sg.Window('Tela de Sistema', size=(300,300)).Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]
