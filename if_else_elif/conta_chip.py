minutosFalados = int(input("Digite os minutos falados: "))
if minutosFalados <= 200:
    calcConta = minutosFalados * 0.20
elif minutosFalados > 200 and minutosFalados <= 400:
    calcConta = minutosFalados * 0.18
else:
    calcConta = minutosFalados * 0.15
print("A conta deu: R$%.2f" %calcConta)