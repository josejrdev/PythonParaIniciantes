qtdValores = 0
listaValores = []
while True:
    valor = int(input("Digite um valor inteiro e positivo(0 encerra): "))
    while valor == 0 and qtdValores == 0:
        print("Deve ter ao menos um valor")
        valor = int(input("Digite um valor inteiro e positivo(0 encerra): "))
    while valor < 0:
        print("Digite um valor positivo")
        valor = int(input("Digite um valor inteiro e positivo(0 encerra): "))
    if valor == 0 and qtdValores > 0:
        break
    listaValores.append(valor)
    qtdValores = qtdValores + 1
listaValores.sort()
maiorValor = listaValores[-1]
menorValor = listaValores[0]
print(f"O Maior valor é: {maiorValor}")
print(f"O Menor valor é: {menorValor}")