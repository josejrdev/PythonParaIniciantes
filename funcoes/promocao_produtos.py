lista_precos = [1500,700,200,2500,600,300]
lista_precos_promocao = []
def promocao(preco):
  return preco < 800
for preco in lista_precos:
  if promocao(preco):
    lista_precos_promocao += [preco]
print(lista_precos_promocao)