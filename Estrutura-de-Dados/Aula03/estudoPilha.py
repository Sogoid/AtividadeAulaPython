import numpy as np


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self) -> object:
        print(self.valor)


# Testes

no1 = No(10)
no1.mostra_no()
