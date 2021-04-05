
class TelaSistemaView():

    def menu_principal(self):
        print ("\n ---- Posto de Saúde Moreira & Santiago ----")
        print ("1 - Cadastro do Paciente")
        print ("2 - Cadastro do Enfermeiro")
        print ("3 - Agendamentos")
        print ("4 - Gerar Relatório Geral")
        print ("0 - Sair")
        try:
            opcao = int(input('Digite uma opção: '))
            return opcao
        except ValueError as e:
            print('Dado Invalido, digite novamente.{}'.format(e))
