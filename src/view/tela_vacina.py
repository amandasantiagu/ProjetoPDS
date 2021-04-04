from view.abstractView import AbstractView

class VacinaView(AbstractView):
    def __init__(self):
        pass

    def incluir(self):
        tipo_vacina = input("Tipo da Vacina: ")
        fabricante = input("Fabricante: ")
        try:
            dose = int(input("Número da dose: "))
            return {"tipo_vacina":tipo_vacina,"fabricante":fabricante, "dose": dose}
        except ValueError:
            print("Valor inválido.")
            self.clear()
            return self.incluir()

    ################ abstract pede para ter isso para ser importado no agendamento
    def excluir(self):
        pass

    def atualizar(self):
        pass

    def listagem(self):
        pass
