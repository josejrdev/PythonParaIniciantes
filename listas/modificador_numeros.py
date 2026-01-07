numeros = [0,0,0,0,0]
for i in range(len(numeros)):
    numeros[i] = int(input("Adicione o %d° número: " %(i+1)))
opcao = int(input("Digite o número que deseja ver(1° ao 5°): "))
selecionador = numeros[opcao - 1]
print("Número %d - posição %d°" %(selecionador, opcao))