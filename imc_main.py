"""finalidade: Calculo do IMC
autor: Diogo
data: 14/02/2023
Python versão: 3.9.13
"""

print("\n****** Programa para Calculo do IMC dos Paciente ******")
print("*********** Informe os dados do paciente **************\n")

nome = input("Digite o nome: ")
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
idade = int(input("Digite a idade: "))

imc = peso / (altura**2)

print(
    f"Paciente: {nome}\nIdade: {idade}\nPeso: {peso}\nAltura: {altura}")
print(f"Valor do IMC é: {imc}")
