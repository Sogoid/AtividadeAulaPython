"""finalidade: Calculo do IMC
autor: Diogo da Silveia Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.9.13
Link do repositorio no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n****** Programa para Calculo do IMC dos Paciente ******")
print("*********** Informe os dados do paciente **************\n")

nome = input("Nome: ")
peso = float(input("Peso: "))
altura = float(input("Altura: "))
idade = int(input("Idade: "))

imc = peso / (altura**2)

print()
print("*************** Ficha médica do paciente **************\n")

print(
    f"Paciente: {nome}\nIdade: {idade}\nPeso: {peso}\nAltura: {altura}")

print(f"Valor do IMC é: {imc:.2f}\n")

print("*************** Resultado medico **********************\n")

if not 18.5 > imc and imc <= 24.9:
    print(f"Paciente: {nome!r} esta com peso normal com {imc:.2f}.")
elif imc > 24.9:
    print(f"Paciente: {nome!r} esta acima do peso com {imc:.2f}.")
else:
    print(f"Paciente: {nome!r} esta abaixo do peso com {imc:.2f}.")
