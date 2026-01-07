notas = [0,0,0,0,0,0,0]
for i in range(len(notas)):
    notas[i] = float(input("Digite a %d° nota: " %(i+1)))
for i in range(len(notas)):
    print("%d° nota: %.2f" %(i+1, notas[i]))
media = sum(notas) / len(notas)
print("média: %.2f" %media)