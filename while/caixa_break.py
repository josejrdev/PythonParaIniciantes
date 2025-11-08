valorFinal = 0
calc = 0
while True:
    codigoProduto = int(input("Digite o código do produto: "))
    if codigoProduto == 0:
        break
    qtdComprada = int(input("Digite a quantidade comprada: "))
    if codigoProduto == 1:
        preco = 0.50
        calc = preco * qtdComprada
        valorFinal = valorFinal + calc
    elif codigoProduto == 2:
        preco = 1.00
        calc = preco * qtdComprada
        valorFinal = valorFinal + calc
    elif codigoProduto == 3:
        preco = 4.00
        calc = preco * qtdComprada
        valorFinal = valorFinal + calc
    elif codigoProduto == 5:
        preco = 7.00
        calc = preco * qtdComprada
        valorFinal = valorFinal + calc
    elif codigoProduto == 9:
        preco = 8.00
        calc = preco * qtdComprada
        valorFinal = valorFinal + calc
    else:
        print("Código inválido.")
print(f"R${valorFinal:.2f}")