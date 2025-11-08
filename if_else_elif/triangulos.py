# Classificação dos triângulos pelos lados
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
if numero1 >= numero2 + numero3 or numero2 >= numero1 + numero3 or numero3 >= numero1 + numero2:
    print("Não forma triangulo.")
elif numero1 == numero2 == numero3:
    print("Equilatero.")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero1 or numero2 == numero3 or numero3 == numero1 or numero3 == numero2:
    print("Isosceles.")
else:
    print("Escaleno.")