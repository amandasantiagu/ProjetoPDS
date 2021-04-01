import os

from abstractView import AbstractView

class PacienteView(AbstractView):

    def tela_paciente(self):
        print ("\n ---- Cadastro do Paciente ----")
        print ("1 - Incluir Paciente")
        print ("2 - Excluir Paciente")
        print ("3 -  Alterações no Cadastro")
        print ("4 - Listagem de Pacientes por CPF")
        print ("0 - Sair")
        opcao = self.le_inteiro('Digite uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def incluir(self):
        nome_completo = input("Nome Completo do Paciente: ")
        idade = input("Idade: ")
        try:
            cpf = int(input("Número do CPF: "))
            self.clear()
            return {'nome_completo': nome_completom 'idade':idade, 'cpf':cpf}
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
            return self.incluir()

    def excluir(self):
        try:
            cpf = int(input("Digite o CPF do paciente para deletar"))
            return cpf
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
            return self.excluir()

    
    def listar(self, listagem):
        self.clear()
        print("\n Lista de Pacientes:")
        for paciente in listagem:
            print("Nome: " + paciente.nome_completo)
            print("Idade: "+ str(paciente.idade))
            print("CPF: "+ str(paciente.cpf))
            print("--------------------------------\n")


    def atualizar(self):
        nome_completo = input("Nome Completo do Paciente: ")
        idade = input("Idade do Paciente: ")
        try:
            cpf = int(input("CPF do Paciente"))
            return {'nome_completo': nome_completom 'idade':idade, 'cpf':cpf}
        except ValueError as e:
            self.dado_invalido('CPF')
            return self.atualizar()


    def selecionar(self, pacientes):
        count = 1
        print("Selecione um paciente")
        for paciente in pacientes:
            print("Paciente nº: ", count)
            print("Nome: " + paciente.nome_completo)
            print("Idade: "+ str(paciente.idade))
            print("CPF: "+ str(paciente.cpf))
            print("--------------------------------\n")

        escolha = self.le_inteiro("-->", range(1, count))
        return escolha


    def cadastro_sucesso(self):
        print("Paciente cadastrado com sucesso!")

    def paciente_duplicado(self):
        print("Erro! Paciente já cadastrado.")

    def dado_invalido(self, dado_str):
        print("Erro! Dado inválido: ", dado_str)
