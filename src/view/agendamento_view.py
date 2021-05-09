import PySimpleGUI as sg
from .abstractView import AbstractView

class AgendamentoView(AbstractView):

    def tela_agendamento(self):
        layout = [
                    [sg.Button('Incluir Agendamento')],
                    [sg.Button('Listar Agendamentos')],
                    [sg.Button('Remover Agendamento')],
                    [sg.Button('Sair')],
                ]
        window = sg.Window('Cadastro de Agendamentos', size=(370,200)).Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]

    def incluir(self):
        layout = [
                    [sg.Text('Data', size=(15, 1)), sg.InputText()],
                    [sg.Text('Horario', size=(15, 1)), sg.InputText()],
                    [sg.Text('ID', size=(15,1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Incluir Agendamento').Layout(layout)
        button_str, items = window.read()
        try:
            items[2] = int(items[2])
        except ValueError:
            self.error("Dado Inválido")
        if button_str == 'Submit':
            window.close()
            return items
        else:
            window.close()
            return None

   
    def get_agendamento_att(self, agendamentos):
        agendamento_str = []
        for agendamento in agendamentos:
            agendamento_str.append(agendamento.data + ' -- ' + str(agendamento.horario))
        layout = [
                    [sg.Listbox(values=agendamento_str, select_mode='extended', key='agen', size=(30, 6))],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Excluir Agendamento').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':
            window.close()
            return items['agen']
        else:
            window.close()
            return None

    # def atualizar(self, agendamento):
    #     # pegar dados de enf, paciente e os caraio a partir do agendamento obj
    #     data = input("Data de Agendamento: ")
    #     horario = input("Horario de Agendamento: ")
    #     return {"data":data, "horario":horario}

    def listagem(self, listagem):
        layout = [
                [sg.Output(size=(40,30), key="_listagem_")],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window('Listagem de Agendamentos').Layout(layout)
        button, values = window.Read(timeout=6)

        while button != 'Voltar' and button != None:
            window.FindElement("_listagem_").Update('')
            lista = []
            
            for agendamento in listagem:
                try:
                    num_id = "ID: " + str(agendamento.num_id)
                    data = "Data: " + str(agendamento.data)
                    horario = "Horario: "+  str(agendamento.horario)
                    paciente = "Paciente: " + str(agendamento.paciente.nome_completo)
                    enfermeiro = "Enfermeiro: " + str(agendamento.enfermeiro.nome_completo)
                    vacina = "Vacina: " + str(agendamento.vacina.tipo_vacina) + "--" + str(agendamento.vacina.fabricante)
                    dose_vacina = "Dose: " + str(agendamento.dose_vacina)
                    lista.extend(["----", num_id, data, horario, paciente, enfermeiro, vacina, dose_vacina])
                
                    for values in lista:
                        print(values)
                except Exception as e:
                    sg.popup("ERRO: {}".format(e))
            
            button, values = window.Read()
        window.close()


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

    def cadastro_sucesso(self):
        sg.popup("Agendamento cadastrado com sucesso.")
    def agendamento_duplicado(self):
        sg.popup("Agendamento Duplicado")
    def agendamento_removido(self):
        sg.popup("Agendamento removido com sucesso!")
    def error(self, error_msg):
        sg.popup("ERRO: " + error_msg)