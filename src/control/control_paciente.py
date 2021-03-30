from model.paciente import Paciente

class ControladorPaciente(Paciente):
    def __init__(self):
        self.__pacientes = []

    def inclui_paciente(self, nome_completo: str, cpf: int, idade: int) -> Paciente:
        paciente = Paciente(nome_completo, cpf, idade)
        for x in self.__pacientes:
            if x.cpf == cpf:
                return

        self.__pacientes.append(paciente)
        return paciente
