"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.10.9
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
lucroMinimo = float(input("Entre com o Lucro Mínimo: "))

# Calculo preço de Venda.
precoVenda = valorCompra * lucroMinimo

precoVenda = valorCompra + precoVenda

lucro = precoVenda - valorCompra

desconto = precoVenda * desconto

precoFinal = precoVenda - desconto

lucroReal = precoVenda - precoFinal

# Formatação dos valores na saídas.

valorCompra = f"{valorCompra:_.2f}"
valorCompra = valorCompra.replace(".", ",").replace("_", ".")

precoVenda = f"{precoVenda:_.2f}"
precoVenda = precoVenda.replace(".", ",").replace("_", ".")

lucro = f"{lucro:_.2f}"
lucro = lucro.replace(".", ",").replace("_", ".")

desconto = f"{desconto:_.2f}"
desconto = desconto.replace(".", ",").replace("_", ".")

precoFinal = f"{precoFinal:_.2f}"
precoFinal = precoFinal.replace(".", ",").replace("_", ".")

lucroReal = f"{lucroReal:_.2f}"
lucroReal = lucroReal.replace(".", ",").replace("_", ".")

print("\n******** Relatório do ajuste de Preços. ***********\n\n"
      f"Nome do Produto       => {nomeProduto.upper()}\n"
      f"Código do Produto     => {codigoProduto}\n"
      f"Lucro mínimo          =>    {lucroMinimo:.0%}\n"
      f"Valor de Compra       => R$ {valorCompra:>5}\n"
      f"Lucro de              => R$ {lucro:>5}\n"
      f"Valor de Venda        => R$ {precoVenda:>5}\n"
      f"Desconto de           => R$ {desconto:>5}\n"
      f"Preço Final de Vendas => R$ {precoFinal:>5}\n"
      f"Lucro Real            => R$ {lucroReal:>5}\n"
      )
