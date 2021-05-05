import PySimpleGUI as sg

from .abstractView import AbstractView

class PacienteView(AbstractView):

    def tela_paciente(self):
        layout = [
                    [sg.Button('Cadastrar Paciente')],
                    [sg.Button('Listar Pacientes')],
                    [sg.Button('Atualizar Paciente')],
                    [sg.Button('Remover Paciente')],
                ]
        window = sg.Window('Pacientes').Layout(layout)
        button_str = window.read()
        return button_str

    def incluir(self):
        layout = [
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Idade', size=(15, 1)), sg.InputText()],
                    [sg.Text('CPF', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Incluir Paciente').Layout(layout)
        button_str, items = window.read()
        values = self.set_keys_to_attrs(items, ['nome_completo', 'idade', 'cpf'])
        return values

    def excluir(self):
        try:
            cpf = int(input("Digite o CPF do paciente para EXCLUIR: "))
            return cpf
        except ValueError:
            self.dado_invalido('CPF')
        else:    
            return cpf
    
    def listagem(self, listagem):
        print("\n Listagem de Pacientes:")
        for paciente in listagem:
            print("Nome: " + paciente.nome_completo)
            print("Idade: "+ str(paciente.idade))
            print("CPF: "+ str(paciente.cpf))
            print("--------------------------------\n")

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
