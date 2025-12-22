listaPlacas = [
  "JKP-2A91", "MQT-7C03", "LBD-4F62", "ZHR-0K58",
  "QVW-9L10", "FSP-1B74", "ARM-6D22", "CXA-3E45",
  "VNJ-8H01","KGL-5J77", "PRX-9M34", "YSU-2N51",
  "ADF-0P96", "ATB-4Q20", "BNO-7R83", "EKM-3S14",
  "RZU-1T69", "GQC-5U02", "UJL-6V37", "NHA-8W98",
  "DYP-9X41", "AFV-0Y55", "ARR-4Z26", "JLX-7A63",
  "MVR-2C08", "LKT-5F72","ZQC-1G99", "QDB-3H27",
  "FNM-8J80", "TWR-6L54", "AOC-99B2", "AFC-0022"
]
lista10PrimeirasPlacas = listaPlacas[0:10]
lista10UltimasPlacas = listaPlacas[-10:]
listaPlacasIniciamLetraA = []
listaPlacasTerminamNumeroPar = []
cont = 0
while cont < len(listaPlacas):
  if listaPlacas[cont][0] == "A":
    listaPlacasIniciamLetraA.append(listaPlacas[cont])
  if int(listaPlacas[cont][-1]) % 2 == 0:
    listaPlacasTerminamNumeroPar.append(listaPlacas[cont])
  cont = cont + 1
print(f"As 10 primeiras placas são: {lista10PrimeirasPlacas}")
print(f"As 10 últimas placas são: {lista10UltimasPlacas}")
print(f"As placas que começam com a letra A são: {listaPlacasIniciamLetraA}")
print(f"As placas que terminam em número par são: {listaPlacasTerminamNumeroPar}")