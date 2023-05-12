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


def app():
    """Função programa principal"""
    titulo_sistema("Sistema para Conversão de Escalas de temperatura.")

    temperatura = []

    for i in range(10):
        celsius = random.randint(1, 100)
        temperatura.append(celsius)

        titulo_sistema("Informe os dados para o Cálculo.")

        print(f"\nEntre com valor da temperatura em Celsius => {temperatura[i]}°C")

        conversor = float(9.5)

        fahrenheit = (temperatura[i] * conversor) + 32

        print(f"\nValor de Fahrenheit é => {fahrenheit:.0f}°F\n")


if __name__ == "__main__":
    app()
