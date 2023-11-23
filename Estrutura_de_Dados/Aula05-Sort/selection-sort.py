import numpy as np


def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp
    return vetor


# Teste
v1 = np.array([25, 35, 18, 7])
print("Vetor original: ", v1)

v2 = selection_sort(v1)
print("Vetor ordenado", v2)
