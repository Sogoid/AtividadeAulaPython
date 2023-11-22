import numpy as np


class VetorNaoOrdenado:
    """Criando vetor não ordenado"""

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
        else:
            self.last_stand += 1
            self.dados[self.last_stand] = valor

    def search(self, valor):
        """Função para pesquisar o valor no vetor."""
        for i in range(self.last_stand + 1):
            if valor == self.dados[i]:
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

v1 = VetorNaoOrdenado(10)
print("Inserindo no vetor")
v1.insert(4)
v1.insert(6)
v1.insert(1)
v1.insert(9)
v1.insert(5)
v1.imprimir()

print("\nRetornando a pesquisa das posições no vetor")
print(
    f"\nPesquisa pelo 4 em {v1.search(4)} pos\n"
    f"Pesquisa pelo 1 em {v1.search(1)} pos\n"
    f"Pesquisa pelo 9 em {v1.search(9)} pos\n"
    f"Pesquisa pelo 8 em {v1.search(8)} pos\n"
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
