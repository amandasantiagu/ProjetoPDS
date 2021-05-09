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
            tipo_vacina = data[0]
            fabricante = data[1]
            try:
                quantidade = int(data[2])
                num_registro = int(data[3])
            except ValueError:
                self.__view.dado_invalido()
            else:
                nova_vacina = Vacina(tipo_vacina, fabricante, quantidade, num_registro)
                lista_vacinas = list(self.__vacinaDAO.get_all())
                for vacina in lista_vacinas:
                    if vacina.num_id == num_registro:
                        self.__view.vacina_duplicada()
                        return
                self.__vacinaDAO.add(nova_vacina)
                self.__view.cadastro_sucesso()
        else:
            return


    def listagem(self):
        self.__view.listagem(list(self.__vacinaDAO.get_all()))

    def get_vacina_att(self):
        lista_vacinas = list(self.__vacinaDAO.get_all())
        return self.__view.get_vacina_att(lista_vacinas)

    def atualizar(self):
        vacina_escolhida = self.get_vacina_att()
        if vacina_escolhida != None:
            try:
                vacina_escolhida = vacina_escolhida[0].split('---')
            except IndexError:
                #Erro ao clicar submit sem selecionar -> vacina_escolhida = [] - lista vazia
                self.__view.error("Nenhum Paciente Escolhido")
                return
        else:
            #Fecha a janela e volta se clicar em Voltar -> paciente_escolhido = None
            return
        try:
            vacina_escolhida[2] = int(vacina_escolhida[2])
            num_registro = int(vacina_escolhida[3])
        except ValueError:
            self.__view.dado_invalido()
        else:
            dados = self.__view.atualizar()
            lista_vacinas = list(self.__vacinaDAO.get_all())
            for vacina in lista_vacinas:
                if vacina.num_registro == num_registro:
                    vacina.tipo_vacina = dados[0]
                    vacina.fabricante = dados[1]
                    vacina.quantidade = dados[2]
                    self.__vacinaDAO.add(vacina)

    def excluir(self):
        lista_vacinas = list(self.__vacinaDAO.get_all())
        vacinas_a_excluir = self.__view.get_vacina_att(lista_vacinas)
        if lista_vacinas != None and vacinas_a_excluir != None:
            for vacina in lista_vacinas:
                for exc in vacinas_a_excluir:
                    if vacina.tipo_vacina in exc and vacina.fabricante in exc:
                        self.__vacinaDAO.remove(vacina.num_registro)
                        self.__view.sucesso_excluir()
                        return
            self.__view.error("Nenhuma vacina selecionada!")

    @property
    def lista_vacinas(self):
        return list(self.__vacinaDAO.get_all())


