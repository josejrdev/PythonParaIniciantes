codigoProduto = int(input("Digite o código do produto: "))
qtdComprada = int(input("Digite a quantidade comprada: "))
if codigoProduto >= 1 and codigoProduto <= 10:
    precoProduto = 10
    acumuladorNota = precoProduto * qtdComprada
elif codigoProduto >= 11 and codigoProduto <= 20:
    precoProduto = 15
    acumuladorNota = precoProduto * qtdComprada
elif codigoProduto >= 21 and codigoProduto <= 30:
    precoProduto = 20
    acumuladorNota = precoProduto * qtdComprada
elif codigoProduto >= 31 and codigoProduto <= 40:
    precoProduto = 30
    acumuladorNota = precoProduto * qtdComprada
else:
    print("Código de produto inválido.")
    precoProduto = 0
    acumuladorNota = 0
if acumuladorNota <= 250:
    valorDesconto = 5
    valorFinalNota = acumuladorNota - (acumuladorNota * valorDesconto / 100)
elif acumuladorNota > 250 and acumuladorNota <= 500:
    valorDesconto = 10
    valorFinalNota = acumuladorNota - (acumuladorNota * valorDesconto / 100)
else:
    valorDesconto = 15
    valorFinalNota = acumuladorNota - (acumuladorNota * valorDesconto / 100)
print(f"Preço unitário do produto: R$ {precoProduto:.2f}")
print(f"Valor final da nota sem desconto: R$ {acumuladorNota:.2f}")
print(f"Valor do desconto: {valorDesconto}%")
print(f"Valor final da nota após o desconto: R$ {valorFinalNota:.2f}")