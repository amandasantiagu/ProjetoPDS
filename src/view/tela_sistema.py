import os

class telaSistemaView():
    def __init__(self):
        pass

def menu_principal(self):
    print ("\n ---- Posto (nome Posto) ----")
    print ("1 - Cadastro do Cliente")
    print ("2 - Cadastro do Enfermeiro")
    print ("3 - Cadastro de Agendamento")
    print ("4 - Cadastro de Vacinas")
    print ("5 - Gerar Relatorio Geral")
    print ("0 - Sair")
    opcao = int(input('Digite uma opção: '))
    return opcao
