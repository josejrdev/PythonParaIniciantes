distancia = float(input("Digite a distância a percorrer (em km): "))
velocidadeMedia = float(input("Digite a velocidade média esperada (em km/h): "))

tempo = distancia / velocidadeMedia  # tempo em horas
tempo_minutos = tempo * 60

print(f"\nTempo estimado de viagem:")
print(f"{tempo:.2f} horas ({tempo_minutos:.0f} minutos)")