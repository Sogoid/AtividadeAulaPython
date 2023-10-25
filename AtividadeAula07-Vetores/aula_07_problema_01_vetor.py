"""Finalidade: Sistema para Conversão de Escalas de Temperatura.
Autor: Diogo da Silveira Ribeiro
data: 12/05/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
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


def celsius():
    """Função para calcular o valor de Celsius."""
    temperatura = []
    for i in range(1):
        c = random.randint(0, 2)
        temperatura.append(c)

        titulo_sistema("Informe os dados para o Cálculo em Celsius.")

        print(f"\nEntre com valor da temperatura em Celsius => {temperatura[i]}°C")

        fahrenheit = (temperatura[i] * 9 / 5) + 32

        print(f"\nValor de Fahrenheit é => {fahrenheit:.0f}°F\n")


def fahrenheits():
    """Função para calcular fahrenheits"""
    f = []
    for i in range(1):
        fahrenheit = random.randint(0, 2)
        f.append(fahrenheit)

        titulo_sistema("Informe os dados para o Cálculo em Fahrenheit.")

        print(f"\nEntre com valor da temperatura em Fahrenheit => {f[i]}°F")

        c = (f[i] - 32) * 5 / 9

        print(f"\nValor de Celsius é => {c:.0f}°C\n")


def app():
    """Função programa principal"""
    titulo_sistema("Sistema para Conversão de Escalas de temperatura.")
    celsius()
    fahrenheits()


if __name__ == "__main__":
    app()
