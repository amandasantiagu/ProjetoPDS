import os

class PacientView():
    def __init__(self):
        pass

    def tela_paciente(self):
        print ("\n ---- Cadastro do Paciente ----")
        print ("1 - Incluir Paciente")
        print ("2 - Excluir Paciente")
        print ("3 -  Alterações no Cadastro")
        print ("4 - Listagem de Pacientes por CPF")
        print ("0 - Sair")
        opcao = int(input('Digite uma opção: '))
        return opcao

    def incluir(self):
        nome = input("Nome do Paciente:")
        sobrenome = input("Sobrenome do Paciente:")
        idade = int(input("Idade:"))
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        try:
            cpf = int(input("Numero do CPF:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:
            cls()
            return [nome, sobrenome, idade, cpf]

    def excluir(self):
        try:
            cpf = int(input("Digite o CPF do Paciente:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:    
            return cpf

    
    def listagem(self, listagem):
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        cls()
        c = 0
        print("\n Lista de Pacientes:")
        for paciente in listagem:
            print("Nome: " + paciente.nome)
            print("Sobrenome: "+ paciente.sobrenome)
            print("Idade: "+ str(paciente.idade))
            print("CPF: "+ str(paciente.cpf))
            c = c + 1

    def atualizar(self):
        nome = input("Nome do Paciente:")
        sobrenome = input("Sobrenome do Paciente:")
        idade = int(input("CPF do Paciente:"))
        try:
           cpf = int(input("Digite o cpf:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else: 
            return [nome, sobrenome, idade, cpf]

    def cadastro_sucesso(self):
        print("Paciente Cadastrado com sucesso")
    
    def cadastro_erro(self):
        print("\n Verifique os valores.")