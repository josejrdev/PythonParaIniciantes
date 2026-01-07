def peso_taxa_engor(p, taxa=15):
  calc_peso_engordado = p * taxa / 100
  return calc_peso_engordado
def peso_taxa_emag(p, taxa=20):
  calc_peso_emagrecido = p * taxa / 100
  return calc_peso_emagrecido
def peso_se_engordar(p):
  calc_peso = p + peso_taxa_engor(p)
  return calc_peso
def peso_se_emagrecer(p):
  calc_peso = p - peso_taxa_emag(p)
  return calc_peso
peso_atual = float(input("Digite o seu peso atual: "))
print(f"Se você engordar 15% seu novo peso será: {peso_se_engordar(peso_atual):.2f} quilos")
print(f"Se você emagrecer 20% seu novo peso será: {peso_se_emagrecer(peso_atual):.2f} quilos")