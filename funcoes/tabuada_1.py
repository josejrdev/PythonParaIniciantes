def tabuada(numero,cont):
  resultado = numero * cont
  return (f"{numero} x {cont} = {resultado}")
numero = int(input("Tabuda do número: "))
cont = 1
print(f"Tabuda do número {numero}")
while cont <= 10:
  print(tabuada(numero,cont))
  cont = cont + 1