import PySimpleGUI as sg
from .abstractView import AbstractView

class EnfermeiroView(AbstractView):

    def __init__(self):
        pass

    def tela_enfermeiro(self):
        layout = [
                    [sg.Button('Cadastrar Enfermeiro')],
                    [sg.Button('Listar Enfermeiro')],
                    [sg.Button('Atualizar Enfermeiro')],
                    [sg.Button('Remover Enfermeiro')],
                    [sg.Button('Sair')],
                ]
        window = sg.Window('Enfermeiros').Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]

    def incluir(self):
        layout = [
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Idade', size=(15, 1)), sg.InputText()],
                    [sg.Text('Matricula COREN', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Cadastrar Enfermeiro').Layout(layout)
        button_str, items = window.read()
        print(type(items))
        values = self.set_keys_to_attrs(items, {0: 'nome_completo', 1: 'idade', 2: 'matricula_coren'})
        return values

    def excluir(self):
        self.clear()
        try:
            matricula_coren = int(input("Digite a matricula/COREN: "))
        except ValueError:
            self.dado_invalido('matricula_coren')
        else:    
            return matricula_coren
    
    def listagem(self, listagem):
        self.clear()
        print("\n Listagem de Enfermeiros:")
        for enfermeiro in listagem:
            print("Nome: " + enfermeiro.nome_completo)
            print("Idade: "+ str(enfermeiro.idade))
            print("Matricula/COREN: " + str(enfermeiro.matricula_coren))
            print("------------------")

    def atualizar(self):
        self.clear()
        print("\n Para atualizar a Matricula deve estar correta")
        nome_completo = input("Nome do Enfermeiro: ")
        idade = self.le_inteiro("Idade: ", range(1, 150))
        try:
           matricula_coren = int(input("Digite a MATRICULA/COREN para EXCLUIR: "))
           return {'nome_completo': nome_completo, 'idade':idade, 'matricula_coren': matricula_coren}
        except ValueError:
            self.dado_invalido('matricula_coren')
            return


    def selecionar(self, enfermeiros):
        count = 1
        print("Selecione um enfermeiro")
        for enfermeiro in enfermeiros:
            print("Enfermeiro nº: ", count)
            print("Nome: " + enfermeiro.nome_completo)
            print("Idade: "+ str(enfermeiro.idade))
            print("Matricula: "+ str(enfermeiro.matricula_coren))
            print("--------------------------------\n")
            count += 1

        escolha = self.le_inteiro("-->", opcoes = range(1, count))
        return enfermeiros[escolha - 1]

    def cadastro_sucesso(self):
        print("------- Enfermeiro cadastrado com sucesso! -------")

    def enfermeiro_duplicado(self):
        print("Erro! Enfermeiro já cadastrado.")

    def dado_invalido(self, dado_str):
        print("Erro! Dado inválido: ", dado_str)

    def sucesso_atualizar(self):
        print("------- Atualizado com Sucesso. -------")
    
    def sucesso_excluir(self):
        print("------- Excluido com Sucesso. -------")
