def media_aritmetica(n_1, n_2):
  calc_media = (n_1 + n_2) / 2
  return calc_media
def situacao_aluno():
  media = media_aritmetica(nota_1, nota_2)
  if media >= 7:
    print("Aprovado")
  elif media >= 4:
    print("Final")
  else:
    print("Reprovado")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
print(situacao_aluno())