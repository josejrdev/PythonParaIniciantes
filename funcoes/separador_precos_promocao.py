"""
Programa que percorre uma lista de preços e seleciona os produtos
com valor inferior a 800. Os preços que atendem a essa condição são
armazenados em uma nova lista e exibidos ao final.
"""
lista_precos = [1500,700,200,2500,600,300]
lista_precos_promocao = []
def promocao(preco):
  return preco < 800
for preco in lista_precos:
  if promocao(preco):
    lista_precos_promocao += [preco]
print(lista_precos_promocao)