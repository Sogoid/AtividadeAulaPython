"""Lista duplamente encadeada
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)


class ListaDuplamenteEncadeada:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia__(self):
        if self.primeiro is None:
            return True
        return False

    def inseri_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia__():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar_inicio(self):
        if self.__lista_vazia__():
            print("Lista está vazia!")
            return
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_final(self):
        if self.__lista_vazia__():
            print("Lista está vazia!")
            return
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def inseri_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia__():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia__():
            print("Lista está vazia!")
            return
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior is None
            self.primeiro = self.primeiro.proximo
            return temp.valor

    def excluir_final(self):
        if self.__lista_vazia__():
            print('Lista está vazia!')
            return
        temp = self.ultimo
        if self.primeiro.proximo is None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp.valor

    def excluir_posicao(self, valor):
        if self.__lista_vazia__():
            print('Lista está vazia!')
            return


# Teste
lista = ListaDuplamenteEncadeada()
lista.inseri_inicio(1)
lista.inseri_inicio(2)
lista.inseri_inicio(3)
lista.inseri_inicio(4)

lista.mostrar_inicio()

lista.inseri_final(8)
