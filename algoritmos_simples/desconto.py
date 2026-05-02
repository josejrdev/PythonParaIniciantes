# Programa que calcula Desconto
# Preço inicial
PrecoInicial = float(input("Qual é o preço do produto? "))
# Porcentagem do desconto
Porcentagem = float(input("Qual é o valor do desconto? "))
# Calculo
Calculo = (Porcentagem / 100 * PrecoInicial) - PrecoInicial
print("Valor Inicial: " + str(PrecoInicial) + " Com desconto de " + str(Porcentagem) + "% fica " + str(Calculo))