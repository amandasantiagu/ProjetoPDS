import PySimpleGUI as sg
class PostoView:

    def incluir(self):
        layout = [
            [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Atualização de nome do Posto').Layout(layout)
        button_str, items = window.read()
        if button_str == 'Submit':  
            window.close()
            return items[0]
        else:
            window.close()
            return None

