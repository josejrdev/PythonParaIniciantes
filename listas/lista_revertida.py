lista = [1,2,3,4,5]
cont = 0
while cont < 5:
    lista[cont] = int(input(f"Digite o {cont + 1}° número: "))
    cont = cont + 1
for i,v in enumerate(lista):
    if v % 2 == 0:
        print(f"{i+1}° número par = {v}")
    else:
        print(f"{i+1}° número impar = {v}")
revertida = list(reversed(lista))
print(revertida)