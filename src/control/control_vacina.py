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
        data = self.__view.incluir()
        if data != None:
            tipo_vacina = data['tipo_vacina']
            fabricante = data['fabricante']
            try:
                quantidade = int(data['quantidade'])
            except ValueError:
                self.__view.dado_invalido()
            nova_vacina = Vacina(tipo_vacina, fabricante, quantidade)
            lista_vacinas = list(self.__vacinaDAO.get_all())
            for vacina in lista_vacinas:
                if vacina.num_id == num_id:
                    self.__view.vacina_duplicada()
                    return
            self.__vacinaDAO.add(nova_vacina)
            self.__view.cadastro_sucesso()


    def listagem(self):
        self.__view.listagem(list(self.__vacinaDAO.get_all()))

    def get_vacina_att(self):
        lista_vacinas = list(self.__vacinaDAO.get_all())
        return self.__view.get_vacina_att(lista_vacinas)
        print(lista_vacinas)

    def atualizar(self):
        vacina_escolhido = self.get_vacina_att()
        vacina_escolhido = vacina_escolhido[0].split('---')
        try:
            quantidade_int = int(paciente_escolhido[2])
        except ValueError:
            self.__view.dado_invalido()
        else:
            dados = self.__view.atualizar()
            lista_vacinas = list(self.__vacinaDAO.get_all())
            for vacina in lista_vacinas:
                if vacina.num_id == num_id:
                    vacina.tipo_vacina = dados[0]
                    vacina.fabricante = dados[1]
                    vacina.quantidade = dados[2]

    def atualizar(self):
        self.listagem()
        data = self.__view.atualizar()
        lista_vacinas = list(self.__vacinaDAO.get_all())
        for vacina in lista_vacinas:
            if vacina.num_id == data['num_id']:
                vacina.tipo_vacina = data['tipo_vacina']
                vacina.fabricante = data['fabricante']
                vacina.quantidade = data['quantidade']


    def excluir(self):
        lista_vacinas = list(self.__vacinaDAO.get_all())
        vacinas_a_excluir = self.__view.excluir(lista_vacinas)
        if lista_vacinas != None and vacinas_a_excluir != None:
            for vacina in lista_vacinas:
                for exc in vacinas_a_excluir:
                    if vacina.tipo_vacina in exc and vacina.fabricante in exc:
                        self.__vacinaDAO.remove(vacina.num_id)
                        self.__view.sucesso_excluir()

    @property
    def vacinas(self):
        return list(self.__vacinaDAO.get_all())


