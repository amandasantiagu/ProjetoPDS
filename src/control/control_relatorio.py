
class RelatorioController:

    def __init__(self, c_paciente, c_agendamentos):
        self.__controller_paciente = c_paciente
        self.__controller_agendamentos = c_agendamentos


    def relatorio(self):
        pacientes_vacinados = self.pacientes_vacinados()
        pacientes_agendados = self.pacientes_agendados()
        pacientes_nao_agendados = self.pacientes_nao_agendados()
        print("Pacientes vacinados: ")
        for paciente in pacientes_vacinados:
            print("", paciente.nome_completo)
            print("----------------")

        for pac in pacientes_agendados:
            print("", pac.nome_completo)
            print("----------------")

        for p in pacientes_nao_agendados:
            print("", p.nome_completo)
            print("----------------")



    def pacientes_vacinados(self):
        todos_pacientes = self.__controller_paciente.pacientes
        pacientes_vacinados = []
        for paciente in todos_pacientes:
            if paciente.dose_vacina is not None:
                pacientes_vacinados.append(paciente)

        return pacientes_vacinados


    def pacientes_agendados(self):
        agendamentos = self.__controller_agendamentos.agendamentos
        pacientes = []
        for ag in agendamentos:
            if not ag.paciente in pacientes:
                pacientes.append(ag.paciente)

        return pacientes


    def pacientes_nao_agendados(self):
        todos_pacientes = self.__controller_paciente.pacientes
        agendamentos = self.__controller_agendamentos.agendamentos
        pacientes = []
        for agendamento in agendamentos:
            if agendamento.paciente in todos_pacientes:
                todos_pacientes.remove(agendamento.paciente)
        return todos_pacientes


