somaPrimeiraMetade = 0
somaSegundaMetade = 0
somaNotas = 0
listaNotas = []
listaNotasMaioresOuIguaisMedia = []
cont = 0
while cont < 12:
  nota = float(input(f"Digite a {cont + 1}° nota do aluno: "))
  listaNotas.append(nota)
  if cont < 6:
    somaPrimeiraMetade = somaPrimeiraMetade + nota
  else:
    somaSegundaMetade = somaSegundaMetade + nota
  somaNotas = somaNotas + nota
  cont = cont + 1
mediaPrimeiraMetade = somaPrimeiraMetade / 6
mediaSegundaMetade = somaSegundaMetade / 6
if mediaPrimeiraMetade > mediaSegundaMetade:
  print(f"A média {mediaPrimeiraMetade:.2f} da primeira metade foi maior.")
elif mediaPrimeiraMetade == mediaSegundaMetade:
  print(f"As médias {mediaPrimeiraMetade} e {mediaSegundaMetade} foram iguais.")
else:
  print(f"A média {mediaSegundaMetade} da segunda metade foi maior.")
mediaGeral = somaNotas / 12
cont = 0
while cont < len(listaNotas):
  if listaNotas[cont] >= mediaGeral:
    listaNotasMaioresOuIguaisMedia.append(listaNotas[cont])
  cont = cont + 1
print(f"Notas maiores ou iguais a {mediaGeral:.2f}(média geral): {listaNotasMaioresOuIguaisMedia}")