"""Finalidade: Sistema para Cálculo de Gasto de Combustível.
Autor: Diogo da Silveira Ribeiro
data: 21/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""
import random


def titulo_sistema(tmsg):
    """Função para mostrar o título através da função."""
    linha_titulo()
    print(f"\n{tmsg}\n")
    linha_titulo()


def linha_titulo():
    """Criação de linha para formar titulo"""
    print("*" * __nun_letras__)


__titulo__ = "Sistema para Cálculo de Combustível."
__nun_letras__ = len(__titulo__)

titulo_sistema(__titulo__)


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
    __sub_titulo__ = f"Cadastro de de viagens. N° {x}"
    __nun_ = len(__sub_titulo__)

    titulo_sistema(__sub_titulo__)

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

    total_gasto = litros * valor_litro

    # Formatação dos valores nas saídas.


    def format_tempo(num):
        """Função para formatar tempo"""
        num = f"{num:_.2f}"
        num = num.replace(".", ":")
        num = num.replace("_", ".")
        return num


    def format_virgula(palavra):
        """Função para formatar tempo"""
        palavra = f"{palavra:_.2f}"
        palavra = palavra.replace(".", ",")
        palavra = palavra.replace("_", ".")
        return palavra


    __sub_titulo__ = "Relatório de gastos na viagem."
    __nun_letra__ = len(__sub_titulo__)

    titulo_sistema(__sub_titulo__)

    print(
        f"\nVelocidade média é               => {velocidade:>7}h/Km\n"
        f"Distancia percorrida foi de      =>   {distancia:.2f}km\n"
        f"Rendamento de combustível por km =>   {rendimento:>6}Lt/Km"
    )

    formatted_string = format_tempo(tempo)
    print(f"Tempo gasto foi de               => {formatted_string:>8}hs")

    formatted_string = format_virgula(litros_usados)
    print(f"total de litros gasto foi        =>  {formatted_string:>7}LT")

    formatted_string = format_virgula(total_gasto)
    print(f"Total do valor gasto foi de      =>R$ {formatted_string}\n")
