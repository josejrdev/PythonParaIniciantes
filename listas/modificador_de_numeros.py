"""
Programa que solicita cinco números inteiros ao usuário e os armazena
em uma lista. Em seguida, solicita uma posição de 1 a 5 e utiliza essa
posição para selecionar e exibir o número correspondente da lista.
"""
numeros = [0,0,0,0,0]
for i in range(len(numeros)):
    numeros[i] = int(input("Adicione o %d° número: " %(i+1)))
opcao = int(input("Digite o número que deseja ver(1° ao 5°): "))
selecionador = numeros[opcao - 1]
print("Número %d - posição %d°" %(selecionador, opcao))