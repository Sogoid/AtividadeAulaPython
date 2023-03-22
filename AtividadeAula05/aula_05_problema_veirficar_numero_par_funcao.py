"""Finalidade: Verificação se o número e impar ou par função com for
autor: Diogo da Silveira Ribeiro
data: 21/03/2023
Versão: 0.4
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random


def titulo_sistema(tmsg):
    """Função para mostrar o título através da função."""
    linha_titulo()
    print(f"\n{tmsg}\n")
    linha_titulo()


def linha_titulo():
    """Criação de linha para formar titulo"""
    print("*" * __nun_letras__)


__titulo__ = "Sistema para verificação se o número e impar ou par."
__nun_letras__ = len(__titulo__)

titulo_sistema(__titulo__)

nuns = []

for i in range(10):

    numero = random.randint(1, 20)
    nuns.append(numero)

__nuns_new__ = str(nuns)[1:-1]
print(f"\nNúmeros sorteados são => {__nuns_new__}\n")

par = sorted(filter(lambda x: x % 2 == 0, nuns))
__par_new__ = str(par)[1:-1]
print(f"Números pares são => {__par_new__}\n")

impar = sorted(filter(lambda x: x % 2 != 0, nuns))
__impar_new__ = str(impar)[1:-1]
print(f"Números impares são => {__impar_new__}")
