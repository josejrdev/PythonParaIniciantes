"""
Programa que solicita o nome de vários produtos e os armazena em uma
lista. A entrada de "fim", independentemente de letras maiúsculas ou
minúsculas, encerra o cadastro. Ao final, utiliza o fatiamento da lista
para obter e exibir os três primeiros produtos e os dois últimos
produtos cadastrados.
"""
listaCadastroProdutos = []
while True:
  produto = input("Digite o nome do produto(fim para encerrar): ")
  if produto.lower() == "fim":
    break
  listaCadastroProdutos.append(produto)
tresPrimeirosProdutos = listaCadastroProdutos[0:3]
doisUltimosProdutos = listaCadastroProdutos[-2:]
print(f"Os três primeiros produtos são: {tresPrimeirosProdutos}")
print(f"Os dois últimos produtos são: {doisUltimosProdutos}")