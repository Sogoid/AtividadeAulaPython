"""Finalidade: Cálculo de Notas dos Alunos de Umas Instituição de Ensino
autor: Diogo da Silveira Ribeiro
data: 13/03/2023
Versão: 0.1
Python versão: 3.10.9
Link do repositório no GitHub para analisar o código
 -> https://github.com/Sogoid/AtividadeAulaPython
"""

print(
    "\n*********** Sistema de notas escolares. *************\n"
    "*********** Informe as notas do Aluno. **************\n"
)

n1 = float(input("Entre com a nota da N1 => "))
n2 = float(input("Entre com a nota da N2 => "))
n3 = float(input("Entre com a nota da N3 => "))

media = (n1 + n2 + n3) / 3

if media > 4.0 and media < 7.5:

    print(f"\nAluno esta de Recuperação nota => {media}")

    print("\n\N{SNAKE} INICIO DA PROVA FINAL \N{SNAKE}\n")

    pf = float(input("Entre com a nota da prova final => "))

    pfm = (pf + media) / 2

    if pfm == 7.5 or pfm > 7.5:
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
            if pfm >= 7.5:
                print(f"\n\N{SNAKE} Aluno aprovado com nota => {pfm}\n")
            else:
                print(f"\n\N{SNAKE} Aluno reprovado com nota => {pfm}\n")

elif media == 7.5 or media > 7.5:
    print(f"\n\N{SNAKE} Aluno aprovado com nota => {media}\n")

else:
    print(f"\n\N{SNAKE} Aluno reprovado com nota => {media}\n")
