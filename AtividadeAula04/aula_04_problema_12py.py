"""Finalidade: Verificação de triângulo
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random

print(
    "\n** Sistema para verificação de triângulo. **\n"
    "******* Informe as número aleatório. ********\n"
)

l1 = round(random.randrange(1, 10 + 1))
print(f"Digite o lado 1 => {l1}")

l2 = round(random.randrange(1, 10 + 1))
print(f"Digite o lado 2 => {l2}")

l3 = round(random.randrange(1, 10 + 1))
print(f"Digite o lado 3 => {l3}")


print("\n******* Retorno da verificação do triângulo ********\n")

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print("Existe um triângulo\n")

    if l1 == l2 and l1 == l3 and l2 == l3:
        print("\nForma triângulo equilátero\n")

    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Forma triângulo isosceles\n")

    elif (
        (l1**2 == l2**2) + l3**2
        or (l2**2 == l1**2) + l3**2
        or (l3**2 == l2**2) + l1**2
    ):
        print("")

    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Forma triângulo escaleno\n")

else:
    print("Não existe um triângulo\n")
