"""Finalidade: Programa para Calculo do IMC dos Paciente
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
print(
    "\n****** Programa para Calculo do IMC dos Paciente ******\n"
    "*********** Informe os dados do paciente **************\n"
)

nome = input("Nome: ")
peso = float(input("Peso: "))
altura = float(input("Altura: "))
idade = int(input("Idade: "))

imc = peso / (altura**2)

print("\n*************** Ficha médica do paciente **************\n")

print(
    f"Paciente: {nome}\n"
    f"Idade: {idade}\n"
    f"Peso: {peso}\n"
    f"Altura: {altura}\n"
)

print(f"Valor do IMC é: {imc:.2f}\n")

print("*************** Resultado medico **********************\n")

if 19.1 >= imc and imc <= 25.8:
    print(f"Paciente: {nome!r} esta com peso normal com {imc:.2f}.\n")
elif imc > 25.8:
    print(f"Paciente: {nome!r} esta acima do peso com {imc:.2f}.\n")
else:
    print(f"Paciente: {nome!r} esta abaixo do peso com {imc:.2f}.\n")
