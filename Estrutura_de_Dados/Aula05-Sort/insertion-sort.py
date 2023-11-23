import numpy as np


def insertion_sort(vetor):
    n = len(vetor)

    for i in range(1, n):
        marcador = vetor[i]
        j = i - 1
        while j >= 0 and (marcador < vetor[j]):
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcador
    return vetor


# Teste
v1 = np.array([25, 35, 18, 7])
print("Vetor original: ", v1)

v2 = insertion_sort(v1)
print("Vetor ordenado", v2)
