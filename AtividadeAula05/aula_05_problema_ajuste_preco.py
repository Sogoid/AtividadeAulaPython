"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.3
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


def get_format(num):
    """Formatação de F-string"""

    num = f"{num: _.2f}"
    num = num.replace(".", ",")
    num = num.replace("_", ".")
    return num


def calculo_prec_venda(__valor_compra__, __lucro_minimo__):
    """Calculo preço de Venda."""

    __prec_lucro_min__ = __valor_compra__ * __lucro_minimo__
    __prec_venda__ = __valor_compra__ + __prec_lucro_min__
    return __prec_venda__


def lucro_venda(__valor_compra__, __prec_venda__):
    """Calculo lucro de venda."""
    __lucro__ = __prec_venda__ - __valor_compra__
    return __lucro__


def calculo_desconto(prec_venda, __desconto__):
    """Calculo do desconto."""
    desconto_valor = prec_venda * __desconto__
    __prec_final__ = prec_venda - desconto_valor
    return __prec_final__


def luc_final(prec_venda, __prec_final__):
    """Calculo do lucro final"""
    __lucro_real__ = prec_venda - __prec_final__
    return __lucro_real__


def gera_relatorio(cont, codigo_produto, nome_produto, valor_compra, lucro, preco_venda, prec_final, lucro_real):
    """Função para gerar relatório"""

    titulo_sistema(f"Relatório do ajuste de Preços. N°{cont}")

    print(
        f"\nCódigo do Produto => {codigo_produto}\n"
        f"Nome do Produto => {nome_produto.upper()}\n"
        f"Lucro mínimo => {__lucro_minimo__: .0%}\n"
        f"Desconto de => {__desconto__: .0%}\n"
    )

    formatted_string = get_format(valor_compra)
    print(f"Valor de Compra => R$ {formatted_string: >5}")

    formatted_string = get_format(lucro)
    print(f"Lucro de => R$ {formatted_string: >5}")

    formatted_string = get_format(preco_venda)
    print(f"Valor de Venda => R$ {formatted_string: >5}")

    formatted_string = get_format(prec_final)
    print(f"Preço Final de Vendas => R$ {formatted_string: >5}")

    formatted_string = get_format(lucro_real)
    print(f"Lucro Real => R$ {formatted_string: >5}\n")


titulo_sistema("Sistema de Ajuste de Preços.")

produto = [
    "Pão",
    "Sal",
    "Feijão",
    "Arroz",
    "Macarrão",
    "Cebola",
    "Alface",
    "Carne",
    "Pera",
    "Bolacha",
    "Biscoito",
    "Batata",
]

__desconto__ = 0.10

__lucro_minimo__ = 0.33


def app():
    """Função programa principal"""
    cont = 0
    while 9 >= cont:
        cont = cont + 1

        titulo_sistema(f"Informe os dados do Produto. N°{cont}")

        codigo_produto = cont
        print(f"\nCódigo do produto: {codigo_produto}")

        nome_produto = produto[random.randrange(len(produto))]
        print(f"Nome do Produto: {nome_produto.upper()}")

        valor_compra = float(random.uniform(1.5, 20))
        print(f"Valor do produto: R$ {valor_compra: .2f}")

        print(f"Valor do desconto: {__desconto__: .0%}")

        print(f"Entre com o Lucro Mínimo: {__lucro_minimo__: .0%}\n")

        preco_venda = calculo_prec_venda(valor_compra, __lucro_minimo__)

        lucro = lucro_venda(valor_compra, preco_venda)

        prec_final = calculo_desconto(preco_venda, __desconto__)

        lucro_real = luc_final(preco_venda, prec_final)

        gera_relatorio(cont, codigo_produto, nome_produto,
                       valor_compra, lucro, preco_venda, prec_final, lucro_real)


if __name__ == "__main__":
    app()
