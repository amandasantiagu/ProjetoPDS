import os

from abstractView import AbstractView

class AgendamentoView(AbstractView):
    def __init__(self):
        pass

    def tela_agendamento(self):
        print ("\n ---- Cadastro de Agendamentos ----")
        print ("1 - Incluir Agendamento")
        print ("2 - Excluir Agendamento")
        print ("3 - Alterar Agendamento")
        print ("4 - Listagem de Agendamento por Paciente")
        print ("0 - Sair")
        opcao = self.le_inteiro('Digite uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def incluir(self):
        data = input("Data Escolhida: ")
        horario = input("Horario Escolhida: ")
        self.clear()
        return [data, horario]

    def excluir(self):
        data = input("Data de Agendamento: ")
        horario = input("Horario de Agendamento:")
        return [data, horario]

    
    def listar(self, listagem):
        self.clear()
        print("\n Listagem de Agendamentos:")
        for agendamento in listagem:
            print("Data: " + agendamento.data)
            print("Horario: " + agendamento.horario)
            print("paciente: " + agendamento.paciente.nome_completo)
            print("Enfermeiro: " + agendamento.enfermeiro.nome_completo)
            print("Vacina: " + agendamento.vacina)

    def atualiza(self):
        data = input("Data de Agendamento: ")
        horario = input("Horario de Agendamento: ")
        return [data, horario]

