# Algoritmo que converte reais em dólar

# Coleta do usuário o valor em Reais
valor_real = float(input("Digite o valor em Reais: ")) 

# Cotação 
cotacao_dolar = 0.19

# Converte de Reais para dólar
conv_dolar = valor_real * cotacao_dolar

# Exibe a o resultado
print(f"{valor_real:.2f} Reais = {conv_dolar:.2f} Dólares")