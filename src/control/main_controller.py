class MainController:

    def __init__(self):
        opcoes = {
                1: controller_paciente.inclui,
                2: controller_enfermeiro.inclui,
                3: controller_agendamentos.inclui,
                }
        escolha = self.__tela_sistema.menu_principal()
        opcoes[escolha]() #isso roda o método que o usuário escolher
