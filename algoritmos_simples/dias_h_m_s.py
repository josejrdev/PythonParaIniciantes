# Programa que converte dias, horas, minutos e segundos para segundos

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Conversão
totalSegundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"O total em segundos é: {totalSegundos}")
