import PySimpleGUI as sg

from .abstractView import AbstractView

class PacienteView(AbstractView):

    def tela_paciente(self):
        layout = [
                    [sg.Button('Cadastrar Paciente')],
                    [sg.Button('Listar Pacientes')],
                    [sg.Button('Atualizar Paciente')],
                    [sg.Button('Remover Paciente')],
                    [sg.Button('Sair')],
                ]
        window = sg.Window('Cadastro de Pacientes', size=(300,200)).Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]

    def incluir(self):
        layout = [
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Idade', size=(15, 1)), sg.InputText()],
                    [sg.Text('CPF', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Incluir Paciente').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':  
            values = self.set_keys_to_attrs(items, ['nome_completo', 'Idade', 'CPF'])
            window.close()
            return items
        else:
            window.close()
            return None

    def selecionar(self, pacientes, acao=None):
        if acao is None:
            acao = 'Selecionar'
        paciente_str = []
        for paciente in pacientes:
            paciente_str.append(paciente.nome_completo + ' -- ' + str(paciente.cpf))
        layout = [
                    [sg.Listbox(values=paciente_str, select_mode='extended', key='pac', size=(30, 6))],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window(acao + ' Paciente').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':
            window.close()
            return items['pac']
        else:
            window.close()
            return None
    
    def listagem(self, listagem):
        layout = [
                [sg.Output(size=(40,30), key="_listagem_")],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window('Listagem de Pacientes').Layout(layout)
        button, values = window.Read(timeout=6)

        while button != 'Voltar' and button != None:
            window.FindElement("_listagem_").Update('')
            for paciente in listagem:
                nome = "Nome: " + paciente.nome_completo
                idade = "Idade: "+ str(paciente.idade)
                cpf = "CPF: "+ str(paciente.cpf)
                lista = ["----", nome, idade, cpf]
             
                for values in lista:
                    print(values)
            button, values = window.Read()
        window.close()

    def get_pacient_att(self, lista_pacientes):
        paciente_str = []
        for paciente in lista_pacientes:
            paciente_str.append(paciente.nome_completo + '---' + str(paciente.idade) + '---' + str(paciente.cpf))
        layout = [
                    [sg.Listbox(values=paciente_str, select_mode='extended', key='pac', size=(30, 6))],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Escolha o Paciente').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':
            window.close()
            return items['pac']
        else:
            window.close()
            return None


    def atualizar(self):
        layout = [
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Idade', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Atualizar Paciente').Layout(layout)
        button_str, items = window.read()
        window.close()
        try:
            idade= int(items[1])
        except ValueError:
            self.dado_invalido()
        else:
            if 'Submit' in button_str:
                return items
            else:
                return None


    def cadastro_sucesso(self):
        sg.popup("------- Paciente cadastrado com sucesso! -------")

    def paciente_duplicado(self):
        sg.popup("Erro! Paciente já cadastrado.")

    def dado_invalido(self):
        sg.popup("Erro! Dado inválido")

    def sucesso_atualizar(self):
        sg.popup("------- Atualizado com Sucesso. --------")

    def sucesso_excluir(self):
        sg.popup("------- Excluido com Sucesso -------.")
