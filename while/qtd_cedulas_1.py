valorAPagar = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
while True:
    if atual <= valorAPagar:
        valorAPagar = valorAPagar - atual
        cedulas = cedulas + 1
    else:
        print(f"{cedulas} de {atual}")
        if valorAPagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0