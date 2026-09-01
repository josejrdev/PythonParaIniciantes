def calculo_nota(n_1, n_2):
  calc_media = (n_1 + n_2) / 2
  return resultado_final(calc_media)
def resultado_final(media):
  if media >= 7:
    return "Aprovado"
  else:
    return "Desaprovado"
nota_1 = float(input("Digite a nota da primeira unidade: "))
nota_2 = float(input("Digite a nota da segunda unidade: "))
print(f"Aluno", calculo_nota(nota_1, nota_2))