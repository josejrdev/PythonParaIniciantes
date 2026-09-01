"""
Programa que solicita 10 números inteiros ao usuário e os armazena
em uma lista. Em seguida, percorre a lista para identificar o maior
e o menor número informado e, ao final, exibe os dois valores.
"""
cont = 1
lista_numeros = []
while cont <= 10:
    numero = int(input(f"Digite o {cont}° número: "))
    lista_numeros.append(numero)
    cont = cont + 1
maior_numero = lista_numeros[0]
menor_numero = lista_numeros[0]
for numero in lista_numeros:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
print(maior_numero, menor_numero)