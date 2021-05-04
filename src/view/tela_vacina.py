from .abstractView import AbstractView

class VacinaView(AbstractView):
    def __init__(self):
        pass

    def tela_vacina(self):
        print ("\n ---- Cadastro de Vacina ----")
        print ("1 - Incluir Vacina")
        print ("2 - Excluir Vacina")
        print ("3 - Alterações no Cadastro")
        print ("4 - Listagem de Vacinas")
        print ("0 - Sair")
        opcao = self.le_inteiro('Digite uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def incluir(self):
        tipo_vacina = input("Tipo da Vacina: ")
        fabricante = input("Fabricante: ")
        try:
            quantidade = int(input("Quantidade: "))
            num_id = int(input("Numero do ID: "))
        except ValueError:
            self.dado_invalido('num_id')
            return self.incluir()
        else:
            return {"tipo_vacina":tipo_vacina,"fabricante":fabricante, 'quantidade':quantidade,'num_id':num_id }


    def excluir(self):
        try:
            num_id = int(input("Digite numero do ID para EXCLUIR: "))
            return num_id
        except ValueError:
            self.dado_invalido('ID')
            self.excluir()

    def atualizar(self):
        self.clear()
        print("\n Para atualizar o ID deve estar correto")
        tipo_vacina = input("Tipo da Vacina: ")
        fabricante = input("Fabricante: ")
        try:
            quantidade = int(input ("Quantidade: "))
            num_id = int(input("Número do ID: "))
        except ValueError:
            self.dado_invalido('ID')
            return self
        else:
            return {"tipo_vacina":tipo_vacina,"fabricante":fabricante, "quantidade": quantidade, "num_id": num_id}

    def listagem(self, listagem):
        print("\n Listagem de Vacinas:")
        for vacina in listagem:
            print("Tipo de Vacina: " + str(vacina.tipo_vacina))
            print("Fabricante: "+ str(vacina.fabricante))
            print("Quantidade: "+ str(vacina.quantidade))
            print("num_id: "+ str(vacina.num_id))
            print("--------------------------------\n")
    
    def cadastro_sucesso(self):
        print("------- Vacina cadastrada com sucesso! -------")

    def dado_invalido(self, dado_str):
        print("Erro! Dado inválido: ", dado_str)

    def vacina_duplicada(self):
        print("Erro! Vacina com ID já cadastrada.")

    def sucesso_atualizar(self):
        print("------- Atualizado com Sucesso. --------")

    def sucesso_excluir(self):
        print("------- Excluido com Sucesso -------.")

