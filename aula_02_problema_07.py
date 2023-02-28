"""Finalidade: Sistema Locadora de Veículos.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

<<<<<<< HEAD
print("\n********** Sistema para Locadora de Veículos. *************\n"
      "*********** Informe os dados para o Cálculo. **************\n"
      )
=======
print(
    "\n********* Sistema para Locadora de Veículos. ************\n"
    "*********** Informe os dados para o Cálculo. **************\n"
)
>>>>>>> 27be0f8 (Atualizações)

# Entrada de dados.
valorAluguel = float(input("Qual é o valor do aluguel do veículo por dia? => R$ "))

quantidadeVeiculo = int(input("Quantidade de Veículos da frota é => "))

# cálculos

danificados = round(quantidadeVeiculo * 0.02)

veiculoCompra = round((danificados / 10) * 1)

frota = round((quantidadeVeiculo - danificados) + veiculoCompra)

locado = quantidadeVeiculo / 3

faturamento = (valorAluguel * 30) * quantidadeVeiculo

faturamentoAnual = faturamento * 12

faturamentoTerco = valorAluguel * locado

faturamentoTercoAnual = faturamentoTerco * 12

# Calculo de atraso de pagamento

atrasaDevolucao = 0.10

quantidadeDevolucoes = (quantidadeVeiculo / 10) * 1

atrasaDevolucoes = (valorAluguel * atrasaDevolucao) * quantidadeDevolucoes

atrasaDevolucao = atrasaDevolucoes * 12

# Formatação dos valores na saídas.

faturamento = f"{faturamento:_.2f}"
faturamento = faturamento.replace(".", ",").replace("_", ".")

faturamentoTerco = f"{faturamentoTerco:_.2f}"
faturamentoTerco = faturamentoTerco.replace(".", ",").replace("_", ".")

faturamentoAnual = f"{faturamentoAnual:_.2f}"
faturamentoAnual = faturamentoAnual.replace(".", ",").replace("_", ".")

faturamentoTercoAnual = f"{faturamentoTercoAnual:_.2f}"
faturamentoTercoAnual = faturamentoTercoAnual.replace(".", ",").replace("_", ".")

atrasaDevolucao = f"{atrasaDevolucao:_.2f}"
atrasaDevolucao = atrasaDevolucao.replace(".", ",").replace("_", ".")

atrasaDevolucoes = f"{atrasaDevolucoes:_.2f}"
atrasaDevolucoes = atrasaDevolucoes.replace(".", ",").replace("_", ".")

<<<<<<< HEAD
print("\n********** Relatório do faturamento por mês. **************\n\n"
      f"Faturamento mensal Previsto é   => R${faturamento:>13}\n"
      f"Frota já alugada no mês é       => R${faturamentoTerco:>13}\n"
      f"Multa por atraso no mês         => R${atrasaDevolucoes:>13}\n"
      "\n\n********** Relatório do faturamento por Ano. **************\n\n"
      f"Faturamento Anual Previsto é    => R${faturamentoAnual:>13}\n"
      f"Faturamento de um terço Anual é => R${faturamentoTercoAnual:>13}\n"
      f"Multa por atraso no Anuais      => R${atrasaDevolucao:>13}\n"
      "\n\n************ Relatório do estado da frota. ****************\n\n"
      f"Quantidade de veículos danificado no ano => {danificados:>2}\n"
      f"Quantidade de veículos comprados é       => {veiculoCompra:>2}\n"
      f"Total da Frota no final do Ano é         => {frota:>2}\n"
      )
=======
print(
    "\n********** Relatório do faturamento por mês. **************\n\n"
    f"Faturamento mensal Previsto é   => R${faturamento:>10}\n"
    f"Frota já alugada no mês é       => R${faturamentoTerco:>10}\n"
    f"Multa por atraso no mês         => R${atrasaDevolucoes:>10}\n"
    "\n\n********** Relatório do faturamento por Ano. **************\n\n"
    f"Faturamento Anual Previsto é    => R${faturamentoAnual:>10}\n"
    f"Faturamento de um terço Anual é => R${faturamentoTercoAnual:>10}\n"
    f"Multa por atraso no Anuais      => R${atrasaDevolucao:>10}\n"
    "\n\n********** Relatório do estado da frota. **************\n\n"
    f"Quantidade de veículos danificado no ano => {danificados:>15}\n"
    f"Quantidade de veículos comprados é       => {veiculoCompra:>15}\n"
    f"Total da Frota no final do Ano é         => {frota:>15}\n"
)
>>>>>>> 27be0f8 (Atualizações)
