from abstractView import AbstractView

class VacinaView(AbstractView):

    def incluir_ou_atualizar(self):
        tipo_vacina = input("Tipo da Vacina: ")
        fabricante = input("Fabricante: ")
        try:
            dose = int(input("Número da dose: "))
            return {"tipo_vacina":tipo_vacina,"fabricante":fabricante, "dose": dose}
        except ValueError:
            print("Valor inválido.")
            self.clear()
            self.incluir_ou_atualizar()
