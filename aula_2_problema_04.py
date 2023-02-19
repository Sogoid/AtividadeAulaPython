"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.9.13
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n********* Sistema de Ajuste de Preços. ************\n"
      "********* Informe os dados do Produto. ************\n"
      )

nomeProduto = input("Nome do Produto: ")
codigoProduto = int(input("Código do produto: "))
valorCompra = float(input("Valor do produto: "))
desconto = float(input("Valor do desconto: "))
__lucro_minimo__ = float(input("Entre com o Lucro Mínimo: "))

# Calculo preço de Venda.
precoVenda = valorCompra * __lucro_minimo__

precoVenda = valorCompra + precoVenda

lucro = precoVenda - valorCompra

desconto = precoVenda * desconto

precoFinal = precoVenda - desconto

lucroReal = precoVenda - precoFinal

print(f"Nome do Produto       => {nomeProduto}\n"
      f"Código do Produto     => {codigoProduto}\n"
      f"Valor de Compra       => R$ {valorCompra:.2f}\n"
      f"Lucro mínimo          => {__lucro_minimo__:.0%}\n"
      f"Valor de Venda        => R$ {precoVenda:.2f}\n"
      f"Lucro de              => R$ {lucro:.2f}\n"
      f"Desconto de           => R$ {desconto:.2f}\n"
      f"Preço Final de Vendas => R$ {precoFinal:.2f}\n"
      f"Lucro Real            => R$ {lucroReal:.2f}\n"
      )
