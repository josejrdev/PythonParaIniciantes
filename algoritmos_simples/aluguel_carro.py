# carro custa R$60,00 por dia e R$0,15 por km 
kmPercorrido = float(input("Qual a quantidade de Km percorridos? ")) # numero do usuario em km
diasAluguel = int(input("Quantos dias voce passou com o carro? "))  # dias que o carro foi alugado
calculoPreco = (kmPercorrido * 0.15) + (diasAluguel * 60) # calculando o preço do carro
print("Você ficou com o carro %d dias, percorreu %.2f km, o valor a pagar é de R$%.2f" %(diasAluguel, kmPercorrido, calculoPreco))