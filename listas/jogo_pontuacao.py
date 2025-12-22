listaPontos = [10, 20, 30, 40, 20, 10]
listaPrimeiraMetade = listaPontos[0:3]
listaSegundaMetade = listaPontos[3:]
somaPrimeiraMetade = listaPrimeiraMetade[0] + listaPrimeiraMetade[1] + listaPrimeiraMetade[2]
somaSegundaMetade = listaSegundaMetade[0] + listaSegundaMetade[1] + listaSegundaMetade[2]
if somaPrimeiraMetade > somaSegundaMetade:
  print(f"A soma da primeira metade é maior.")
elif somaPrimeiraMetade == somaSegundaMetade:
  print(f"A soma das duas metades são iguais.")
else:
  print(f"A soma da segunda metade é maior.")