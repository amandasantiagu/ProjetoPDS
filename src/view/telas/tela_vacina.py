import os

class VacinaView():
    def __init__(self):
        pass

    def tela_vacina(self):
        print ("\n ---- Cadastro de Vacina ----")
        print ("1 - Incluir Vacina")
        print ("2 - Excluir Vacina")
        print ("3 - Alterar Vacina")
        print ("4 - Listagem de Vacina por fabricante")
        print ("0 - Sair")
        opcao = int(input('Digite uma opção: '))
        return opcao

    def incluir(self):
        tipo_vacina = input("Tipo de Vacina:")
        fabricante = input("Fabricante da Vacina:")
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        try:
            quantidade = int(input("Digite a quantidade:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
        else:
            cls()
            return [tipo_vacina, fabricante, quantidade]

    
    def listagem(self, listagem):
        os.system('cls' if os.name == 'nt' else 'clear')
        c = 0
        print("\nLISTA DE VACINA:")
        for vacina in listagem:
            print("Tipo de Vacina: " + vacina.tipo_vacina)
            print("Fabricante: "+ vacina.fabricante)
            print("Quantidade: "+ vacina.quantidade)
            c += 1

    def atualiza(self):
        tipo_vacina = input("Tipo de Vacina:")
        fabricante = input("Fabricante da Vacina:")
        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
        else: 
            return [tipo_vacina, fabricante, quantidade]

    def excluir(self):

        tipo_vacina = input("Tipo de Vacina: ")
        fabricante = input("Fabricante da Vacina: ")
        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:    
            return [tipo_vacina, fabricante, quantidade]

    def cadastro_sucesso(self):
        print("Paciente Cadastrado com sucesso")
    
    def cadastro_erro(self):
        print("\n Verifique os valores.")