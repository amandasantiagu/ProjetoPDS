from telas.abstractView import AbstractView

class TelaSistemaView(AbstractView):

    def __init__(self):
        #inicializa todos os controllers, e chama o método de cada um

    def menu_principal(self):
        print ("\n ---- Posto de Saúde ----")
        print ("1 - Cadastro do Paciente")
        print ("2 - Cadastro do Enfermeiro")
        print ("3 - Agendamentos")
        print ("5 - Gerar Relatorio Geral")
        print ("0 - Sair")
        opcao = self.le_inteiro("-->", range(5))
        return opcao
