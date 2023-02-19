"""Finalidade: Cadastro de Funcionário de uma Empresa
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.9.13
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

print("********* Contra-Cheque dos dados do funcionário ***********\n")

print(f"Nome: {nome}\n"
      f"CPF: {cpf}"
      )

print(f"Valor da Hora  => R$ {valorHora:.2f}\n"
      f"Transporte     => R$ {transporte:.2f}\n"
      f"Alimentação    => R$ {alimentacao:.2f}\n"
      f"Periculosidade => R$ {periculosidade:.2f}\n"
      f"Insalubridade  => R$ {insalubridade:.2f}\n"
      f"Salário        => R$ {salario:.2f}\n"
      )

print("******** Informações adicionais do Contra-Cheque **********\n")

print(
    f"Salário Base  => R$ {salarioBase:.2f}\n"
    f"Horas Mensais => {horasMensais} HS"
)
