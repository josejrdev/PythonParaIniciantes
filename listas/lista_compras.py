compras = []
somaFinal = 0
while True:
    nomeProduto = input("Digite o nome do produto(fim sai): ")
    if nomeProduto.lower() == "fim":
        break
    quantidadeProduto = int(input("Digite a quantidade do produto: "))
    precoProduto = float(input("Digite o preço do produto: "))
    compras.append([nomeProduto, quantidadeProduto, precoProduto])
for p in compras:
    print("Nome:", p[0])
    print("Quantidade:", p[1])
    print("Preço da unidade: R$", p[2])
    print("Preço a pagar: R$ %.2f" % (p[2] * p[1]))
for p in compras:
    somaFinal = somaFinal + (p[2] * p[1])
print("Valor final a pagar: R$", somaFinal)