import numpy as np


def shell_sort(vetor):
    intervalo = len(vetor) // 2
    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2
    return vetor


# Teste
v1 = np.array([25, 35, 18, 7])
print("Vetor original: ", v1)

v2 = shell_sort(v1)
print("Vetor ordenado", v2)
