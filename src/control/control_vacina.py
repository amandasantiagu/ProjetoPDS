from view.telas.tela_vacina import VacinaView

class VacinaController():
    def __init__(self):
        self.__view = VacinaView()

    def run(self):
        opcao = self.__view.tela_principal()
        while opcao != "0":
            if opcao == "1":
                self.cadastra()
            elif opcao == "2":
                self.lista()
            elif opcao == "3":
                self.atualiza()
            elif opcao == "4":
                self.remove()
            opcao = self.__view.tela_principal()
