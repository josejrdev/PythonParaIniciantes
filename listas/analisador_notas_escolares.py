"""
Programa que percorre uma lista de notas e separa os valores em duas
listas de acordo com a situação do aluno. Notas maiores ou iguais a 7
são armazenadas na lista de aprovados, enquanto notas menores que 7
são armazenadas na lista de reprovados. Ao final, exibe as duas listas.
"""

listaNotas = [8, 5, 9, 3, 4, 7]
listaNotasAprovados = []
listaNotasReprovados = []
for i in range(len(listaNotas)):
  if listaNotas[i] >= 7:
    listaNotasAprovados.append(listaNotas[i])
  else:
    listaNotasReprovados.append(listaNotas[i])
print(f"Lista de notas maiores ou iguais a 7: {listaNotasAprovados}")
print(f"Lista de notas menores que 7: {listaNotasReprovados}")