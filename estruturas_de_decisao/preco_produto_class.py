precoProduto = float(input("Digite o preço do produto: "))
if precoProduto <= 50:
  calcAumento = precoProduto + (precoProduto * 5 / 100)
elif precoProduto > 50 and precoProduto <= 100:
  calcAumento = precoProduto + (precoProduto * 10 / 100)
else:
  calcAumento = precoProduto + (precoProduto * 15 / 100)
if calcAumento <= 80:
  classificacao = "Barato"
elif calcAumento > 80 and calcAumento <= 120:
  classificacao = "Normal"
elif calcAumento > 120 and calcAumento <= 200:
  classificacao = "Caro"
else:
  classificacao = "Muito Caro"
print(f"Preço: R${calcAumento:.2f} Classificação: {classificacao}")