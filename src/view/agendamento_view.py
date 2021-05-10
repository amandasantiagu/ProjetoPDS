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


    def relatorio(self, lista_agendamentos, lista_pacientes):
        num_agendamentos = 0
        datas = []
        pacientes_doseum = 0
        pacientes_dosedois = 0
        for ag in lista_agendamentos:
            datas.append(ag.data)
            num_agendamentos +=1

            if ag.paciente.dose_vacina == 1:
                pacientes_doseum += 1
            if ag.paciente.dose_vacina == 2:
                pacientes_dosedois += 1
        
        horarios = []
        for ag in lista_agendamentos:
            horarios.append(ag.horario)

        num_pacientes = 0

        for pac in lista_pacientes:
            num_pacientes += 1
        layout = [
                [sg.Output(size=(40,30), key="_listagem_")],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window('Relatorio de Vacinaçao').Layout(layout)
        button, values = window.Read(timeout=6)

        while button != 'Voltar' and button != None:
            window.FindElement("_listagem_").Update('')

            print("\n ---- RELATORIO GERAL ------:")
            print(" -> Data de Agendamentos Marcados: ")
            for data in datas:
                print(data)
            print("\nHorario de Agendamentos Marcados: " )
            for horario in horarios:
                print(horario)
            print("\nQuantidade de Agendamentos Marcados: " + str(num_agendamentos))
            print("\nPacientes com agendamento marcado: " + str(num_agendamentos) )
            print("\nPacientes aguardando agendamento: " + str(num_pacientes - num_agendamentos))
            print("\nQuantidade de Vacinas Aplicadas: " + str(num_agendamentos))
            print("\nQuantidade de Pacientes 1 dose Aplicada: " + str(pacientes_doseum))
            print("\nQuantidade de Pacientes 2 dose Aplicada: " + str(pacientes_dosedois))
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