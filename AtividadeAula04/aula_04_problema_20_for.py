"""Finalidade: Sistema Locadora de Veículos.
Autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n********** Sistema para Locadora de Veículos. *************\n")

for __cont__ in range(5):
    __cont__ = __cont__ + 1

    print(f"******** Informe os dados para o Cálculo. {__cont__} *********\n")

    # Entrada de dados.
    marca = input("Qual a marca do veiculo? ")

    modelo = input("Qual o modelo do veículo? ")

    tipo = input("Qual o tipo do veículo? ")

    valorAluguel = float(input("Diária do aluguel do veículo por dia? R$ "))

    quantidadeVeiculo = int(input("Quantidade de Veículos da frota é => "))

    # cálculos

    danificados = round(quantidadeVeiculo * 0.02)

    veiculoCompra = round((danificados / 10) * 1)

    frota = round((quantidadeVeiculo - danificados) + veiculoCompra)

    locado = quantidadeVeiculo / 3

    faturamento = (valorAluguel * 30) * quantidadeVeiculo

    faturamentoAnual = faturamento * 12

    fat_terco = valorAluguel * locado

    fat_terco_anual = fat_terco * 12

    # Calculo de atraso de pagamento

    atrasaDevolucao = 0.10

    quantidadeDevolucoes = (quantidadeVeiculo / 10) * 1

    atrasaDevolucoes = (valorAluguel * atrasaDevolucao) * quantidadeDevolucoes

    atrasaDevolucao = atrasaDevolucoes * 12

    # Formatação dos valores na saídas.

    faturamento = f"{faturamento:_.2f}"
    faturamento = faturamento.replace(".", ",").replace("_", ".")

    fat_terco = f"{fat_terco:_.2f}"
    fat_terco = fat_terco.replace(".", ",").replace("_", ".")

    faturamentoAnual = f"{faturamentoAnual:_.2f}"
    faturamentoAnual = faturamentoAnual.replace(".", ",").replace("_", ".")

    fat_terco_anual = f"{fat_terco_anual:_.2f}"

    fat_terco_ano = fat_terco_anual.replace(".", ",").replace("_", ".")

    atrasaDevolucao = f"{atrasaDevolucao:_.2f}"
    atrasaDevolucao = atrasaDevolucao.replace(".", ",").replace("_", ".")

    atrasaDevolucoes = f"{atrasaDevolucoes:_.2f}"
    atrasaDevolucoes = atrasaDevolucoes.replace(".", ",").replace("_", ".")

    print(
        f"\n************ Relatório dos veículos. {__cont__} *************\n"
        f"\nA marca do veículo é => {marca}\n"
        f"\nO modelo do veículo é => {modelo}\n"
        f"\nO tipo do veículo é => {tipo}\n\n"
        f"\n****** Relatório do faturamento por mês. {__cont__} ********\n\n"
        f"Faturamento mensal Previsto é   => R${faturamento:>13}\n"
        f"Frota já alugada no mês é       => R${fat_terco:>13}\n"
        f"Multa por atraso no mês         => R${atrasaDevolucoes:>13}\n"
        f"\n\n***** Relatório do faturamento por Ano. {__cont__} *******\n\n"
        f"Faturamento Anual Previsto é    => R${faturamentoAnual:>13}\n"
        f"Faturamento de um terço Anual é => R${fat_terco_ano:>13}\n"
        f"Multa por atraso no Anuais      => R${atrasaDevolucao:>13}\n"
        f"\n\n***** Relatório do estado da frota. {__cont__} ********\n\n"
        f"Quantidade de veículos danificado no ano => {danificados:>2}\n"
        f"Quantidade de veículos comprados é       => {veiculoCompra:>2}\n"
        f"Total da Frota no final do Ano é         => {frota:>2}\n"
    )
