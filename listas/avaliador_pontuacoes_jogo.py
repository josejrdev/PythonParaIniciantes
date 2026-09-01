"""
Programa que utiliza o fatiamento (slicing) de listas para selecionar
as quatro maiores e as duas menores pontuações de uma lista. Os valores
são obtidos a partir de suas posições na lista e armazenados em novas
listas, que são exibidas ao final.
"""
listaPontos = [100, 80, 150, 40, 120, 90]
lista4Maiores = listaPontos[2:3] + listaPontos[4:5] + listaPontos[0:1] + listaPontos[-1:]
lista2Menores = listaPontos[3:4] + listaPontos[1:2]
print(f"As quatro maiores pontuações foram: {lista4Maiores}")
print(f"As duas menores pontuações foram: {lista2Menores}")