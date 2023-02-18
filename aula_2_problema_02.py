"""Finalidade: Cadastro dos clientes de um sistema de comércio eletrônico.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.9.13
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n** Programa de cadastro de cliente do Comércio Eletrônico **")
print("******** Informe os dados para cadastro do cliente *********\n")

nome = input("Nome: ")

apelido = input("Apelido: ")

print("Gênero:")
genero = input("Masculino (M) / Feminino (F): ")

telefone = int(input("Telefone: "))

email = input("Email: ")

endereco = input("Endereço: ")

numero = int(input("Nº: "))

barrio = input("Barrio: ")

cidade = input("Cidade: ")

estado = input("Estado: ")

cep = input("CEP: ")

senhas = input("Digita uma senha: ")

rep_senhas = input("Digita sua senha novamente: ")

while senhas != rep_senhas:
    print("\nSenhas diferentes. Tente novamente.\n")
    senhas = input("Digita uma senha: ")

    rep_senhas = input("Digita sua senha novamente: ")
    print()
else:
    print("Senha cadastrada com sucesso!\n")

print("Cadastro realizado com Sucesso!!\n")

print("*************** Relatório do cadastro do cliente ***********\n")

print(f"Nome: {nome}\n"
      f"Apelido: {apelido}\n"
      f"Gênero: {genero}\n"
      f"Telefone: {telefone}\n"
      f"E-mail: {email}"
      f"Endereço: {endereco}\n"
      f"Nº: {numero}\n"
      f"Barrio: {barrio}\n"
      f"Cidade: {cidade}\n"
      f"Estado: {estado}"
      f"CEP: {cep}\n"
      f"Senha: {senhas}"
      )
