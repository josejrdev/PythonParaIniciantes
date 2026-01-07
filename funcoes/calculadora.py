def calculadora(n_1, n_2, operacao):
  if operacao == "+":
    return soma(n_1, n_2)
  elif operacao == "-":
    return subtracao(n_1, n_2)
  elif operacao.lower() == "x":
    return multiplicacao(n_1, n_2)
  elif operacao == "/":
    return divisao(n_1, n_2)
def soma(n_1, n_2):
  calc_soma = n_1 + n_2
  return calc_soma
def subtracao(n_1, n_2):
  calc_subtracao = n_1 - n_2
  return calc_subtracao
def multiplicacao(n_1, n_2):
  calc_multiplicacao = n_1 * n_2
  return calc_multiplicacao
def divisao(n_1, n_2):
  if n_2 != 0:
    calc_divisao = n_1 / n_2
    return calc_divisao
  else:
    return "DIVISÃO POR ZERO"
numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar(+,-,x,/): ")
print(calculadora(numero_um, numero_dois, operacao))