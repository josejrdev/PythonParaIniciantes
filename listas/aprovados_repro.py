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