"""Finalidade: Sistema para calculo do IMC.
Autor: Diogo da Silveira Ribeiro
data: 24/10/2023
Versão: 1.0
Python versão: 3.12
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython/Estrutura-de-Dados/Aila01
"""

# Criar um versão 2 do sistema de IMC usando dicionário
# salvando o IMC de dada pessoa, sendo que o sistema deve
# calcular para n pessoas (usando while), o sistema deve perguntar
# se deseja continuar e mostrar as faixa o IMC (usando case)
# Abaixo de 16.0: Magreza grave.
# 16.0 a 16.9: Magreza moderada.
# 17.0 a 18.4: Magreza leve.
# 18.5 a 24.9: Peso saudável (normal).
# 25.0 a 29.9: Sobrepeso.
# 30.0 a 34.9: Obesidade Grau I.
# 35.0 a 39.9: Obesidade Grau II (severa).
# 40.0 ou superior: Obesidade Grau III (mórbida).

import os
import platform
import random
import sys
import time


def logo():
    "Logo do sistema"
    print(
        """
███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗     ██╗███╗   ███╗ ██████╗
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗    ██║████╗ ████║██╔════╝
███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║    ██║██╔████╔██║██║     
╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║    ██║██║╚██╔╝██║██║     
███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║    ██║██║ ╚═╝ ██║╚██████╗
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝╚═╝     ╚═╝ ╚═════╝                                                                                                           
"""
    )


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


def calculo(peso1, altura1):
    """Função para calulo do IMC"""
    resultado = peso1 / (altura1**2)
    return resultado


