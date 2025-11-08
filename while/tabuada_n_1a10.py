numero = 1
cont = 1
while numero <= 10:
  print(f"Tabuada do número {numero}")
  while cont <= 10:
    tabResultado = numero * cont
    print(f"{numero} x {cont} = {tabResultado}")
    cont = cont + 1
  cont = 1
  numero = numero + 1