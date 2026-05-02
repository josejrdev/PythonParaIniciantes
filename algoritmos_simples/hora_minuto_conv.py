hora = int(input("Digite o tempo em horas: "))
minuto = int(input("Digite o tempo em minutos: "))
convHoraMinuto = hora * 60
totalMinuto = minuto + convHoraMinuto
convMinutoSegundo = totalMinuto * 60
print(f"Hora em minutos {convHoraMinuto}, total de minutos: {totalMinuto}, minutos em segundos: {convMinutoSegundo}")