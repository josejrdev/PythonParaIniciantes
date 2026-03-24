peso_usuario = float(input("Digite o peso atual em quilos: "))
altura_usuario = float(input("Digite a altura atual em metros: "))
calc_imc = peso_usuario / altura_usuario ** 2
if calc_imc >= 40:
    print("Obesidade grau 3.")
elif calc_imc >= 35:
    print("Obesidade grau 2.")
elif calc_imc >= 30:
    print("Obesidade grau 1.")
elif calc_imc >= 25:
    print("Sobrepeso.")
elif calc_imc >= 18.5:
    print("Peso normal.")
else:
    print("Abaixo do peso.")