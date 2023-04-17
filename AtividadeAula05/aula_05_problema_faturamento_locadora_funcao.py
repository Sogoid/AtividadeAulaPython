"""Finalidade: Sistema Locadora de Veículos.
Autor: Diogo da Silveira Ribeiro
data: 29/03/2023
Versão: 0.3
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""


def titulo_sistema(tmsg):
    """Função para mostrar o título através da função."""
    linha_titulo()
    print(f"\n{tmsg}\n")
    linha_titulo()


def linha_titulo():
    """Criação de linha para formar titulo"""
    print("*" * __nun_letras__)


def calculo_fat_anual(faturamento_mensal):
    """Calculo do faturamento anual"""
    __faturamento_anual__ = faturamento_mensal * 12
    return __faturamento_anual__


def calculo_fat_mensal(__valor_aluguel__, __quantidade_veiculo__):
    """Calculo do faturamento mensal"""
    faturamento_mensal = (__valor_aluguel__ * 30) * __quantidade_veiculo__
    return faturamento_mensal


def calculo_fat_terco(__quantidade_veiculo__, __valor_aluguel__):
    """Calculo que mostra um terço dos veículos locados mensal"""
    locado = __quantidade_veiculo__ / 3
    __fat_terco__ = __valor_aluguel__ * locado
    return __fat_terco__


def calulo_fat_terco_anual(__fat_terco__):
    """Calculo que mostra um terço dos veículos locados anual"""
    __fat_terco_anual__ = __fat_terco__ * 12
    return __fat_terco_anual__


def calculo_atraso_pgto(__quantidade_veiculo__, __valor_aluguel__):
    """Calculo de atraso de pagamento"""
    __atrasa_devolucao__ = 0.10
    quantidade_devolucoes = (__quantidade_veiculo__ / 10) * 1
    __atrasa_devolucoes__ = (__valor_aluguel__ * __atrasa_devolucao__) * quantidade_devolucoes
    return __atrasa_devolucoes__


def calculo_atraso_pgto_anual(__atrasa_devolucoes__):
    __atrasa_devolucao__ = __atrasa_devolucoes__ * 12
    return __atrasa_devolucao__


def format_string(num):
    """Função para formatar tempo"""
    num = f"{num:_.2f}"
    num = num.replace(".", ":")
    num = num.replace("_", ".")
    return num


__titulo__ = "Sistema para Locadora de Veículos."
__nun_letras__ = len(__titulo__)

titulo_sistema(__titulo__)

for __cont__ in range(5):
    __cont__ = __cont__ + 1

    titulo_sistema(f"Informe os dados para o Cálculo. {__cont__}")

    # Entrada de dados.
    marca = input("\nQual a marca do veiculo? ")

    modelo = input("Qual o modelo do veículo? ")

    tipo = input("Qual o tipo do veículo? ")

    valor_aluguel = float(input("Diária do aluguel do veículo por dia? R$ "))

    quantidade_veiculo = int(input("Quantidade de Veículos da frota é => "))

    # cálculos

    danificados = round(quantidade_veiculo * 0.02)

    veiculo_compra = round((danificados / 10) * 1)

    frota = round((quantidade_veiculo - danificados) + veiculo_compra)

    faturamento = calculo_fat_mensal(valor_aluguel, quantidade_veiculo)
    faturamento_anual = calculo_fat_anual(faturamento)

    fat_terco = calculo_fat_terco(quantidade_veiculo, valor_aluguel)
    fat_terco_anual = calulo_fat_terco_anual(fat_terco)

    atrasa_devolucoes = calculo_atraso_pgto(quantidade_veiculo, valor_aluguel)
    atrasa_devolucao = calculo_atraso_pgto_anual(atrasa_devolucoes)

    # Formatação dos valores nas saídas.

    print(
        f"\n************ Relatório dos veículos. {__cont__} *************\n"
        f"\nA marca do veículo é => {marca}\n"
        f"\nO modelo do veículo é => {modelo}\n"
        f"\nO tipo do veículo é => {tipo}\n\n"

        f"\n****** Relatório do faturamento por mês. {__cont__} ********\n\n"
        f"Faturamento mensal Previsto é   => R${faturamento:>13}\n"
        f"Frota já alugada no mês é       => R${fat_terco:>13}\n"
        f"Multa por atraso no mês         => R${atrasa_devolucoes:>13}\n"

        f"\n\n***** Relatório do faturamento por Ano. {__cont__} *******\n\n"
        f"Faturamento Anual Previsto é    => R${faturamento_anual:>13}\n"
        f"Faturamento de um terço Anual é => R${fat_terco_anual:>13}\n"
        f"Multa por atraso no Anuais      => R${atrasa_devolucao:>13}\n"

        f"\n\n***** Relatório do estado da frota. {__cont__} ********\n\n"
        f"Quantidade de veículos danificado no ano => {danificados:>2}\n"
        f"Quantidade de veículos comprados é       => {veiculo_compra:>2}\n"
        f"Total da Frota no final do Ano é         => {frota:>2}\n"
    )
