import os

class EnfermeiroView():
    def __init__(self):
        pass

    def tela_paciente(self):
        print ("\n ---- Cadastro do Enfermeiro ----")
        print ("1 - Incluir Enfermeiro")
        print ("2 - Excluir Enfermeiro")
        print ("3 - Alterações no Cadastro")
        print ("4 - Listagem de Enfermeiros por matricula")
        print ("0 - Sair")
        opcao = int(input('Digite uma opção: '))
        return opcao

    def incluir(self):
        nome = input("Nome do Enfermeiro:")
        sobrenome = input("Sobrenome:")
        idade = int(input("Idade:"))
        cpf = str(input("Digite o CPF:"))
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        try:
            matricula_coren = int(input("Numero de matricula coren:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:
            cls()
            return [nome, sobrenome, idade, cpf, matricula_coren]

    def excluir(self):
        try:
            matricula_coren = int(input("ID do vendedor:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:    
            return matricula_coren

    
    def listagem(self, listagem):
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        cls()
        c = 0
        print("\n Lista de Enfermeiros:")
        for enfermeiro in listagem:
            print("Nome: " + enfermeiro.nome)
            print("Sobrenome: "+ enfermeiro.sobrenome)
            print("Idade: "+ str(enfermeiro.idade))
            print("CPF: "+ enfermeiro.cpf)
            print("Matricula/COREN: " + enfermeiro.matricula_coren)
            c = c + 1

    def atualiza(self):
        nome = input("Nome do Enfermeiro:")
        sobrenome = input("Sobrenome:")
        idade = int(input("Idade:"))
        cpf = input("Digite o cpf:")
        try:
           matricula_coren = int(input("Digite a MATRICULA/COREN:"))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else: 
            return [nome, sobrenome, idade, cpf, matricula_coren]

    def cadastro_sucesso(self):
        print("Enfermeiro Cadastrado com sucesso")
    
    def cadastro_erro(self):
        print("\n Verifique os valores.")