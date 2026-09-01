"""
Programa que utiliza o fatiamento (slicing) de uma lista de vendas
para selecionar os três maiores valores, de acordo com as posições
previamente identificadas na lista. Ao final, exibe os três valores
selecionados.
"""
listaVendas = [120,330,290,800,150,90,1000]
tresMaioresValores = listaVendas[-1:] + listaVendas[-4:-3] + listaVendas[1:2]
print(f"Os três maiores valores são: {tresMaioresValores}")