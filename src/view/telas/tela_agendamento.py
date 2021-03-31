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
    print ("0 - Sair")
    opcao = int(input('Digite uma opção: '))
    return opcao

    def incluir(self):
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        data = input("Data Escolhida: ")
        horario = input("Horario Escolhida: ")
        cls()
        return [data, horario]

    def excluir(self):
        data = input("Data de Agendamento: ")
        horario = input("Horario de Agendamento:")
        return [data, horario]

    
    def listagem(self, listagem):
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        cls()
        c = 0
        print("\n Listagem de Agendamentos:")
        for agendamento in listagem:
            print("Data: " + agendamento.cpf)
            print("Horario: " + agendamento.cpf)
            print("paciente: " + agendamento.paciente.nome_completo)
            print("Enfermeiro: " + agendamento.enfermeiro.nome_completo)
            print("Vacina: " + agendamento.vacina)
            c = c + 1

    def atualiza(self):
        data = input("Data de Agendamento: ")
        horario = input("Horario de Agendamento: ")
        return [data, horario]

    def cadastro_sucesso(self):
        print("Agendamento Cadastrado com sucesso")
    
    def cadastro_erro(self):
        print("\n Verifique os valores.")