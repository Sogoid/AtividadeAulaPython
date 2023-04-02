"""Finalidade: Sistema para Cálculo de Gasto de Combustível.
Autor: Diogo da Silveira Ribeiro
data: 21/03/2023
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


def calculo_distancia(__tempo__, __velocidade__):
    """Função que vai calcular a distância"""
    __distancia__ = __tempo__ * __velocidade__
    return __distancia__


def calculo_rendimento(__distancia__, __litro__):
    """Função para calcular o rendimento"""
    __rendimento__ = __distancia__ / __litro__
    return __rendimento__


def calculo_lt_usados(__distancia__, __rendimento__):
    """Função para calcular os litros usados"""
    __litros_usados__ = __distancia__ / __rendimento__
    return __litros_usados__


for x in range(6):

    titulo_sistema(f"Cadastro de de viagens. N° {x}")

    velocidade = round(random.randint(80, 100 + 1))
    print(f"\nQual é a velocidade? => {velocidade}")

    tempo = random.randint(1, 3)
    print(f"Quanto tempo de viagem? => {tempo}")

    litros = random.randint(10, 80)
    print(f"Quantos litros gastou de combustível? {litros}")

    valor_litro = random.randint(3, 6)
    print(f"Preço do litro => R$ {valor_litro}")

    print()

    distancia = calculo_distancia(
        tempo,
        velocidade,
    )

    rendimento = calculo_rendimento(distancia, litros)

    litros_usados = calculo_lt_usados(distancia, rendimento)

    total_gasto = calculo_total_gasto(litros, valor_litro)

    gera_relatorio()
