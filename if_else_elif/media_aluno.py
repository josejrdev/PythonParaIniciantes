nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
  print("Aprovado")
elif media >= 2 and media < 7:
  print("Final")
  notaFinal = float(input("Digite a nota da prova final: "))
  if notaFinal >= 5:
    print("Aprovado na final")
  else:
    print("Reprovado na final")
else:
  print("Reprovado")