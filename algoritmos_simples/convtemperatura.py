# Programa que converte temperatura em Celsius para Fahrenheit e Kelvin

# Coletando tempo em Celsius
TempC = float(input("Celsius: "))

# Convertendo
CalcFa = (TempC * 1.8) + 32 # Fahrenheit
CalcKe = TempC + 273.15 # Kelvin

# Exibindo o resultado
print("A temperatura: " + str(TempC) + "°C é igual a: " + str(CalcFa) + "°F e " + str(CalcKe) + "K")