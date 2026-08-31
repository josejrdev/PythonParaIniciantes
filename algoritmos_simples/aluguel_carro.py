# Algoritmo que calcula preço de aluguel de um carro.
# O carro custa R$60,00 por dia e R$0,15 por km 

kmPercorrido = float(input("Qual a quantidade de Km percorridos? ")) # Coleta do usuário o numero do usuario em km

diasAluguel = int(input("Quantos dias voce passou com o carro? "))  # Coleta do usuário os dias que o carro foi alugado

calculoPreco = (kmPercorrido * 0.15) + (diasAluguel * 60) # Calcula o valor do aluguel do carro

print("Você ficou com o carro %d dias, percorreu %.2f km, o valor a pagar é de R$%.2f" %(diasAluguel, kmPercorrido, calculoPreco)) # Exibe o resultado