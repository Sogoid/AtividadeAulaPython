"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n********* Sistema de Ajuste de Preços. ************\n")

__cont__ = 0

while __cont__ <= 9:
    __cont__ = __cont__ + 1

    print(f"********* Informe os dados do Produto. {__cont__} ***********\n")

    codigo_produto = int(input("Código do produto: "))
    nome_produto = input("Nome do Produto: ")
    valor_compra = float(input("Valor do produto: "))
    desconto = 0.10
    print(f"Valor do desconto: {desconto:.0%}")
    lucro_minimo = 0.33
    print(f"Entre com o Lucro Mínimo: {lucro_minimo:.0%}")

    # Calculo preço de Venda.
    preco_venda = valor_compra * lucro_minimo

    preco_venda = valor_compra + preco_venda

    lucro = preco_venda - valor_compra

    desconto_new = preco_venda * desconto

    preco_final = preco_venda - desconto_new

    lucro_real = preco_venda - preco_final

    # Formatação dos valores nas saídas.

    valor_compra = f"{valor_compra:_.2f}"
    valor_compra = valor_compra.replace(".", ",").replace("_", ".")

    preco_venda = f"{preco_venda:_.2f}"
    preco_venda = preco_venda.replace(".", ",").replace("_", ".")

    lucro = f"{lucro:_.2f}"
    lucro = lucro.replace(".", ",").replace("_", ".")

    preco_final = f"{preco_final:_.2f}"
    preco_final = preco_final.replace(".", ",").replace("_", ".")

    lucro_real = f"{lucro_real:_.2f}"
    lucro_real = lucro_real.replace(".", ",").replace("_", ".")

    print(
        f"\n******** Relatório do ajuste de Preços.{__cont__} **********\n\n"
        f"Código do Produto     => {codigo_produto}\n"
        f"Nome do Produto       => {nome_produto.upper()}\n"
        f"Lucro mínimo          =>    {lucro_minimo:.0%}\n"
        f"Desconto de           =>    {desconto:.0%}\n"
        f"Valor de Compra       => R$ {valor_compra:>5}\n"
        f"Lucro de              => R$ {lucro:>5}\n"
        f"Valor de Venda        => R$ {preco_venda:>5}\n"
        f"Preço Final de Vendas => R$ {preco_final:>5}\n"
        f"Lucro Real            => R$ {lucro_real:>5}\n"
    )
