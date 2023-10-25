"""Finalidade: Sistema Locadora de Veículos.
Autor: Diogo da Silveira Ribeiro
data: 17/03/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""


def len_titulo(titulo):
    """Função para mostrar o título através da função."""
    return len(titulo)


def linha_titulo(titulo):
    """Criação de linha para formar titulo"""
    __nun_letras__ = len_titulo(titulo)
    print("*" * __nun_letras__)


def titulo_sistema(tmsg):
    """Função para mostrar o título através da função."""
    linha_titulo(tmsg)
    print(f"\n{tmsg}\n")
    linha_titulo(tmsg)


# cálculos
def calculo_danificado(__quantidade_veiculo__):
    """Função para calcular os veículos danificados"""
    __danificados__ = round(__quantidade_veiculo__ * 0.02)
    return __danificados__


def calculo_compra_veiculo(__danificados__):
    """Função para calcular os veículos comprados"""
    __veiculo_compra__ = round((__danificados__ / 10) * 1)
    return __veiculo_compra__


def calculo_frota(__quant_veiculo__, __danificados__, __veic_comp__):
    """Função para calcular de frotas"""
    __frota__ = round((__quant_veiculo__ - __danificados__) + __veic_comp__)
    return __frota__


def calculo_locado(__quantidade_veiculo__):
    """Função quantidade veiculo locado"""
    __locado__ = __quantidade_veiculo__ / 3
    return __locado__


def calculo_fat_mensal(__valor_aluguel__, __quantidade_veiculo__):
    """Função para calcular o faturamento mensal"""
    __faturamento_mensal__ = (__valor_aluguel__ * 30) * __quantidade_veiculo__
    return __faturamento_mensal__


def calculo_fat_anual(__faturamento_mensal__):
    """Função para calcular o faturamento mensal"""
    __faturamento_anual__ = __faturamento_mensal__ * 12
    return __faturamento_anual__


def calculo_fat_terco(__valor_aluguel__, __locado__):
    """Função para calcular do faturamento mensal referente a um terço"""
    __fat_terco__ = __valor_aluguel__ * __locado__
    return __fat_terco__


def calculo_fat_terco_anual(__fat_terco__):
    """Função para calcular o faturamento anula referente a um terço"""
    __fat_terco_anual__ = __fat_terco__ * 12
    return __fat_terco_anual__


# Calculo de atraso de pagamento


def calculo_quant_devolucoes(__quantidade_veiculo__):
    """Função para calcular a quantidade de devoluções"""
    __quantidade_devolucoes__ = (__quantidade_veiculo__ / 10) * 1
    return __quantidade_devolucoes__


def calculo_atrasa_devolucao(
    __valor_aluguel__, __atrasa_devolucao__, __quantidade_devolucoes__
):
    """Função para calcular o atraso nas devoluções"""
    __atrasa_devolucoes__ = (
        __valor_aluguel__ * __atrasa_devolucao__
    ) * __quantidade_devolucoes__
    return __atrasa_devolucoes__


def calculo_atrasa_devolucao_anual(__atrasa_devolucoes__):
    """Função para calcular o atraso nas devoluções no período de 12 meses"""
    __atrasa_devolucao_anual__ = __atrasa_devolucoes__ * 12
    return __atrasa_devolucao_anual__


def get_format(num):
    """Formatação de F-string"""
    num = f"{num:_.2f}"
    num = num.replace(".", ",")
    num = num.replace("_", ".")
    return num


def gera_relatorio():
    """Função para gerar relatório"""

    titulo_sistema(f"Relatório dos veículos. {__cont__}")

    print(
        f"\nA marca do veículo é => {marca}\n"
        f"\nO modelo do veículo é => {modelo}\n"
        f"\nO tipo do veículo é => {tipo}\n\n"
    )

    titulo_sistema(f"Relatório do faturamento por mês. {__cont__}")

    formatted_string = get_format(faturamento_mensal)
    print(f"\nFaturamento mensal Previsto é   => R${formatted_string:>13}")

    formatted_string = get_format(fat_terco)
    print(f"Frota já alugada no mês é       => R${formatted_string:>13}")

    formatted_string = get_format(atrasa_devolucoes)
    print(f"Multa por atraso no mês         => R${formatted_string:>13}\n")

    titulo_sistema(f"Relatório do faturamento por Ano. {__cont__}")

    formatted_string = get_format(faturamento_anual)
    print(f"\nFaturamento Anual Previsto é    => R${formatted_string:>13}")

    formatted_string = get_format(fat_terco_anual)
    print(f"Faturamento de um terço Anual é => R${formatted_string:>13}")

    formatted_string = get_format(__atrasa_devolucao__)
    print(f"Multa por atraso no Anuais      => R${formatted_string:>13}\n")

    titulo_sistema(f"Relatório do estado da frota. {__cont__}")

    formatted_string = get_format(danificados)
    print(f"\nQuantidade de veículos danificado" 
          f" no ano => {formatted_string:>5}")

    formatted_string = get_format(veiculo_compra)
    print(f"Quantidade de veículos comprados é       => {formatted_string:>5}")

    formatted_string = get_format(frota)
    print(f"Total da Frota no final do Ano é   " 
          f"      => {formatted_string:>5}\n")


titulo_sistema("Sistema para Locadora de Veículos.")

__atrasa_devolucao__ = 0.10

for __cont__ in range(5):
    __cont__ = __cont__ + 1

    titulo_sistema(f"Informe os dados para o Cálculo. {__cont__}")

    # Entrada de dados.
    marca = input("Qual a marca do veiculo? ")

    modelo = input("Qual o modelo do veículo? ")

    tipo = input("Qual o tipo do veículo? ")

    valor_aluguel = float(input("Diária do aluguel do veículo por dia? R$ "))

    quantidade_veiculo = int(input("Quantidade de Veículos da frota é => "))

    # calulos buscando função

    danificados = calculo_danificado(quantidade_veiculo)

    veiculo_compra = calculo_compra_veiculo(danificados)

    frota = calculo_frota(quantidade_veiculo, danificados, veiculo_compra)

    locado = calculo_locado(quantidade_veiculo)

    faturamento_mensal = calculo_fat_mensal(valor_aluguel, quantidade_veiculo)

    faturamento_anual = calculo_fat_anual(faturamento_mensal)

    fat_terco = calculo_fat_terco(valor_aluguel, locado)

    fat_terco_anual = calculo_fat_terco_anual(fat_terco)

    # Calculo de atraso de pagamento

    quantidade_devolucoes = calculo_quant_devolucoes(quantidade_veiculo)

    atrasa_devolucoes = calculo_atrasa_devolucao(
        valor_aluguel, __atrasa_devolucao__, quantidade_devolucoes
    )

    __atrasa_devolucao__ = calculo_atrasa_devolucao_anual(atrasa_devolucoes)

    gera_relatorio()
