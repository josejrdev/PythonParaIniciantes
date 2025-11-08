tempo = int(input("Digite o tempo em segundos inteiros: "))
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = (tempo % 3600) % 60
print("%02d:%02d:%02d" %(horas,minutos,segundos))