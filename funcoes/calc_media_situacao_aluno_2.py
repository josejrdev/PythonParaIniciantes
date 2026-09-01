def boletim(n_1,n_2):
  calc_media = (n_1 + n_2) / 2
  return situacao_aluno(calc_media)
def situacao_aluno(media):
  if media >= 7:
    return "Aprovado."
  elif media >= 2:
    return calc_prova_final(media)
  else:
    return "Reprovado, sem direito a final."
def calc_prova_final(media):
  nota_na_final = float(input("Digite a nota na prova final: "))
  media_apos_final = (nota_na_final + media) / 2
  return situacao_aluno_apos_final(media_apos_final)
def situacao_aluno_apos_final(media_a_f):
  if media_a_f >= 5:
    return "Aprovado na final."
  else:
    return "Reprovado na final."
nota_1 = float(input("Digite a nota da primeira unidade: "))
nota_2 = float(input("Digite a nota da segunda unidade: "))
print("Situação do aluno:",boletim(nota_1,nota_2))