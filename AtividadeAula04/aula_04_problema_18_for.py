"""Finalidade: Verificação se o número e impar ou par usando for
autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.3
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random

print(
    "\n** Sistema para verificação se o número e impar ou par. **\n"
    "******* Informe as número aleatório. ********\n"
)

for nuns in range(10):

    numero = random.randint(1, 20)
    print(f"Números sorteados é => {numero}\n")

    if numero % 2 == 0:

        print("O número é par\n")

    else:
        print("O número é impar\n")
