# multa se o o carro passar de 80km/h. R$5,00 a cada km passado
velocidadeCarro = int(input("Digite a velocidade do carro em km/h: "))
if velocidadeCarro > 80:
    precoMulta = (velocidadeCarro - 80) * 5
    print("Multado no valor %.2f" %precoMulta)
if velocidadeCarro == 80:
    print("No limite.")
if velocidadeCarro < 80:
    print("Abaixo do limite de velocidade de 80km/h")