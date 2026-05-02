cont = 0
lista_numeros = []
while cont < 10:
    numero = int(input(f"Digite o {cont + 1}° número: "))
    lista_numeros.append(numero)
    cont = cont + 1
for i,v in enumerate(lista_numeros):
    if v % 2 == 0:
        print(f"{i}° número par digitado: {v}")