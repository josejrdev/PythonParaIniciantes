cont1 = 1
cont2 = 1
numero = 1
while cont1 <= 10:
  cont2 = 1
  print(f"Tabuada do {numero}:")
  while cont2 <= 10:
    tabuada = numero * cont2
    print(f"{numero} x {cont2} = {tabuada}")
    cont2 = cont2 + 1
  numero = numero + 1
  cont1 = cont1 + 1