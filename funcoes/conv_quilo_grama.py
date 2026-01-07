def conv_quilos_gramas(peso):
  conversor = peso * 1000
  return conversor
peso_usuario = float(input("Digite o seu peso: "))
print(f"Quilos: {peso_usuario:.2f} - Gramas: {conv_quilos_gramas(peso_usuario):.2f}")