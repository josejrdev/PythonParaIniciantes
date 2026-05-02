codigoProduto = int(input("Digite o código do produto: "))
qtdCompradaProduto = int(input("Digite a quantidade de produtos comprada: "))
if codigoProduto >= 1 and codigoProduto <= 10:
  precoInicialProduto = 10
  precoInicialNota = precoInicialProduto * qtdCompradaProduto
elif codigoProduto >= 11 and codigoProduto <= 20:
  precoInicialProduto = 15
  precoInicialNota = precoInicialProduto * qtdCompradaProduto
elif codigoProduto >= 21 and codigoProduto <= 30:
  precoInicialProduto = 20
  precoInicialNota = precoInicialProduto * qtdCompradaProduto
elif codigoProduto >= 31 and codigoProduto <= 40:
  precoInicialProduto = 30
  precoInicialNota = precoInicialProduto * qtdCompradaProduto
if precoInicialNota <= 250:
  desconto = precoInicialNota * 5 / 100
  precoFinalNota = precoInicialNota - desconto
elif precoInicialNota > 250 and precoInicialNota <= 500:
  desconto = precoInicialNota * 10 / 100
  precoFinalNota = precoInicialNota - desconto
else:
  desconto = precoInicialNota * 15 / 100
  precoFinalNota = precoInicialNota - desconto
print(f"Preço unitário: R${precoInicialProduto:.2f}")
print(f"Preço total da nota R${precoInicialNota:.2f}")
print(f"Valor desconto: R${desconto:.2f}")
print(f"Preço Final da nota: R${precoFinalNota:.2f}")