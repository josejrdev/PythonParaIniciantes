"""
Programa que simula o registro de compras de vários produtos.
Para cada produto, são armazenados seu nome, quantidade e preço
unitário em uma lista. A entrada é encerrada quando o usuário
digita "fim". Ao final, o programa exibe os dados de cada produto,
calcula o valor a pagar por cada item e soma o valor total da compra.
"""
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