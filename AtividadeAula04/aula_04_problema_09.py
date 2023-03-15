"""Finalidade: Para identificar diferença entre número
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random

print(
    "\n******** Sistema para identificar diferença entre número. *********\n"
    "***************** Informe as número aleatório. ********************\n"
)

x = round(random.randrange(1, 100 + 1))
print(f"Digite um número para X => {x} ")
y = round(random.randrange(1, 100 + 1))
print(f"Digite um número para Y => {y} ")
z = round(random.randrange(1, 100 + 1))
print(f"Digite um número para Z => {z}")

print("\n*********** Qual é o maior número? *************\n")

if x > y and x > z:
    print(f"O maior número é X => {x}")
elif y > x and y > z:
    print(f"O maior número é Y => {y}")
elif z > x and x > y:
    print(f"O maior número é Z => {z}")

print("\n*********** Qual é o menor número? *************\n")

if x < y and x < z:
    print(f"O menor número é X => {x}")
elif y < x and y < z:
    print(f"O menor número é Y => {y}")
elif z < x and x < y:
    print(f"O menor número é Z => {z}")

print("\n*********** Qual é número do meio? *************\n")

if x > y and x < z:
    print(f"O número do meio é X => {x}\n")
elif y < x and y > z:
    print(f"O número do meio é Y => {y}\n")
elif z > x and x < y:
    print(f"O número do meio é Z => {z}\n")
