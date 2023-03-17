"""Finalidade: Programa para Calculo do IMC dos Paciente usando for
autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.3
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
print("\n****** Programa para Calculo do IMC dos Paciente ******\n")

for __cont__ in range(5):
    __cont__ = __cont__ + 1
    print(f"********* Informe os dados do paciente {__cont__} ************\n")

    nome = input("Nome: ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    idade = int(input("Idade: "))

    imc = peso / (altura**2)

    print(f"\n************ Ficha médica do paciente {__cont__} ************\n")

    print(
        f"Paciente: {nome}\n"
        f"Idade: {idade}\n"
        f"Peso: {peso}\n"
        f"Altura: {altura}\n"
    )

    print(f"Valor do IMC é: {imc:.2f}\n")

    print(f"*************** Resultado medico {__cont__}******************\n")

    if imc >= 18.5 and imc <= 24.9:
        print(f"Paciente: {nome!r} esta com peso normal com {imc:.2f}.\n")

    elif imc >= 25 and imc <= 27.3:
        print(f"Paciente: {nome!r}"
              f"esta um pouco acima do peso com {imc:.2f}.\n")

    elif imc >= 27.4 and imc <= 32.3:
        print(f"Paciente: {nome!r} esta muito acima do peso com {imc:.2f}.\n")

    elif imc > 32.3:
        print(f"Paciente: {nome!r} esta acima do peso com {imc:.2f}.\n")

    else:
        print(f"Paciente: {nome!r} esta abaixo do peso com {imc:.2f}.\n")
