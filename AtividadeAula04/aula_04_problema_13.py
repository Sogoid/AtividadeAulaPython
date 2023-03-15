"""Finalidade: Verificação se o número e impar ou par
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""

print(
    "\n** Sistema para verificação se o número e impar ou par. **\n"
    "******* Informe as número aleatório. ********\n"
)

numero = int(input("Digite um número inteiro: "))

numero = numero % 2

if numero == 0:
    print("O número é par")

else:
    print("O número é impar")
