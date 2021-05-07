from ..model.vacina import Vacina
from ..model.persistence.vacinaDAO import VacinaDAO
from ..view.vacina_view import VacinaView


class VacinaController():
    def __init__(self):
        self.__vacinaDAO = VacinaDAO()
        self.__view = VacinaView()


    def option(self):
        escolha = self.__view.tela_vacina()
        while escolha != 'Sair' and escolha != None:
            options = {
                    'Incluir Vacina': self.incluir,
                    'Listar Vacinas': self.listagem,
                    'Atualizar Vacina': self.atualizar,
                    'Remover Vacina': self.excluir,
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_vacina()


    def incluir(self) -> Vacina:
        dados = self.__view.incluir()
        if dados != None:
            tipo_vacina = dados[0]
            fabricante = dados[1]
            try:
                quantidade = int(dados[2])
                num_id = int(dados[3])
            except TypeError:
                self.__view.dado_invalido()
            nova_vacina = Vacina(tipo_vacina, fabricante, quantidade, num_id)
            print(nova_vacina)
            lista_vacinas = list(self.__vacinaDAO.get_all())
            for vacina in lista_vacinas:
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
        lista_vacinas = list(self.__vacinaDAO.get_all())
        for vacina in lista_vacinas:
            if vacina.num_id == dados['num_id']:
                vacina.tipo_vacina = dados['tipo_vacina']
                vacina.fabricante = dados['Fabricante']
                vacina.quantidade = dados['quantidade']


    def excluir(self):
        self.listagem()
        num_id = self.__view.excluir()
        lista_vacinas = list(self.__vacinaDAO.get_all())
        for vacina in lista_vacinas:
            if vacina.num_id == num_id:
                self.__vacinaDAO.remove(vacina.num_id)
                self.__view.sucesso_excluir()

    @property
    def vacinas(self):
        return list(self.__vacinaDAO.get_all())


