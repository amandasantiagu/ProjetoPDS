
class TelaSistemaView:

    def __init__(self, posto):
        self.__posto = posto

    def menu_principal(self):
        print("\n ---- Posto de Saúde " + self.__posto.nome + "----")
        print ("1 - Cadastro do Paciente")
        print ("2 - Cadastro do Enfermeiro")
        print ("3 - Cadastro de Vacinas")
        print ("4 - Agendamentos")
        print ("5 - Gerar Relatório Geral")
        print ("6 - Alterar nome do Posto")
        print ("0 - Sair")
        try:
            opcao = int(input('Digite uma opção: '))
            return opcao
        except ValueError as e:
            print('Dado Invalido, digite novamente.{}'.format(e))
