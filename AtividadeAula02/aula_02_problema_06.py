"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n*** Sistema para Conversão de Escalas de temperatura. ****\n"
      "*********** Informe os dados para o Cálculo. *************\n"
      )

celsios = float(input("Entre com valor da temperatura em °C => "))

conversor = float(9.5)

fahrenheit = (celsios * conversor) + 32

print(f"\nValor de Fahrenheit é => {fahrenheit:.0f}°F\n")
