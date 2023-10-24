"""Finalidade: Cadastro dos clientes de um sistema de comércio eletrônico.
Autor: Diogo da Silveira Ribeiro
data: 12/05/2023
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


def cadastro(dados):
    """Função para cadastrar cliente"""
    titulo_sistema("Informe os dados para cadastro do cliente.")
    # Cria uma lista vazia para armazenar dados
    continuar = "s"

    while continuar == "s":
        informacoes_usuario = []

        print(f"Current data: {dados}")

        if dados:
            ultima_matricula = int(dados[-1][0])
            matricula = ultima_matricula + 1
        else:
            matricula = 1
        informacoes_usuario.append(matricula)
        print(f"Matricula: {matricula}")

        nome = input("Nome: ")
        informacoes_usuario.append(nome.upper())

        apelido = input("Apelido: ")
        informacoes_usuario.append(apelido.upper())

        print("Gênero:")
        genero = input("Masculino (M) / Feminino (F): ")
        informacoes_usuario.append(genero.upper())

        telefone = int(input("Telefone: "))
        informacoes_usuario.append(telefone)

        email = input("Email: ")
        informacoes_usuario.append(email)

        endereco = input("Endereço: ")
        informacoes_usuario.append(endereco.upper())

        numero = int(input("Nº: "))
        informacoes_usuario.append(numero)

        bairro = input("Bairro: ")
        informacoes_usuario.append(bairro.upper())

        cidade = input("Cidade: ")
        informacoes_usuario.append(cidade.upper())

        estado = input("Estado: ")
        informacoes_usuario.append(estado.upper())

        cep = input("CEP: ")
        informacoes_usuario.append(cep)

        senhas = input("Digita uma senha: ")
        informacoes_usuario.append(senhas)

        rep_senhas = input("Digita sua senha novamente: ")
        informacoes_usuario.append(rep_senhas)

        dados.append(informacoes_usuario)

        # Chama a função verifica_senha passando os dados como argumento
        verifica_senha(dados)

        continuar = input("\nDeseja cadastrar outro usuário? (s/n) ")

    return dados


def verifica_senha(dados):
    """Função para verificar se a senha do cliente são iguais"""
    for usuario in dados:
        senhas = usuario[-2]
        rep_senhas = usuario[-1]
        while senhas != rep_senhas:
            print("\nSenhas diferentes. Tente novamente.\n")

            senhas = input("Digita uma senha: ")
            rep_senhas = input("Digita sua senha novamente: ")

            # Atualiza as senhas do usuário na lista de dados
            usuario[-2] = senhas
            usuario[-1] = rep_senhas

    print("\nSenha cadastrada com sucesso!"
          "\nCadastro realizado com Sucesso!!\n")


def atualizar(dados):
    """Função para atualizar os dados de um usuário"""
    matricula = int(
        input("\nDigite o matricula do usuário que deseja atualizar: "))
    for usuario in dados:
        if usuario[0] == matricula:
            print(
                "Usuário encontrado. Escolha a opção abaixo para atualize as informações do usuário:")
            continuar = "s"
            while continuar == 's' or continuar == 'S':
                print("\nEscolha uma das opções abaixo:\n")
                print('''
                    1 – Apelido ;\n
                    2 – Telefone ;\n
                    3 – E-mail; \n
                    4 - Endereço; \n
                    5 - Sair.''')
                opcao = int(input("\nDigite uma opção que deseja atualizar: "))
                match opcao:
                    case 1:
                        usuario[2] = input("Novo apelido: ")
                        usuario[2] = usuario[2].upper()
                        print("Dados atualizados com sucesso!")
                        break
                    case 2:
                        usuario[4] = int(input("Novo telefone: "))
                        print("Dados atualizados com sucesso!")
                        break
                    case 3:
                        usuario[5] = input("Novo email: ")
                        print("Dados atualizados com sucesso!")
                        break
                    case 4:
                        usuario[6] = input("Novo endereço: ")
                        usuario[6] = usuario[6].upper()
                        usuario[7] = int(input("Novo número: "))
                        usuario[8] = input("Novo bairro: ")
                        usuario[8] = usuario[8].upper()
                        usuario[9] = input("Nova cidade: ")
                        usuario[9] = usuario[9].upper()
                        usuario[10] = input("Novo estado: ")
                        usuario[10] = usuario[10].upper()
                        usuario[11] = input("Novo CEP: ")
                        print("Dados atualizados com sucesso!")
                        break
                    case 5:
                        print("\nVocê saiu com Sucesso!!")
                        break
                continuar = input("\nDeseja continuar S/N: ")

            else:
                print("\nUsuário não encontrado.")


def excluir_cadastro(dados):
    """Função para excluir cadastro do cliente na lista de vetor"""
    matricula = int(
        input("\nDigite o matricula do usuário que deseja Excluir: "))
    for usuario in dados:
        if usuario[0] == matricula:
            print(
                "Usuário encontrado. Escolha a opção abaixo para Excluir as informações do usuário:")
            continuar = "s"
            continuar = continuar.casefold()
            while continuar == 's':
                print("\nEscolha uma das opções abaixo:\n")
                print('''
                1 – Excluir ;\n
                2 - Sair.''')
                opcao = int(input("\nDigite uma opção para excluir ou sair: "))
                match opcao:
                    case 1:
                        for i, sub_list in enumerate(dados):
                            if matricula in sub_list:
                                del dados[i]
                                print(f"Updated list: {dados}")
                                break
                        else:
                            print("Value not found")
                    case 2:
                        print("\nVocê saiu com Sucesso!!")
                        break
                continuar = input(
                    "\nDeseja continuar a excluir usuários? S/N: ")
                while continuar.casefold() not in ['s', 'n']:
                    print(
                        "Entrada inválida. Por favor, digite 's' para continuar ou 'n' para sair.")
                    continuar = input(
                        "\nDeseja voltar para o menu inicial? S/N: ")
        else:
            print("\nUsuário não encontrado.")

        # meu_vetor = [1, 2, 3]
        # meu_vetor.remove(2)
        # print(meu_vetor)


def gera_relatorio(dados):
    """Função para gerar relatorio do cliente"""
    titulo_sistema("Relatório do cadastro do cliente")

    # Cria a lista com os títulos das colunas
    cabecalho = ["MATRICULA", "NOME", "APELIDO", "GÊNERO", "TELEFONE", "E-MAIL",
                 "ENDEREÇO", "Nº", "BAIRRO", "CIDADE",
                 "ESTADO", "CEP", "SENHA"]

    # Verifica se a lista dados está vazia
    if len(dados) == 0:
        # A lista dados está vazia
        # Aqui você pode tratar esse caso de maneira adequada
        print("A lista dados está vazia")
        return

    # Verifica se todas as linhas têm o mesmo número de colunas que a lista cabeçalho
    for linha in dados:
        if len(linha) != len(cabecalho):
            # Adiciona elementos vazios à linha
            linha.extend([""] * (len(cabecalho) - len(linha)))

    # Calcula a largura máxima de cada coluna
    largura_colunas = [max(len(str(dado)) for dado in coluna)
                       for coluna in zip(cabecalho, *dados)]

    # Imprime o cabeçalho da tabela
    for i, titulo in enumerate(cabecalho):
        print(f"{titulo: {largura_colunas[i]}}", end=" | ")
    print()

    # Imprime uma linha separadora
    for largura in largura_colunas:
        print("-" * largura, end="-+-")
    print()

    # Verifica se a lista largura_colunas tem o mesmo comprimento que a lista cabeçalho
    if len(largura_colunas) != len(cabecalho):
        print(
            f"Erro: A lista largura_colunas tem comprimento {
                len(largura_colunas)}, "
            f"mas deveria ter o mesmo comprimento que a lista cabeçalho ({len(cabecalho)})")

    else:
        # Imprime os dados da tabela
        for linha in dados:
            for dado, largura in zip(linha, largura_colunas):
                print(f"{dado: {largura}}", end=" | ")
            print()


def menu_opcao(dados_cadastrados):
    """Função criada para ser menu"""
    continuar = "s"
    while continuar == 's' or continuar == 'S':
        print("\nEscolha uma das opções abaixo:")
        print('''
        1 – Cadastro ;\n
        2 – Atualizar ;\n
        3 - Excluir;\n
        4 – Relatorio; \n
        5 - Sair.''')
        opcao = int(input("\nDigite uma opção para interagir: "))
        match opcao:
            case 1:
                dados_cadastrados = cadastro(dados_cadastrados)
            case 2:
                atualizar(dados_cadastrados)
            case 3:
                excluir_cadastro(dados_cadastrados)
            case 4:
                if not dados_cadastrados:
                    print("Nenhum usuário cadastrado.")
                else:
                    gera_relatorio(dados_cadastrados)
            case 5:
                print("\nVocê saiu com Sucesso!!")
                break
        continuar = input("\nDeseja voltar para o menu inicial? S/N: ")
        while continuar.casefold() not in ['s', 'n']:
            print("""Entrada inválida. Por favor, digite 's' para continuar
                   ou 'n' para sair.""")
            continuar = input("\nDeseja voltar para o menu inicial? S/N: ")


def app():
    """Função programa principal"""

    titulo_sistema("Programa de cadastro de cliente do Comércio Eletrônico.")
    # Armazena os dados do cadastro em uma variável
    dados_cadastrados = []

    # Chama a função menu_opcao passando os dados cadastrados como argumento
    menu_opcao(dados_cadastrados)


if __name__ == "__main__":
    app()
