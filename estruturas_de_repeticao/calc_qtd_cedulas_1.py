"""
Algoritmo que calcula a quantidade de cédulas necessárias para representar
um valor a pagar, utilizando cédulas de 100, 50, 20, 10, 5 e 1 reais.
O programa utiliza a maior cédula possível a cada etapa, subtraindo seu
valor do total a pagar até que não seja mais possível utilizá-la. Ao final
de cada etapa, exibe a quantidade de cédulas utilizadas de cada valor.
"""

valorAPagar = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100

while True:
    if atual <= valorAPagar:
        valorAPagar = valorAPagar - atual
        cedulas = cedulas + 1
    else:
        print(f"{cedulas} de {atual}")
        if valorAPagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0