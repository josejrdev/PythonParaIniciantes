# Programa que calcula Desconto de um produto

# Coleta o preço inicial
preco_inicial = float(input("Qual é o preço do produto? "))

# Coleta a porcentagem do desconto
porcentagem = float(input("Qual é o valor do desconto? "))

# Calcula o resultado
Calculo = (porcentagem / 100 * preco_inicial) - preco_inicial

# Exibe a saída
print("Valor Inicial: " + str(preco_inicial) + " Com desconto de " + str(porcentagem) + "% fica " + str(Calculo))