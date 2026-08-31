""" 
Algoritmo que informa se um carro é novo ou velho de acordo com a sua idade
"""

# Coleta do usuário a idade do carro
idadeCarro = int(input("Digite a idade do seu carro: "))

# Informando se o carro é novo ou velho (<= 3 é novo), (> 3 é velho).
if idadeCarro <= 3:
    print("Carro Novo!")
if idadeCarro > 3:
    print("Carro Velho!")