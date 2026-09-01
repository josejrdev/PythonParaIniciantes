"""
Programa que solicita números inteiros ao usuário e os armazena em
uma lista. A entrada do valor 0 encerra a coleta de números. Ao final,
percorre a lista e exibe cada número juntamente com sua posição.
"""

lista = []
while True:
    numero = int(input("Digite um número para adicionar a lista(0 sai): "))
    if numero == 0:
        break
    lista.append(numero)
for i in range(len(lista)):
    print("%d° número: %d" %(i+1, lista[i]))