def clear_terminal():
    """Função para verificar o sistema operacional e limpar o terminal
    Obs.: Esta função não funciona no terminal do PyCharm somente no terminal
    do integrado.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033[H\033[J")


def tempo_sleep(total):
    """Este código define uma função chamada tempo_sleep que recebe um
    argumento total. A função cria uma barra de progresso simples, atualizada
    a cada iteração do loop for.
    Dentro do loop for, a função faz o seguinte:
    Faz uma pausa de 0,1 segundo usando a função sleep do módulo time.
    Move o cursor para o início da linha atual usando o caractere de escape \r.
    Usa uma f-string para formatar a barra de progresso e a porcentagem de
    conclusão. A barra de progresso é criada repetindo o caractere = um número
    de vezes proporcional à porcentagem de conclusão. A porcentagem de
    conclusão é calculada dividindo o índice atual do loop pelo valor total e
    multiplicando por 100.
    Usa a função flush do objeto sys.stdout para forçar a atualização da saída.
    Depois que o loop for é concluído, a função move o cursor para o início da
    linha atual novamente e exibe a barra de progresso completa (100%) usando
    outra f-string. Por fim, a função chama a função print para mover o cursor
    para a próxima linha.
    Quando você chama a função progress_bar com um argumento numérico, ela
    exibe uma barra de progresso que é atualizada ao longo do tempo até
    atingir 100%. 😊"""

    for i in range(total):
        time.sleep(0.1)
        sys.stdout.write("\r")
        sys.stdout.write(
            " " * 12 + f"[{'=' * int(20 * i / total):<20}]" f"{int(100 * i / total)}%"
        )
        sys.stdout.flush()
    sys.stdout.write("\r")
    sys.stdout.write(" " * 12 + f"[{'=' * 20:<20}] 100%")
    sys.stdout.flush()
    print()


def menu_option(info_user):
    """Função criada para ser menu"""
    while True:
        print("\nEscolha uma das opções abaixo:")
        print(
            """
        1 - Cadastro ;\n
        2 - Relatório; \n
        3 - Sair."""
        )
        option = int(input("\nDigite uma opção para interagir: "))
        match option:
            case 1:
                info_user = cadastro(info_user)
            case 2:
                if not info_user:
                    print("Nenhum usuário cadastrado.")
                else:
                    clear_terminal()
                    for user in info_user:
                        report(user)
            case 3:
                clear_terminal()
                logo()
                print("\nSaindo do sistema por favor aguarde!")
                tempo_sleep(50)
                print("\nVocê saiu com Sucesso!!")
                return

        if not should_continue():
            break


def should_continue():
    """
    É uma função auxiliar que interage com o usuário para determinar
    se o programa deve continuar ou não
    """
    while True:
        continuar = input("\nDeseja voltar para o menu inicial? S/N: ").casefold()
        if continuar == "s":
            return True
        elif continuar == "n":
            clear_terminal()
            logo()
            print("\nSaindo do sistema por favor aguarde!")
            tempo_sleep(50)
            print("\nVocê saiu com Sucesso!!")
            break

        else:
            print(
                "\nEntrada inválida."
                " Por favor, digite 's' para continuar ou 'n' para sair."
            )


def go_on_cadastre():
    """
    Função para perguntar se continuar fazendo cadastro.
    """
    while True:
        continuar_cadastro = input("\nDeseja Cadastrar outro usuário? S/N: ").casefold()
        if continuar_cadastro in ["s", "n"]:
            break
        print(
            "\nEntrada inválida."
            "Por favor, digite 's' para continuar ou 'n' para sair."
        )

    if continuar_cadastro == "n":
        return should_continue()

    return True


def cadastro(dados):
    """Função programa principal"""
    clear_terminal()
    logo()

    pessoas_nome = {
        1: "Wanderson",
        2: "Gabriel",
        3: "Caio",
        4: "Diogo",
        5: "Ana",
        6: "Cristiano",
        7: "João",
        8: "Fabrício",
        9: "Pedro",
        10: "Victor",
    }

    pessoas_sobrenome = {
        1: "Ramos",
        2: "Cesar",
        3: "Rego",
        4: "Nogueira",
        5: "Maria",
        6: "Araújo",
        7: "Santos",
        8: "Pereira",
        9: "Augitinho",
        10: "Morais",
    }

    while True:
        info_user = {}

        if dados:
            ultima_matricula = ultima_matricula = dados[-1]["matricula"]
            matricula = ultima_matricula + 1
        else:
            matricula = 1
        info_user["matricula"] = matricula
        print(f"Matricula: {matricula}")

        titulo_sistema(f"Informe os dados do paciente {matricula}")

        nome = random.choice(list(pessoas_nome.values()))
        sobrenome = random.choice(list(pessoas_sobrenome.values()))

        # Combinação do nome e sobrenome
        nome_completo = nome + " " + sobrenome
        info_user["nome_completo"] = nome_completo.upper()
        print(f"Paciente: {nome_completo}")

        peso = float(random.randint(70, 100))
        info_user["peso"] = peso
        print(f"Peso informado: {peso:.2f}")

        altura = float(random.uniform(1.5, 2))
        info_user["altura"] = altura
        print(f"Altura informada: {altura:.2f}")

        idade = int(random.randint(30, 60))
        info_user["idade"] = idade
        print(f"Idade informada: {idade}")

        imc = calculo(peso, altura)
        info_user["imc"] = imc

        # Adicione esta linha para adicionar info_user à lista dados
        dados.append(info_user)

        if not go_on_cadastre():
            break

        clear_terminal()
        logo()
    return dados


def report(info_user):
    """Relatório sobre o paciente
    Mostra em qual o valor de IMC com informações se o mesmo está
    acima ou não do peso.
    """
    logo()
    titulo_sistema(f"Ficha médica do paciente {info_user['matricula']}")

    print(
        f"\nPaciente: {info_user['nome_completo']}\n"
        f"Idade: {info_user['idade']}\n"
        f"Peso: {info_user['peso']}\n"
        f"Altura: {info_user['altura']: .2f}\n"
    )

    print(f"Valor do IMC é: {info_user['imc']: .2f}\n")

    titulo_sistema(f"Resultado medico {info_user['matricula']}")

    imc_ranges = [
        (16.0, "Magreza grave."),
        (16.9, "Magreza moderada."),
        (18.4, "Magreza leve."),
        (24.9, "Peso saudável (normal)."),
        (29.9, "Sobrepeso."),
        (34.9, "Obesidade Grau I."),
        (39.9, "Obesidade Grau II (severa)."),
        (40.0, "ou superior: Obesidade Grau III (mórbida)."),
        (float("inf"), "esta abaixo do peso com"),
    ]

    for i in range(len(imc_ranges) - 1):
        if imc_ranges[i][0] <= info_user["imc"] < imc_ranges[i + 1][0]:
            print(
                f"\nPaciente: {info_user['nome_completo']} "
                f"{imc_ranges[i][1]}{info_user['imc']: .2f}Kg.\n"
            )
            break


def app():
    """Função programa principal"""
    logo()
    titulo_sistema("Programa para Calculo do IMC dos Paciente")
    # Armazena os dados do cadastro em uma variável
    info_user = []

    # Chama a função menu_option passando os dados cadastrados como argumento
    menu_option(info_user)


if __name__ == "__main__":
    app()
