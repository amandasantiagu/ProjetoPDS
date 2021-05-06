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
        window = sg.Window('Pacientes').Layout(layout)
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
            values = self.set_keys_to_attrs(items, {0: 'nome_completo', 1: 'idade', 2: 'cpf'})
            print(values)
            window.close()
            return values
        else:
            window.close()
            return None

    def excluir(self):
        layout = [
                    [sg.Text('CPF', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Excluir Paciente').Layout(layout)
        button_str, items = window.read()
        try:
            cpf = int(items[0])
        except ValueError:
            self.dado_invalido('CPF')
            window.close()
            return None
        else:
            window.close()    
            return cpf
    
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

    def atualizar(self):
        self.clear()
        print("\n Para atualizar o CPF deve estar correto")
        nome_completo = input("Nome Completo do Paciente: ")
        idade = self.le_inteiro("Idade: ", range(1, 150))
        try:
            cpf = int(input("CPF do Paciente: "))
            return {'nome_completo': nome_completo, 'idade':idade, 'cpf':cpf}
        except ValueError:
            self.dado_invalido('CPF')
            return self

    # ONDE VAMOS USAR?
    # def selecionar(self, pacientes):
    #     count = 1
    #     print("Selecione um paciente")
    #     for paciente in pacientes:
    #         print("Paciente nº: ", count)
    #         print("Nome: " + paciente.nome_completo)
    #         print("Idade: "+ str(paciente.idade))
    #         print("CPF: "+ str(paciente.cpf))
    #         print("--------------------------------\n")
    #         count += 1

    #     escolha = self.le_inteiro("-->", opcoes = range(1, count))
    #     return pacientes[escolha - 1]

    def cadastro_sucesso(self):
        sg.popup("------- Paciente cadastrado com sucesso! -------")

    def paciente_duplicado(self):
        sg.popup("Erro! Paciente já cadastrado.")

    def dado_invalido(self, dado_str):
        sg.popup("Erro! Dado inválido: ", dado_str)

    def sucesso_atualizar(self):
        sg.popup("------- Atualizado com Sucesso. --------")

    def sucesso_excluir(self):
        sg.popup("------- Excluido com Sucesso -------.")