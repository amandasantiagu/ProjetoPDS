import os

class VacinaView():

    def tela_vacina(self):
        print ("\n ---- Cadastro de Vacina ----")
        print ("1 - Incluir Vacina")
        print ("2 - Excluir Vacina")
        print ("3 - Alterar Vacina")
        print ("4 - Listagem de Vacina por fabricante")
        print ("0 - Sair")
        opcao = self.le_inteiro('Digite uma opção: ')
        return opcao

    def incluir(self):
        tipo_vacina = input("Tipo de Vacina: ")
        fabricante = input("Fabricante da Vacina: ")
        try:
            quantidade = self.le_inteiro("Digite a quantidade: ")
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
        else:
            self.clear()
            return [tipo_vacina, fabricante, quantidade]

    
    def listagem(self, listagem):
        self.clear()
        print("\nLISTA DE VACINA:")
        for vacina in listagem:
            print("Tipo de Vacina: " + vacina.tipo_vacina)
            print("Fabricante: "+ vacina.fabricante)
            print("Quantidade: "+ vacina.quantidade)

    def atualiza(self):
        tipo_vacina = input("Tipo de Vacina:")
        fabricante = input("Fabricante da Vacina:")
        try:
            quantidade = self.le_inteiro("Digite a quantidade: ")
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
        else: 
            return [tipo_vacina, fabricante, quantidade]

    def excluir(self):

        tipo_vacina = input("Tipo de Vacina: ")
        fabricante = input("Fabricante da Vacina: ")
        try:
            quantidade = self.le_inteiro("Digite a quantidade: ")
        except ValueError as e:
            print('\nERRO: Digite um valor valido: {}'.format(e))
        else:    
            return [tipo_vacina, fabricante, quantidade]

    def cadastro_sucesso(self):
        print("Vacina Cadastrada com sucesso")
    
    def cadastro_erro(self):
        print("\n Verifique os valores.")
