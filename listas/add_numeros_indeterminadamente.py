lista = []
while True:
    numero = int(input("Digite um número para adicionar a lista(0 sai): "))
    if numero == 0:
        break
    lista.append(numero)
for i in range(len(lista)):
    print("%d° número: %d" %(i+1, lista[i]))