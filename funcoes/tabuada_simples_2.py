def resultado(numero, cont):
  calc = numero * cont
  return calc
numero = int(input("Tabuada do número: "))
cont = 1
print(f"Tabuda do número {numero}")
while cont <= 10:
  print(f"{numero} x {cont} = {resultado(numero,cont)}")
  cont = cont + 1