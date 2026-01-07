def novo_preco(p,taxa_desconto = 10):
  calc_novo_preco = p - (p * taxa_desconto / 100)
  return calc_novo_preco
preco_original = float(input("Digite o preço do produto: "))
print("O novo preço é: R$ %.2f" % novo_preco(preco_original))