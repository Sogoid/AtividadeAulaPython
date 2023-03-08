"""Finalidade: Cadastro de Funcionário de uma Empresa
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n****** Programa para Calculo do Salário Funcionário ******\n"
      "*********** Informe os dados do funcionário **************\n"
      )

# Dados do cadastro do funcionário.
nome = input("Nome: ")
cpf = int(input("CPF: "))


# Dados referente a calculo do salário.
salarioBase = float(input("Salario Base: "))
transporte = int(input("Valor do Vale Transporte: "))
alimentacao = int(input("Valor do Vale Alimentação: "))
periculosidade = float(input("Porcentagem da Periculosidade: "))
insalubridade = float(input("Porcentagem da Insalubridade: "))
jornada = 40
quantidadesemana = 4
quantidadedias = 5

print()

# Calculo para descobrir a quantidade de dias.
dias = quantidadesemana * quantidadedias

# Calculo do vale-transporte e Alimentação.
transporte = dias * transporte

alimentacao = dias * alimentacao

# Calculo Horas Trabalhadas.
horasMensais = jornada * quantidadesemana

valorHora = salarioBase / horasMensais

# Calculo da Pericolosidade e Insalubriade.
periculosidade = salarioBase * periculosidade

insalubridade = salarioBase * insalubridade

# Calculo do Salário.
salario = (horasMensais * valorHora) + periculosidade + \
    insalubridade + transporte + alimentacao

# Formatação dos valores na saídas.

valorHora = f"{valorHora:_.2f}"
valorHora = valorHora.replace(".", ",").replace("_", ".")

transporte = f"{transporte:_.2f}"
transporte = transporte.replace(".", ",").replace("_", ".")

alimentacao = f"{alimentacao:_.2f}"
alimentacao = alimentacao.replace(".", ",").replace("_", ".")

periculosidade = f"{periculosidade:_.2f}"
periculosidade = periculosidade.replace(".", ",").replace("_", ".")

insalubridade = f"{insalubridade:_.2f}"
insalubridade = insalubridade.replace(".", ",").replace("_", ".")

salario = f"{salario:_.2f}"
salario = salario.replace(".", ",").replace("_", ".")

salarioBase = f"{salarioBase:_.2f}"
salarioBase = salarioBase.replace(".", ",").replace("_", ".")

print("********* Contra-Cheque dos dados do funcionário ***********\n")

print(f"Nome: {nome.upper()}\n"
      f"CPF:  {cpf}\n"
      "----------------------------------------\n"
      )

print(f"Valor da Hora  => R$ {valorHora:_>10}\n"
      f"Transporte     => R$ {transporte:_>10}\n"
      f"Alimentação    => R$ {alimentacao:_>10}\n"
      f"Periculosidade => R$ {periculosidade:_>10}\n"
      f"Insalubridade  => R$ {insalubridade:_>10}\n"
      f"Salário        => R$ {salario:_>10}\n"
      )

print("******** Informações adicionais do Contra-Cheque **********\n")

print(
    f"Salário Base  => R$ {salarioBase:_>10}\n"
    f"Horas Mensais => {horasMensais} HS"
)
