"""Finalidade: Imprimir três números em ordem crescente e decrescente
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random

print(
    "\n** Sistema p/ imprimir 3 números em ordem crescente e decrescente. **\n"
    "********************** Informe as número aleatório. *******************\n"
)

x = round(random.randrange(1, 10 + 1))
print(f"Digite um número para X => {x} ")
y = round(random.randrange(1, 10 + 1))
print(f"Digite um número para Y => {y} ")
z = round(random.randrange(1, 10 + 1))
print(f"Digite um número para Z => {z}")

print("\n*********** Ordem crescente *************\n")

if x <= y and x <= z and y <= z:
    print(f"Os números em ordem crescente são: X, Y, Z => {x}, {y}, {z}")

elif x <= y and x <= z and z <= y:
    print(f"Os números em ordem crescente são: X, Z, Y => {x}, {z}, {y}")

elif y <= x and y <= z and x <= z:
    print(f"Os números em ordem crescente são: Y, X, Z => {y}, {x}, {z}")

elif y <= x and y <= z and z <= x:
    print(f"Os números em ordem crescente são: Y, Z, X => {y}, {z}, {x}")

elif z <= x and z <= y and x <= y:
    print(f"Os números em ordem crescente são: Z, X, Y => {z}, {x}, {y}")

elif z <= x and z <= y and y <= x:
    print(f"Os números em ordem crescente são: Z, Y, X => {z}, {y}, {x}")

print("\n********** Ordem decrescente ************\n")

if x >= y and x >= z and y >= z:
    print(f"Os números em ordem decrescente são: X, Y, Z => {x}, {y}, {z}")

elif x >= y and x >= z and z >= y:
    print(f"Os números em ordem decrescente são: X, Z, Y => {x}, {z}, {y}")

elif y >= x and y >= z and x >= z:
    print(f"Os números em ordem decrescente são: Y, X, Z => {y}, {x}, {z}")

elif y >= x and y >= z and z >= x:
    print(f"Os números em ordem decrescente são: Y, Z, X => {y}, {z}, {x}")

elif z >= x and z >= y and x >= y:
    print(f"Os números em ordem decrescente são: Z, X, Y => {z}, {x}, {y}")

elif z >= x and z >= y and y >= x:
    print(f"Os números em ordem decrescente são: Z, Y, X => {z}, {y}, {x}")
