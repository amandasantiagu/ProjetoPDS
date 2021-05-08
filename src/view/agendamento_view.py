import PySimpleGUI as sg
from .abstractView import AbstractView

class AgendamentoView(AbstractView):

    def tela_agendamento(self):
        layout = [
                    [sg.Button('Incluir Agendamento')],
                    [sg.Button('Listar Agendamentos')],
                    [sg.Button('Atualizar Agendamento')],
                    [sg.Button('Remover Agendamento')],
                    [sg.Button('Sair')],
                ]
        window = sg.Window('Cadastro de Agendamentos').Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]

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


    def relatorio(self):
        layout = [
                [sg.Output(size=(40,30), key="_listagem_")],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window('Listagem de Pacientes').Layout(layout)
        button, values = window.Read(timeout=6)

        while button != 'Voltar' and button != None:
            window.FindElement("_listagem_").Update('')

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
            button, values = window.Read()
        window.close()
