"""
Programa que divide uma lista original em três partes, inverte a
ordem dos elementos de cada parte e, em seguida, recombina as três
listas invertidas em uma única lista. Ao final, exibe a lista
resultante da recombinação.
"""
listaOriginal = [
  "Zx9", "zy42", "*&%@@", "A_D_S@@",
  "1**P", "55%%", "P@ALMARES666", "89##",
  "if1fpe", "ghhw&&", "sys$&**", "%%%t*i"
]
listaPrimeiraParte = listaOriginal[0:4]
listaSegundaParte = listaOriginal[4:8]
listaTerceiraParte = listaOriginal[8:]
listaPrimeiraParte.reverse()
listaSegundaParte.reverse()
listaTerceiraParte.reverse()
ListaRecombinada = listaPrimeiraParte + listaSegundaParte + listaTerceiraParte
print(ListaRecombinada)