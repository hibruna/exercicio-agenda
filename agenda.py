class Agenda:
    def __init__(self, nome, ano):
        self.__nome = input('Digite seu nome ')
        self.__ano = input('Digite o ano ')

    def get_nome(self):
        return self.__nome

    def get_ano(self):
        return self.__ano
