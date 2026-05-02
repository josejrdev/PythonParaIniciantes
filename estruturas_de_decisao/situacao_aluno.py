nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
calcMedia = (nota1 + nota2) / 2
if calcMedia >= 7.0:
    print("Aluno aprovado!")
elif calcMedia >= 4.0 and calcMedia <= 6.9:
    print("Recuperação.")
else:
    print("Reprovado")