import os

class AgendamentoView():
    def __init__(self):
        pass

def tela_agendamento(self):
    print ("\n ---- Cadastro de Agendamentos ----")
    print ("1 - Incluir Agendamento")
    print ("2 - Excluir Agendamento")
    print ("3 - Alterar Agendamento")
    print ("4 - Listagem de Agendamento por Paciente")
    print ("5 - Listagem de Agendamento por Enfermeiro")
    print ("0 - Sair")
    opcao = int(input('Digite uma opção: '))
    return opcao
