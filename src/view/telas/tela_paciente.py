import os

from abstractTela import AbstractTela

class PacienteView(AbstractTela):

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
        idade = self.le_inteiro("Idade:"))
        try:
            cpf = self.le_inteiro("Numero do CPF:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:
            self.clear()
            return [nome_completo, idade, cpf]

    def excluir(self):
        try:
            cpf = self.le_inteiro("Digite o CPF do Paciente:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:    
            return cpf

    
    def listar(self, listagem):
        self.clear()
        print("\n Lista de Pacientes:")
        for paciente in listagem:
            print("Nome: " + paciente.nome_completo)
            print("Idade: "+ str(paciente.idade))
            print("CPF: "+ str(paciente.cpf))

    def atualizar(self):
        nome_completo = input("Nome Completo do Paciente: ")
        idade = self.le_inteiro("CPF do Paciente:"))
        try:
           cpf = self.le_inteiro("Digite o cpf:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else: 
            return [nome_completo, idade, cpf]
