from ..model.vacina import Vacina
from .abstractDAO import AbstractDAO
from ..view.tela_vacina import VacinaView

class VacinaController():
    def __init__(self):
        self.__vacinaDAO = VacinaDAO()
        self.__view = VacinaView()

    def option(self):
        escolha = self.__view.tela_vacina()
        while escolha != 0:
            options = {
                    1: self.incluir,
                    2: self.excluir,
                    3: self.atualizar,
                    4: self.listagem,
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_vacina()

    def incluir(self) -> Vacina:
        dados = self.__view.incluir()
        tipo_vacina = dados['tipo_vacina']
        fabricante = dados['fabricante']
        num_id = dados['cpf']
        nova_vacina = Vacina(dados, tipo_vacina, num_id)
        for vacina in self.__vacina:
            if vacina.num_id == num_id:
               self.__view.vacina_duplicada()
                return
        self.__vacinaDAO.add(nova_vacina)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(list(self.__vacinaDAO.get_all()))

    def atualizar(self):
        self.listagem()
        dados = self.__view.atualizar()
        lista_vacinas = list(self.__vacinasDAO.get_all())
        for vacina in lista_vacinas:
            if vacina.num_id == dados['num_id']:
                vacina.tipo_vacina = dados['tipo_vacina']
                vacina.fabricante = dados['Fabricante']


    def excluir(self):
        self.listagem()
        num_id = self.__view.excluir()
        lista_vacinas = list(self.__vacinaDAO.get_all())
        for vacina in lista_vacinas:
            if vacina.num_id == num_id:
                self.__vacinaDAO.remove(vacina.id)
                self.__view.sucesso_excluir()

    @property
    def vacinas(self):
        return list(self.__vacinaDAO.get_all())
