import numpy as np


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro is None:
            print("A lista está vazia!")
            return None
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.primeiro is None:
            print("A lista está vazia!")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisa(self, valor):
        if self.primeiro is None:
            print("A lista está vazia!")
            return None
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            atual = atual.proximo
        return atual

    def excluir_posicao(self, valor):
        if self.primeiro is None:
            print("A lista está vazia!")
            return None
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            anterior = atual
            atual = atual.proximo
            # Se o atual for igual ao primeiro vamos apontar para o proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo

            # Senão o ponteiro proximo do anterior recebe o proximo valor que
            # vai ser excluído.
        else:
            anterior.proximo = atual.proximo
        return atual


# Teste
# no1 = No(10)
# no1.mostra_no()
# Criar uma Lista Encadeada
lista = ListaEncadeada()

lista.insere_inicio(10)
lista.insere_inicio(20)
lista.insere_inicio(30)
lista.insere_inicio(40)
lista.insere_inicio(50)
# lista.excluir_inicio()
lista.mostrar()

print("")

lista.excluir_posicao(30)
lista.mostrar()

# lista_pesquisa = lista.pesquisa(20)
# print(lista_pesquisa)
# if lista_pesquisa is None:
#     print("Não encontrado")
# else:
#     print("Encontrado")
