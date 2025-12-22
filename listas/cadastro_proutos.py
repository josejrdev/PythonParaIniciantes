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