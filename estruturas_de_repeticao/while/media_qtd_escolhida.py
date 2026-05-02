qtd_numeros = int(input("Digite a quantidade de números: "))
while qtd_numeros <= 0:
    print("Quantidade inválida.")
    qtd_numeros = int(input("Digite a quantidade de números: "))
cont = 1
lista_numeros = []
while qtd_numeros > 0:
    numero = float(input(f"Digite o {cont}° número: "))
    lista_numeros.append(numero)
    cont = cont + 1
    qtd_numeros = qtd_numeros - 1
media_numeros = sum(lista_numeros) / len(lista_numeros)
print(media_numeros)