"""Finalidade: Cadastro dos clientes de um sistema de comércio eletrônico.
Autor: Diogo da Silveira Ribeiro
data: 14/02/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAula2
"""

print("\n** Programa de cadastro de cliente do Comércio Eletrônico **\n"
      "******** Informe os dados para cadastro do cliente *********\n"
      )

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

print("\nSenha cadastrada com sucesso!\n"
      "Cadastro realizado com Sucesso!!\n"
      )

print("*************** Relatório do cadastro do cliente ***********\n")

print(f"Nome:     {nome.upper()}\n"
      f"Apelido:  {apelido.upper()}\n"
      f"Gênero:   {genero.upper()}\n"
      f"Telefone: {telefone}\n"
      f"E-mail:   {email}"
      f"Endereço: {endereco.upper()}\n"
      f"Nº:       {numero}\n"
      f"Barrio:   {barrio.upper()}\n"
      f"Cidade:   {cidade.upper()}\n"
      f"Estado:   {estado.upper()}"
      f"CEP:      {cep}\n"
      f"Senha:    {senhas}\n"
      )
