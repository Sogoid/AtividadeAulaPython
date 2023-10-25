"""Finalidade: Programa para cálculo do IMC dos pacientes usando função
autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.4
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""
import random


def len_titulo(titulo):
    """Função para mostrar o título através da função."""
    return len(titulo)


def linha_titulo(titulo):
    """Criação de linha para formar titulo"""
    __nun_letras__ = len_titulo(titulo)
    print("*" * __nun_letras__)


def titulo_sistema(tmsg):
    """Função para mostrar o título através da função."""
    linha_titulo(tmsg)
    print(f"\n{tmsg}\n")
    linha_titulo(tmsg)


def calculo(peso1, altura1):
    """Função para calulo do IMC"""
    resultado = peso1 / (altura1**2)
    return resultado


def relatorio():
    """Relatório sobre o paciente
    Mostra em qual o valor de IMC com informações se o mesmo está
    acima ou não do peso.
    """
    titulo_sistema(f"Ficha médica do paciente {__cont__}")

    print(
        f"\nPaciente: {nome}\n"
        f"Idade: {__idade__}\n"
        f"Peso: {peso}\n"
        f"Altura: {altura:.2f}\n"
    )

    print(f"Valor do IMC é: {imc:.2f}\n")

    titulo_sistema(f"Resultado medico {__cont__}")

    if 18.5 <= imc <= 24.9:
        print(f"\nPaciente: {nome!r} esta com peso normal com {imc:.2f}.\n")

    elif 25 <= imc <= 27.3:
        print(f"\nPaciente: {nome!r}"
              f"esta um pouco acima do peso com {imc:.2f}.\n")

    elif 27.4 <= imc <= 32.3:
        print(f"\nPaciente: {nome!r}"
              f"esta muito acima do peso com {imc:.2f}.\n")

    elif imc > 32.3:
        print(f"\nPaciente: {nome!r} esta acima do peso com {imc:.2f}.\n")

    else:
        print(f"\nPaciente: {nome!r} esta abaixo do peso com {imc:.2f}.\n")


titulo_sistema("Programa para Calculo do IMC dos Paciente")

pessoas = [
    "Wanderson Ramos",
    "Gabriel Cesar",
    "Caio Rego",
    "Diogo Nogueira",
    "Ana Maria",
    "Cristiano Araújo",
]

for __cont__ in range(5):
    __cont__ = __cont__ + 1

    titulo_sistema(f"Informe os dados do paciente {__cont__}")

    nome = pessoas[random.randrange(len(pessoas))]
    print(f"\nNome: {nome}")

    peso = float(random.randint(70, 100))
    print(f"Peso: {peso}")

    altura = float(random.uniform(1.5, 2))
    print(f"Altura: {altura:.2f}")

    __idade__ = int(random.randint(30, 60))
    print(f"Idade: {__idade__}\n")

    imc = calculo(peso, altura)

    relatorio()
