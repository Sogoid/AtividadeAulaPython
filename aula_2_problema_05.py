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

valorLitro = float(input("Preço do litro => R$ "))

km = float(input("Quantos KM seu carro roda com 1 Litro? => "))

velocidadeMedia = float(input("Qual é a velocidade média? => "))

tempoGasto = float(input("Quanto tempo de viagem? => "))

quantidadeLitros = float(input("Quantos litros foi gasto? => "))

kmLitro = valorLitro / km

distancia = tempo * velocidade

litrosUsados = distancia / rendimento

print(f"Velocidade média é                => {velocidadeMedia}"
      f"Tempo gasto foi de                => {tempoGasto}"
      f"Distancia percorrida foi de       => {distancia}"
      f"Quantidade de litros gasto foi de => {litrosUsados}"
      # f"Total do valor gasto foi de       =>{totalGasto}"
      )
