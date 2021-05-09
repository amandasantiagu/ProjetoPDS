import PySimpleGUI as sg

from .abstractView import AbstractView

class VacinaView(AbstractView):

    def tela_vacina(self):
        layout = [
                    [sg.Button('Incluir Vacina')],
                    [sg.Button('Listar Vacinas')],
                    [sg.Button('Atualizar Vacina')],
                    [sg.Button('Remover Vacina')],
                    [sg.Button('Sair')],
                ]
        window = sg.Window('Cadastro de Vacinas', size=(300,200)).Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]

    def incluir(self):
        layout = [
                    [sg.Text('Tipo de Vacina', size=(15, 1)), sg.InputText()],
                    [sg.Text('Fabricante', size=(15, 1)), sg.InputText()],
                    [sg.Text('Quantidade', size=(15, 1)), sg.InputText()],
                    [sg.Text('Nº Registro', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Incluir Vacina').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':
            window.close()
            return items
        else:
            window.close()
            return None

    def listagem(self, listagem):
        layout = [
                [sg.Output(size=(40,30), key="_listagem_")],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window('Listagem de Vacinas').Layout(layout)
        button, values = window.Read(timeout=6)
        
        while button != 'Voltar' and button != None:
            window.FindElement("_listagem_").Update('')
            for vacina in listagem:
                tipo_vacina = "Tipo de Vacina: " + str(vacina.tipo_vacina)
                fabricante = "Fabricante: "+ str(vacina.fabricante)
                quantidade = "Quantidade: "+ str(vacina.quantidade)
                num_registro = "Nº Registro: "+ str(vacina.num_registro)
                lista = ["----", tipo_vacina, fabricante, quantidade, num_registro]
             
                for values in lista:
                    print(values)
            button, values = window.Read()
            window.close()

    def get_vacina_att(self, lista_vacinas):
        vacina_str = []
        for vacina in lista_vacinas:
            vacina_str.append(vacina.tipo_vacina + '---' + vacina.fabricante + '---' + str(vacina.quantidade) + '---' + str(vacina.num_registro))
        layout = [
                    [sg.Listbox(values=vacina_str, select_mode='extended', key='vac', size=(30, 6))],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Escolha a Vacina').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':
            window.close()
            return items['vac']
        else:
            window.close()
            return None

    def atualizar(self):
        layout = [
                    [sg.Text('Tipo de Vacina', size=(15, 1)), sg.InputText()],
                    [sg.Text('Fabricante', size=(15, 1)), sg.InputText()],
                    [sg.Text('Quantidade', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Atualizar Vacina').Layout(layout)
        button_str, items = window.read()
        window.close()
        try:
            items[2]= int(items[2])
        except ValueError:
            self.dado_invalido()
        else:
            if 'Submit' in button_str:
                return items
            else:
                return None

    def cadastro_sucesso(self):
        sg.popup("------- Vacina cadastrada com sucesso! -------")

    def vacina_duplicada(self):
        sg.popup("Erro! Vacina com ID já cadastrada.")

    def dado_invalido(self):
        sg.popup("Erro! Dado inválido ")

    def sucesso_atualizar(self):
        sg.popup("------- Atualizado com Sucesso. --------")

    def sucesso_excluir(self):
        sg.popup("------- Excluido com Sucesso -------.")

    def error(self, error_msg: str):
        sg.popup("ERRO: " + error_msg)
