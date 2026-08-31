# Algoritmo que converte um tempo de horas para minutos, calcula o total em minutos e converte de minutos para segundos

# Coleta o tempo em horas do usuário
horas = int(input("Digite o tempo em horas: "))

# Coleta o tempo em minutos
minutos = int(input("Digite o tempo em minutos: "))

# Converte horas em minutos
conv_horas_minutos = horas * 60

# Calculando o total de minutos
total_minutos = minutos + conv_horas_minutos

# Converte o total de minutos em segundos
conv_minutos_segundos = total_minutos * 60

# Exibe o resultado
print(f"Hora em minutos {conv_horas_minutos}, total de minutos: {total_minutos}, minutos em segundos: {conv_minutos_segundos}")