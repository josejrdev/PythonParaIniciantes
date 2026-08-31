# Algoritmo que converte um valor de metros para centrimentros e para milimetros

valor_metros = float(input("Digite o valor em metros: ")) # Coleta do usuário o valor em metros

conv_centimetros = valor_metros * 100 # Converte para centimetros

conv_milimetros = valor_metros * 1000 # Converte para milimetros

# Exibindo o resultado
print(f"{valor_metros} metros tem {conv_centimetros} centimetros.")
print(f"{valor_metros} metros tem {conv_milimetros} milimetros.")