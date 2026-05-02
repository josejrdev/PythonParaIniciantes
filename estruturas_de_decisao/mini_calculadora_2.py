numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segunda número: "))
escolha = input("Qual operação deseja realizar? ")
if escolha == "1":
  calcMedia = (numero1 + numero2) / 2
  print(calcMedia)
elif escolha == "2":
  if numero1 > numero2:
    print(numero1 - numero2)
  elif numero2 > numero1:
    print(numero2 - numero1)
elif escolha == "3":
  calcPro = numero1 * numero2
  print(calcPro)
elif escolha == "4":
  calcDiv = numero1 / numero2
  print(calcDiv)
else:
  print("Você digitou uma operação inválida.")