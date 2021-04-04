
class TelaSistemaView():
    def __init__(self):
        pass

    def menu_principal(self):
        print ("\n ---- Posto de Saúde Moreira & Santiago ----")
        print ("1 - Cadastro do Paciente")
        print ("2 - Cadastro do Enfermeiro")
        print ("3 - Agendamentos")
        print ("4 - Gerar Relatório Geral")
        print ("0 - Sair")
        opcao = int(input('Digite uma opção: ')) ###Por try depois
        return opcao
