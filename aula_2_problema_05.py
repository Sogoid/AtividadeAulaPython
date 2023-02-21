"""Finalidade: Sistema de Ajuste de Preços.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n********* Sistema para Cálculo de Combustível. ************\n"
      "*********** Informe os dados para o Cálculo. **************\n"
      )

velocidade = float(input("Qual é a velocidade? => "))

tempo = float(input("Quanto tempo de viagem? => "))

litros = float(input("Quantos litros gastou de combustível? "))

valorLitro = float(input("Preço do litro => R$ "))

# Calculo

distancia = tempo * velocidade

rendimento = distancia / litros

litrosUsados = distancia / rendimento

totalGasto = litros * valorLitro

# Formatação dos valores na saídas.

tempo = f"{tempo:_.2f}"
tempo = tempo.replace(".", ":").replace("_", ".")

rendimento = f"{rendimento:_.2f}"
rendimento = rendimento.replace(".", ",").replace("_", ".")

litrosUsados = f"{litrosUsados:_.2f}"
litrosUsados = litrosUsados.replace(".", ",").replace("_", ".")

totalGasto = f"{totalGasto:_.2f}"
totalGasto = totalGasto.replace(".", ",").replace("_", ".")

print("\n********** Relatório de gastos na viagem. **************\n\n"
      f"Velocidade média é                =>   {velocidade:>6}h/Km\n"
      f"Tempo gasto foi de                =>   {tempo:>6}hs\n"
      f"Distancia percorrida foi de       =>   {distancia:.2f}km\n"
      f"Rendamento de combustível por km  =>   {rendimento:>6}Lt/Km\n"
      f"Quantidade de litros gasto foi de =>   {litrosUsados:>6}LT\n"
      f"Total do valor gasto foi de       =>R$ {totalGasto}"
      )
