"""Finalidade: Sistema para Cálculo de Gasto de Combustível.
Autor: Diogo da Silveira Ribeiro
data: 21/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""


def titulo_sistema(tmsg):
    """Função para mostrar o titulo através da função."""
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
    """Função que vai calcular a distancia"""
    __distancia__ = __tempo__ * __velocidade__
    return __distancia__


def calculo_rendimento(__distancia__, __litro__):
    """Função para calcular o rendimento"""
    __rendimento__ = __distancia__ / __litro__
    return __rendimento__


def calculo_lt_usados(__distancia__, __rendimento__):
    """Função para calcular o litros usados"""
    __litros_usados__ = __distancia__ / __rendimento__
    return __litros_usados__


velocidade = float(input("\nQual é a velocidade? => "))

tempo = float(input("Quanto tempo de viagem? => "))

litros = float(input("Quantos litros gastou de combustível? "))

valorLitro = float(input("Preço do litro => R$ "))

print()

distancia = calculo_distancia(
    tempo,
    velocidade,
)

rendimento = calculo_rendimento(distancia, litros)

litros_usados = calculo_lt_usados(distancia, rendimento)

total_gasto = litros * valorLitro

# Formatação dos valores na saídas.


def format_tempo(__tempo__):
    """Função para formatar tempo"""
    __tempo__ = f"{__tempo__:_2f}"
    __tempo__ = __tempo__.replace(".", ":")
    __tempo__ = __tempo__.replace("_", ".")
    return __tempo__


def format_virgula(palavra):
    """Função para formatar tempo"""
    palavra = f"{palavra:_2f}"
    palavra = palavra.replace(".", ",")
    palavra = palavra.replace("_", ".")
    return palavra


__sub_titulo__ = "Relatório de gastos na viagem."
__nun_letras__ = len(__sub_titulo__)

titulo_sistema(__sub_titulo__)

print(
    f"\nVelocidade média é                =>   {velocidade:>6}h/Km\n"
    f"Distancia percorrida foi de       =>   {distancia:.2f}km\n"
    f"Rendamento de combustível por km  =>   {rendimento:>7}Lt/Km\n"
)

formatted_string = format_tempo(tempo)
print(f"Tempo gasto foi de               => {formatted_string:>6}hs\n")

formatted_string = format_virgula(litros_usados)
print((f"total de litros gasto foi =>  {formatted_string:>6}LT\n"))

formatted_string = format_virgula(total_gasto)
print(f"Total do valor gasto foi de    =>R$ {formatted_string}\n")
