n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar: ")
if operacao == "+":
  calc = n1 + n2
  print(calc)
elif operacao == "-":
  calc = n1 - n2
  print(calc)
elif operacao == "*":
  calc = n1 * n2
  print(calc)
elif operacao == "/" and n2 != 0:
  calc = n1 / n2
  print(calc)
elif operacao == "/" and n2 == 0:
  print("Divisão por zero.")
else:
  print("Operação Inválida.")