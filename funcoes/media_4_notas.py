def media_aritmetica(nota_1,nota_2,nota_3,nota_4):
  media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
  if media >= 7:
    return "Aprovado"
  else:
    return "Reprovado"
nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))
nota_quatro = float(input("Digite a quarta nota: "))
print(media_aritmetica(nota_um,nota_dois,nota_tres,nota_quatro))