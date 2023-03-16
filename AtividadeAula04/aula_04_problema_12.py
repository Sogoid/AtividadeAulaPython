"""Finalidade: Verificação de triângulo
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""

print(
    "\n** Sistema para verificação de triângulo. **\n"
    "******* Informe as número aleatório. ********\n"
)

# Utilize os valores de 3,3,3 para Triângulo Equilátero
# Utilize os valores de 8,9,10 para Triângulo Escaleno
# Utilize os valores de 5,6,5 para Triângulo Isósceles
# Utilize os valores de 3,4,5 para Triângulo Retângulo

l1 = int(input("Digite lado 1 => "))

l2 = int(input("Digite lado 2 => "))

l3 = int(input("Digite lado 3 => "))


print("\n******* Retorno da verificação do triângulo ********\n")

# Verifica se os lados formam um triângulo
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    # Se formam um triângulo, verifica o tipo
    if l1 == l2 == l3:
        print("Forma Triângulo equilátero\n")

    elif ((l1 == l2 and l1 != l3)
          or (l1 == l3 and l2 != l1) or (l2 == l3 and l3 != l1)):
        print("\nForma Triângulo isósceles\n")

    elif (
        l1**2 == (l2**2 + l3**2)
        or l2**2 == (l1**2 + l3**2)
        or l3**2 == (l2**2 + l1**2)
    ):
        print("Forma Triângulo Retângulo")

    # verifica se os lados são diferentes entre si
    elif l1 != l2 or l1 != l3 or l2 != l3:
        print("Forma Triângulo escaleno\n")


else:
    print("Não é possível formar um triângulo com essas medidas\n")
