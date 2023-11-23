import numpy as np


def bubble_sort(vetor):
    n = len(vetor)
    # Complexidade 0(n^2) um for dentro e outro for
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor


# Teste

v1 = np.array([25, 35, 18, 7])
print("Vetor original: ", v1)

v2 = bubble_sort(v1)

print("Vetor ordenado", v2)
