valorAPagar = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
while True:
    # margem pequena para evitar erros com floats
    if atual <= valorAPagar + 0.001:
        valorAPagar = valorAPagar - atual
        cedulas = cedulas + 1
    else:
        if cedulas > 0:  # imprime apenas se houve pelo menos 1 cédula/moeda desse valor
            print(f"{cedulas} de R$ {atual:.2f}")
        if valorAPagar < 0.001:  # condição de parada com margem
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0