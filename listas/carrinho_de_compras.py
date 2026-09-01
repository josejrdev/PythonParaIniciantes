"""
Programa que manipula uma lista de produtos de um e-commerce.
Remove os três últimos produtos da lista, adiciona dois novos
produtos (processador e SSD) e, ao final, exibe a lista atualizada.
"""
listaEcommerce = ["mouse", "fone", "teclado", "cabo", "hub", "mousepad"]
del listaEcommerce[-3:]
listaEcommerce.append("processador")
listaEcommerce.append("SSD")
print(listaEcommerce)