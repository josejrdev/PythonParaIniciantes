"""
Algoritmo que converte um tempo informado em segundos inteiros
para o formato de horas, minutos e segundos.
"""

# Coleta do usuário um tempo inteiro em segundos
tempo_s_i = int(input("Digite o tempo em segundos inteiros: "))

# Obtém a quantidade de horas inteiras do tempo informado
calc_horas = tempo_s_i // 3600

# Obtém os minutos restantes após retirar as horas completas
calc_minutos = (tempo_s_i % 3600) // 60

# Obtém os segundos restantes após retirar as horas e os minutos
calc_segundos = (tempo_s_i % 3600) % 60

# Exibe o resultado
print("%02d:%02d:%02d" % (calc_horas, calc_minutos, calc_segundos))