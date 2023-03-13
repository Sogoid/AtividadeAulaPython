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

if media == 4.0 and media > 4.0 and media < 7.5:
    print(f"Aluno esta de Recuperação nota => {media}")
    print("\n***INICIO DA PROVA FINAL***\n")
    pf = float(input("Entre com a nota da prova final => "))
    
    if pf == 7.5 or pf > 7.5:
        print(f"Aluno aprovado com nota => {pf}")

elif media == 7.5 or media > 7.5:
    print(f"Aluno aprovado com nota => {media}")
else:
    print(f"Aluno reprovado com nota => {media}")
