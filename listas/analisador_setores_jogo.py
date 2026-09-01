"""
Programa que divide uma lista de recursos em duas listas, representando
dois setores, utilizando o fatiamento com passo 2. Em seguida, calcula
a soma dos recursos de cada setor e compara os resultados para identificar
qual dos dois setores possui a maior soma.
"""
listaRecursos = [40, 20, 10, 50, 60, 15, 5, 30]
listaPrimeiroSetor = listaRecursos[0::2]
listaSegundoSetor = listaRecursos[1::2]
somaPrimeiroSetor = 0
somaSegundoSetor = 0
cont = 0
while cont < len(listaPrimeiroSetor):
  somaPrimeiroSetor = somaPrimeiroSetor + listaPrimeiroSetor[cont]
  cont = cont + 1
cont = 0
while cont < len(listaSegundoSetor):
  somaSegundoSetor = somaSegundoSetor + listaSegundoSetor[cont]
  cont = cont + 1
if somaPrimeiroSetor > somaSegundoSetor:
  print(f"O Primeiro setor tem a maior soma.")
else:
  print(f"O Segundo setor tem a maior soma.")