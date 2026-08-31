"""
Algoritmo que lê quatro notas de um aluno, valida se cada nota está
entre 0 e 10, calcula a média das notas e informa se o aluno foi
aprovado ou reprovado de acordo com a média obtida.
"""

cont = 1
somaNotas = 0

while cont <= 4:
  nota = float(input("Digite a nota do aluno: "))
  while nota < 0 or nota > 10:
    nota = float(input("Nota inválida, digite a nota do aluno: "))
  somaNotas = somaNotas + nota
  cont = cont + 1
media = somaNotas / 4
if media >= 7:
  situacao = "Aprovado"
else:
  situacao = "Reprovado"
print(f"O aluno foi: {situacao}, a média foi de: {media:.2f}")