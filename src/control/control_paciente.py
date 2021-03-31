from model.paciente import Paciente
from view.telas.tela_paciente import PacienteView

## acho que precisaria receber o POSTO DE SAUDE (SISTEMA) / controller tbm?
class ControladorPaciente():
    def __init__(self):
        self.__pacientes = []
        self.__view = PacienteView()

## Utilizar um dicionario
    def option(self):
        opcao = self.__view.PacienteView()
        while opcao != "0":
            if opcao == "1":
                self.cadastra()
            elif opcao == "2":
                self.listagem()
            elif opcao == "3":
                self.atualiza()
            elif opcao == "4":
                self.remove()
            opcao = self.__view.PacienteView()

    ## Endereço add???
    def incluir_paciente(self, nome_completo, cpf, idade) -> Paciente:
        dados = self.__view.incluir()
        paciente = Paciente(nome_completo, cpf, idade)
        if tela is not None:
            for x in self.__pacientes:
                if x.cpf == cpf:
                    return
        if paciente.idade >= 0 and paciente.idade <= 150:
            self.__pacientes.append(paciente)
            self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem() 

    def atualiza(self):
        dados = self.__view.atualiza()
        for paciente in self.__view:
            if paciente.cpf == dados[2]:
                paciente.nome_completo = dados[0]
                paciente.idade = dados[1]

    def remove(self):
        cpf = self.__view.remove()
        for paciente in self.__view.pacientes:
            if paciente.cpf == cpf:
                self.__view.remove(paciente)
