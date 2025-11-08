consumoKwh = float(input("Digite a quantidade de Kwn consumida: "))
tipoInstalacao = input("Digite o tipo de instalação: ")
if tipoInstalacao.lower() == "r":
    if consumoKwh <= 500:
        calcPreco = consumoKwh * 0.40
    else:
        calcPreco = consumoKwh * 0.65
    print("Preço a pagar R$%.2f" %calcPreco)
elif tipoInstalacao.lower() == "c":
    if consumoKwh <= 1000:
        calcPreco = consumoKwh * 0.55
    else:
        calcPreco = consumoKwh * 0.60
    print("Preço a pagar R$%.2f" %calcPreco)
elif tipoInstalacao.lower() == "i":
    if consumoKwh <= 5000:
        calcPreco = consumoKwh * 0.55
    else:
        calcPreco = consumoKwh * 0.60
    print("Preço a pagar R$%.2f" %calcPreco)
else:
    print("Tipo de instação inválido.")