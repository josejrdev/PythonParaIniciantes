final = int(input("Digite o número final: "))
cont = 1
while cont <= final:
    if cont % 2 == 0:
        print(cont, "Par")
    else:
        print(cont, "Impar")
    cont += 1