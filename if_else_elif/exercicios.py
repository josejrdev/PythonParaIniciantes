qtdKWh = float(input("Digite a quantidade de KWh consumida: "))
tipoInstalacao = input("Digite o tipo de instalação: ")
if tipoInstalacao.lower() == "r":
    if qtdKWh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipoInstalacao.lower() == "c":
    if qtdKWh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipoInstalacao.lower() == "i":
    if qtdKWh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Digite uma categoria válida")
    preco = 0
calculoPreco = preco * qtdKWh
print(calculoPreco)