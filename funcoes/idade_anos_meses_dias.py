def idade_em_anos(a_n,a_a):
  calc_anos = a_a - a_n
  return calc_anos
def idade_em_meses(a_n,a_a):
  calc_meses = idade_em_anos(a_n,a_a) * 12
  return calc_meses
def idade_em_dias(a_n,a_a):
  calc_dias = idade_em_meses(a_n,a_a) * 30
  return calc_dias
def idade_em_semanas(a_n,a_a):
  calc_semanas = idade_em_dias(a_n,a_a) // 7
  return calc_semanas
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite a ano atual: "))
print(f"Idade em anos: {idade_em_anos(ano_nascimento,ano_atual)} anos.")
print(f"Idade em meses: {idade_em_meses(ano_nascimento,ano_atual)} meses.")
print(f"Idade em dias: {idade_em_dias(ano_nascimento,ano_atual)} dias.")
print(f"Idade em semanas: {idade_em_semanas(ano_nascimento,ano_atual)} semanas.")