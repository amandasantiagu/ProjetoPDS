import PySimpleGUI as sg
from .abstractView import AbstractView

class EnfermeiroView(AbstractView):

    def __init__(self):
        pass

    def tela_enfermeiro(self):
        layout = [
                    [sg.Button('Cadastrar Enfermeiro')],
                    [sg.Button('Listar Enfermeiros')],
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
                    [sg.Text('Matricula/COREN', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Cadastrar Enfermeiro').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':  
            values = self.set_keys_to_attrs(items, {0: 'nome_completo', 1: 'idade', 2: 'matricula_coren'})
            print(values)
            window.close()
            return values
        else:
            window.close()
            return None

    def excluir(self):
        layout = [
                    [sg.Text('Matricula', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Excluir Enfermeiro').Layout(layout)
        button_str, items = window.read()
        try:
           matricula_coren = int(items[0])
        except ValueError:
            self.dado_invalido('Matricula')
            window.close()
            return None
        else:
            window.close()    
            return matricula_coren
    
    def listagem(self, listagem):
        layout = [
                [sg.Output(size=(40,30), key="_listagem_")],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window('Listagem de Enfermeiros').Layout(layout)
        button, values = window.Read(timeout=6)

        while button != 'Voltar' and button != None:
            window.FindElement("_listagem_").Update('')
            for  enfermeiro in listagem:
                nome = "Nome: " + enfermeiro.nome_completo
                idade = "Idade: "+  str(enfermeiro.idade)
                matricula_coren = "Matricula/COREN: " + str(enfermeiro.matricula_coren)
                lista = ["----", nome, idade, matricula_coren]
             
                for values in lista:
                    print(values)
            button, values = window.Read()
        window.close()

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


    # def selecionar(self, enfermeiros):
    #     count = 1
    #     print("Selecione um enfermeiro")
    #     for enfermeiro in enfermeiros:
    #         print("Enfermeiro nº: ", count)
    #         print("Nome: " + enfermeiro.nome_completo)
    #         print("Idade: "+ str(enfermeiro.idade))
    #         print("Matricula: "+ str(enfermeiro.matricula_coren))
    #         print("--------------------------------\n")
    #         count += 1

    #     escolha = self.le_inteiro("-->", opcoes = range(1, count))
    #     return enfermeiros[escolha - 1]

    def cadastro_sucesso(self):
        sg.popup("------- Enfermeiro cadastrado com sucesso! -------")

    def enfermeiro_duplicado(self):
        sg.popup("Erro! Enfermeiro já cadastrado.")

    def dado_invalido(self, dado_str):
        sg.popup("Erro! Dado inválido: ", dado_str)

    def sucesso_atualizar(self):
        sg.popup("------- Atualizado com Sucesso. --------")

    def sucesso_excluir(self):
        sg.popup("------- Excluido com Sucesso -------.")