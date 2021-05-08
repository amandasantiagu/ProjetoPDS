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
        window = sg.Window('Vacinas').Layout(layout)
        button_str = window.read()
        window.close()
        return button_str[0]

    def incluir(self):
        layout = [
                    [sg.Text('Tipo de Vacina', size=(15, 1)), sg.InputText()],
                    [sg.Text('Fabricante', size=(15, 1)), sg.InputText()],
                    [sg.Text('Quantidade', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Incluir Vacina').Layout(layout)
        button_str, items = window.read()
        print('Submit', items)
        if button_str == 'Submit':
            values = self.set_keys_to_attrs(items, ['tipo_vacina', 'fabricante', 'quantidade'])
            window.close()
            return items
        else:
            window.close()
            return None

    def excluir(self, vacinas):
        vacinas_str = []
        for vacina in vacinas:
            vacinas_str.append(vacina.tipo_vacina + ' -- ' + vacina.fabricante)
        layout = [
                    [sg.Listbox(values=vacinas_str, select_mode='extended', key='vac', size=(30, 6))],
                    [sg.Submit(), sg.Cancel()]
                ]
        window = sg.Window('Excluir Vacina').Layout(layout)
        button_str, items = window.read()
        window.close()
        return items['vac']

    def atualizar(self):
        self.clear()
        print("\n Para atualizar o ID deve estar correto")
        tipo_vacina = input("Tipo da Vacina: ")
        fabricante = input("Fabricante: ")
        try:
            quantidade = int(input ("Quantidade: "))
            num_id = int(input("Número do ID: "))
        except ValueError:
            self.dado_invalido('ID')
            return self
        else:
            return {"tipo_vacina":tipo_vacina,"fabricante":fabricante, "quantidade": quantidade, "num_id": num_id}

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
                num_id = "num_id: "+ str(vacina.num_id)
                lista = ["----", tipo_vacina, fabricante, quantidade, num_id]
             
                for values in lista:
                    print(values)
            button, values = window.Read()
            window.close()

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
