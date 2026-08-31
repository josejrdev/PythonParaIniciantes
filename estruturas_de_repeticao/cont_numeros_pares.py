cont = 0
lista_numeros = []
qtd_numeros = int(input("Quantidade de números: "))
cont = 0

while qtd_numeros <= 0:
    print("Quantidade de números inválida.")
    qtd_numeros = int(input("Quantidade de números:"))

while cont < qtd_numeros:
    numero = int(input(f"{cont + 1}° número: "))
    lista_numeros.append(numero)
    cont = cont + 1

for i,v in enumerate(lista_numeros):
    if v % 2 == 0:
        print(f"O {i + 1}° número é par = {v}")



        