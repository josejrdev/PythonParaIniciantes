n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? ")
calculo = 0
if operacao == "+":
    calculo = n1 + n2
elif operacao == "-":
    calculo = n1 - n2
elif operacao == "*":
    calculo = n1 * n2
elif operacao == "/":
    if n2 != 0:
        calculo = n1 / n2
    else:
        calculo = 0
else:
    print("Operação inválida.")
print(f"Resultado: {calculo}")