import os

from .abstractView import AbstractView

class PacienteView(AbstractView):
    def __init__(self):
        pass

    def tela_paciente(self):
        print ("\n ---- Cadastro do Paciente ----")
        print ("1 - Incluir Paciente")
        print ("2 - Excluir Paciente")
        print ("3 - Alterações no Cadastro")
        print ("4 - Listagem de Pacientes")
        print ("0 - Sair")
        opcao = self.le_inteiro('Digite uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def incluir(self):
        self.clear()
        nome_completo = input("Nome Completo do Paciente: ")
        idade = self.le_inteiro("Idade: ", range(1, 150))
        try:
            cpf = int(input("Número do CPF: "))
            return {'nome_completo': nome_completo, 'idade':idade, 'cpf':cpf}
        except ValueError:
            self.dado_invalido('CPF')
            return self.incluir()

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

    def cadastro_sucesso(self):
        print("------- Paciente cadastrado com sucesso! -------")

    def paciente_duplicado(self):
        print("Erro! Paciente já cadastrado.")

    def dado_invalido(self, dado_str):
        print("Erro! Dado inválido: ", dado_str)

    def sucesso_atualizar(self):
        print("------- Atualizado com Sucesso. --------")

    def sucesso_excluir(self):
        print("------- Excluido com Sucesso -------.")
