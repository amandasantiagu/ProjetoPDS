from .abstractView import AbstractView

class AgendamentoView(AbstractView):

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
        return {"data":data, "horario":horario}

    def excluir(self):
        data = input("Data de Agendamento: ")
        horario = input("Horario de Agendamento:")
        self.clear()
        return {"data":data, "horario":horario}

# TODO atualizar pra utilizar a gui
    def atualizar(self, agendamento):
        # pegar dados de enf, paciente e os caraio a partir do agendamento obj
        data = input("Data de Agendamento: ")
        horario = input("Horario de Agendamento: ")
        return {"data":data, "horario":horario}

    def listagem(self, listagem):
        self.clear()
        print("\n Listagem de Agendamentos:")
        for agendamento in listagem:
            print(agendamento.paciente)
            print("Data: " + agendamento.data)
            print("Horario: " + agendamento.horario)
            print("Paciente: " + agendamento.paciente.nome_completo)
            print("Enfermeiro: " + agendamento.enfermeiro.nome_completo)
            print("Vacina: " + agendamento.vacina)

    def cadastro_sucesso(self):
        print("Agendamento cadastrado com sucesso!")

    def agendamento_duplicado(self):
        print("Erro! Agendamento já cadastrado.")

    def relatorio(self, agendamentos):
        self.clear()
        print("\n ---- RELATORIO GERAL ------:")
        print("Data de Agendamentos Marcados: ")
        print("Horario de Agendamentos Marcados: " )
        print("Quantidade de Agendamentos Marcados: ")
        print("Pacientes Agendados: ")
        print("Quantidade de Pacientes atendidos: ")
        print("Quantidade de Pacientes com agendamento marcados: ")
        print("Quantidade de Vacinas Aplicadas: ")
        print("Quantidade de Pacientes 1 dose Aplicada: ")
        print("Quantidade de Pacientes 2 dose Aplicada: ")

