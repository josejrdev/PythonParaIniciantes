"""
Algoritmo que exibe as tabuadas dos números de 1 a 10.
O programa utiliza dois laços de repetição, sendo um para percorrer
os números de 1 a 10 e outro para realizar e exibir as multiplicações
de cada número também de 1 a 10.
"""

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