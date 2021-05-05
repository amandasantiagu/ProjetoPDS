import PySimpleGUI as sg
from abc import ABC, abstractmethod

class AbstractView(ABC):

    def __init__(self, title_text):
        self.__title_text = title_text
        self.__window = None


    def show(self, layout):
        self.__window = sg.Window(self.__title_text).Layout(layout)
        

    def read(self):
        button, values = window.Read()
        return values
