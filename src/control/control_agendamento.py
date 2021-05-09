from ..model.paciente import Paciente
from ..model.agendamento import Agendamento
from ..model.enfermeiro import Enfermeiro
from ..model.vacina import Vacina
from ..model.persistence.agendamentoDAO import AgendamentoDAO
from ..view.agendamento_view import AgendamentoView
from ..view.vacina_view import VacinaView
from ..view.paciente_view import PacienteView
from ..view.enfermeiro_view import EnfermeiroView


class AgendamentoController():
    def __init__(self, pac_controller, enf_controller, vac_controller):
        self.__dao = AgendamentoDAO()
        self.__agendamento_view = AgendamentoView()
        self.__vacina_view = VacinaView()
        self.__paciente_view = PacienteView()
        self.__enfermeiro_view = EnfermeiroView()
        self.__enfermeiro_controller = enf_controller
        self.__paciente_controller = pac_controller
        self.__vacina_controller = vac_controller

    def option(self):
        escolha = self.__agendamento_view.tela_agendamento()
        while escolha != 'Sair' and escolha != None:
            options = {
                    'Incluir Agendamento': self.incluir,
                    'Listar Agendamentos':self.listagem,
                    #'Atualizar Agendamento': self.atualizar,
                    'Remover Agendamento':  self.excluir
                    }
            function = options[escolha]
            function()
            escolha = self.__agendamento_view.tela_agendamento()

    def incluir(self) -> Agendamento:
        dados = self.__agendamento_view.incluir()
        if dados != None:
            data = dados[0]
            horario = dados[1]
            try:
                num_id = int(dados[2])
            except ValueError:
                self.__agendamento_view.error("ID Inválido")
                return
        else:
            return

        #verifica duplicidade de data/horário
        lista_agendamentos = list(self.__dao.get_all())
        for ag in lista_agendamentos:
            if ag.data == data and ag.horario == horario:
                self.__agendamento_view.agendamento_duplicado()
                return

        #recebe a str do listbox com o paciente escolhido
        paciente = self.__paciente_view.get_paciente_att(self.__paciente_controller.pacientes)
        if paciente == []:
            self.__agendamento_view.error("Nenhum paciente selecionado")
            return
        #recebe o objeto Paciente associado ao cpf
        paciente = self.array_to_obj(paciente, self.__paciente_controller.pacientes)

        #recebe a str do listbox com o enfermeiro escolhido
        enfermeiro = self.__enfermeiro_view.get_enfermeiro_att(self.__enfermeiro_controller.enfermeiros)
        if enfermeiro == []:
            self.__agendamento_view.error("Nenhum enfermeiro selecionado")
            return
        #recebe o objeto Enfermeiro associado à matrícula coren
        enfermeiro = self.array_to_obj(enfermeiro, self.__enfermeiro_controller.enfermeiros)

        #recebe a str do listbox com a vacina escolhida
        vacina = self.__vacina_view.get_vacina_att(self.__vacina_controller.lista_vacinas)
        if vacina == []:
            self.__agendamento_view.error("Nenhuma vacina selecionada")
            return
        #recebe o objeto Vacina associado à matrícula coren
        vacina = self.array_to_obj(vacina, self.__vacina_controller.lista_vacinas)

        #Define qual a dose da vacina que vai ser aplicada
        if paciente.dose_vacina == 0:
            paciente.dose_vacina += 1
        elif paciente.dose_vacina == 1:
            paciente.dose_vacina += 1


        #caso todos os objetos existam -> cria o agendamento e adiciona no DAO
        if paciente != None and enfermeiro != None and vacina != None:
            agendamento = Agendamento(num_id, data, horario, vacina, paciente.dose_vacina , enfermeiro, paciente)
            self.__dao.add(agendamento)
            self.__agendamento_view.cadastro_sucesso()
        else:
            return

    def listagem(self):
        self.__agendamento_view.listagem(self.__dao.get_all())

    def get_agendamento_att(self):
        lista_agendamentos = list(self.__dao.get_all())
        return self.__agendamento_view.get_agendamento_att(lista_agendamentos)

    def excluir(self):
        lista_agendamentos = list(self.__dao.get_all())
        dados = self.get_agendamento_att()
        agendamento = self.array_to_obj(dados, lista_agendamentos)

        if agendamento != None:
                self.__dao.remove(agendamento.num_id)
                self.__agendamento_view.agendamento_removido()
                return
        self.__agendamento_view.error("Nenhum agendamento selecionado!")

    ########### EM DUVIDA DE COMO ACESSAR MEU PACIENTE/ENFERMEIRO P EDITAR
    def atualizar(self, agendamento):
        #agendamento_escolhido = self.get_pacient_att()
        #dados = self.__agendamento_view.atualizar(agendamento)
        #self.__dao.update(agendamento, agendamento.id)
        pass

    @property
    def agendamentos(self):
        return self.__dao.get_all()

    #pega a string do get_att - que é listbox - e retorna o objeto relacionado ao ID (ou data/hora pra agendamento)
    def array_to_obj(self, escolhido_lista_str, lista_obj):
        for obj in lista_obj:
            if isinstance(obj, Agendamento):
                try:
                    for item in escolhido_lista_str:
                        if obj.data in item and obj.horario:
                            return obj
                except TypeError:
                    return

            elif isinstance(obj, Paciente):
                num_id = obj.cpf
            elif isinstance(obj, Enfermeiro):
                num_id = obj.matricula_coren
            elif isinstance(obj, Vacina):
                num_id = obj.num_registro

            try:
                for item in escolhido_lista_str:
                    if str(num_id) in item:
                        return obj
            except TypeError:
                return

