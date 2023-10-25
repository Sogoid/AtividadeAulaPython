"""Finalidade: Cálculo de Notas dos Alunos de Umas Instituição de Ensino
autor: Diogo da Silveira Ribeiro
data: 02/04/2023
Versão: 0.2
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
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


def calculo_media(__n1__, __n2__):
    """Função para calcular a Média"""
    __media__ = (__n1__ + __n2__) / 2
    return __media__


def titulo_relatorio(tmsg):
    """Função para mostrar o título dos relatorios."""
    print(f"\n{tmsg}\n")


titulo_sistema("Sistema de notas escolares.")

titulo_sistema("Informe as notas do Aluno.")

matricula = int(input("Matricula do aluno => "))
nome = input("Nome do aluno => ")
curso = input("Nome do Curso => ")
instituicao = "IPOG - INSTITUIÇÃO DE PÓS-GRADUÇÃO & GRADUAÇÃO"
print(f"Instituição => {instituicao}")

n1 = float(input("Entre com a nota da N1 => "))
n2 = float(input("Entre com a nota da N2 => "))

media = calculo_media(n1, n2)

if 4.0 < media < 7.0:

    titulo_relatorio(f"Aluno esta de Recuperação nota => {media}")

    titulo_sistema("\N{SNAKE} INICIO DA PROVA FINAL")

    pf = float(input("Entre com a nota da prova final => "))

    pfm = (pf + media) / 2

    if pfm >= 5.0:
        print(f"\n\N{SNAKE} Aluno aprovado com nota => {pfm}\n")

    else:
        print(f"\n\N{SNAKE} Aluno reprovado com nota => {pfm}\n")
        while True:
            try:
                ponto_extra = input("Quer dar 1 ponto extra! SIM OU NÃO => ")
                if ponto_extra != "":
                    break
            except ValueError:
                print("Escolha uma opção SIM ou NÃO.")

        ponto_extra = ponto_extra.upper()
        ponto_extra = ponto_extra.strip()

        if ponto_extra == "SIM":
            pfm = pfm + 1
            if pfm >= 5.0:
                print(f"\n\N{SNAKE} Aluno aprovado com nota => {pfm}\n")
            else:
                print(f"\n\N{SNAKE} Aluno reprovado com nota => {pfm}\n")

elif media >= 7.0:
    print(f"\n\N{SNAKE} Aluno aprovado com nota => {media}\n")

else:
    print(f"\n\N{SNAKE} Aluno reprovado com nota => {media}\n")
