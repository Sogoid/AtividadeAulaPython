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

    numero = random.randint(1, 20)
    nuns.append(numero)

__nuns_new__ = str(nuns)[1:-1]
print(f"Números sorteados são => {__nuns_new__}\n")

par = sorted(filter(lambda x: x % 2 == 0, nuns))
__par_new__ = str(par)[1:-1]
print(f"Números pares são => {__par_new__}\n")

impar = sorted(filter(lambda x: x % 2 != 0, nuns))
__impar_new__ = str(impar)[1:-1]
print(f"Números impares são => {__impar_new__}")

# if numero % 2 == 0:

#    nuns.append(numero)
#    print("O número é par\n")

# else:
#    print("O número é impar\n")
