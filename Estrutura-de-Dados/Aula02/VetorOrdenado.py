import numpy as np


class VetorOrdenado:
    """Criando vetor ordenado"""

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.last_stand = -1
        self.dados = np.empty(capacidade, dtype=int)

    def imprimir(self):
        """Função de impressão"""
        if self.last_stand == -1:
            print("O vetor esta vazio")
        else:
            for i in range(self.last_stand + 1):
                print(i, " - ", self.dados[i])

    def insert(self, valor):
        """Função para inserir dados no vetor"""
        if self.last_stand == self.capacidade - 1:
            print("Capacidade máxima atingida")
            return
        position = 0
        for i in range(self.last_stand + 1):
            position = i
            if self.dados[i] > valor:
                break
            if i == self.last_stand:
                position = i + 1
        aux = self.last_stand
        while aux >= position:
            self.dados[aux + 1] = self.dados[aux]
            aux -= 1

        self.dados[position] = valor
        self.last_stand += 1

    def search(self, valor):
        """Função para pesquisar vetor
        """
        for i in range(self.last_stand + 1):
            if self.dados[i] > valor:
                return -1
            if self.dados[i] == valor:
                return i
        return -1

    def excluir(self, valor):
        """Função para excluir valor no vetor"""
        position = self.search(valor)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_stand):
                self.dados[i] = self.dados[i + 1]
        self.last_stand -= 1


# Teste
v1 = VetorOrdenado(10)
print("Inserindo no vetor ordenado")
v1.insert(4)
v1.insert(6)
v1.insert(1)
v1.insert(9)
v1.insert(5)
v1.insert(3)
v1.insert(7)
v1.insert(2)
v1.insert(8)
v1.insert(10)
v1.insert(11)
v1.imprimir()

print("\nRetornando a pesquisa das posições no vetor")
print(
    f"\nPesquisa pelo 1 em {v1.search(1)} pos\n"
    f"Pesquisa pelo 1 em {v1.search(1)} pos\n"
    f"Pesquisa pelo 1 em {v1.search(9)} pos\n"
    f"Pesquisa pelo 1 em {v1.search(8)} pos\n"
)

print("Excluindo do vetor")
v1.excluir(1)
v1.excluir(9)
v1.imprimir()

print("\nRetornando a pesquisa das posições no vetor apos exclusão")
print(
    f"\nPesquisa pelo 1 em {v1.search(1)} pos\n"
    f"Pesquisa pelo 9 em {v1.search(9)} pos\n"
)
