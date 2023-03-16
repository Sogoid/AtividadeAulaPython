"""Finalidade: Verificação se o número e impar ou par
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random

print(
    "\n** Sistema para verificação se o número e impar ou par. **\n"
    "******* Informe as número aleatório. ********\n"
)

nuns = []

while len(nuns) <= 10:

    numero = round(random.randrange(1, 20 + 1))
    print(f"Digite um número => {numero}\n")

if numero % 2 == 0:
    nuns.append(numero) 
    print("O número é par\n")

else:
    print("O número é impar\n")
