"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.3
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""
import random


def linha_titulo():
    """Criação de linha para formar titulo"""
    print("*" * 42)


def get_format(num):
    """Formatação de F-string"""

    num = f"{num:_.2f}"
    num = num.replace(".", ",")
    num = num.replace("_", ".")
    return num


def calculo(__valor_compra__, __desconto__, __lucro_minimo__):
    """Calculo preço de Venda."""

    preco_venda = __valor_compra__ * __lucro_minimo__
    preco_venda = __valor_compra__ + preco_venda
    lucro = preco_venda - __valor_compra__
    desconto_valor = preco_venda * __desconto__
    preco_final = preco_venda - desconto_valor
    lucro_real = preco_venda - preco_final

    return (
        preco_venda,
        lucro,
        lucro_real,
        preco_final,
    )


linha_titulo()
print("Sistema de Ajuste de Preços.")
linha_titulo()


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

__cont__ = 0

__desconto__ = 0.10

__lucro_minimo__ = 0.33

while __cont__ <= 9:
    __cont__ = __cont__ + 1

    print(f"******* Informe os dados do Produto. {__cont__} ********\n")

    nome_produto = produto[random.randrange(len(produto))]
    print(f"Nome do Produto: {nome_produto}")

    __codigo_produto__ = int(random.randint(1, 10))
    print(f"Código do produto: {__codigo_produto__}")

    __valor_compra__ = float(random.uniform(1.5, 20))
    print(f"Valor do produto: R$ {__valor_compra__:.2f}")

    print(f"Valor do desconto: {__desconto__}")

    print(f"Entre com o Lucro Mínimo: {__lucro_minimo__}")

    preco_venda, lucro, lucro_real, preco_final = calculo(
        __valor_compra__,
        __desconto__,
        __lucro_minimo__,
    )

    # Formatação dos valores nas saídas.

    print(
        f"\n****** Relatório do ajuste de Preços.{__cont__} ********\n\n"
        f"Nome do Produto       => {nome_produto.upper()}\n"
        f"Código do Produto     => {__codigo_produto__}\n"
        f"Lucro mínimo          => {__lucro_minimo__:.0%}\n"
    )

    formatted_string = get_format(__valor_compra__)
    print(f"Valor de Compra       => R$ {formatted_string:>5}")

    formatted_string = get_format(lucro)
    print(f"Lucro de              => R$ {formatted_string:>5}")

    formatted_string = get_format(preco_venda)
    print(f"Valor de Venda        => R$ {formatted_string:>5}")

    formatted_string = get_format(__desconto__)
    print(f"Desconto de           => R$ {formatted_string:>5}")

    formatted_string = get_format(preco_final)
    print(f"Preço Final de Vendas => R$ {formatted_string:>5}")

    formatted_string = get_format(lucro_real)
    print(f"Lucro Real            => R$ {formatted_string:>5}\n")
