"""
Algoritmo que converte um peso informado pelo usuário em quilogramas
para gramas. O programa recebe o peso em quilogramas, utiliza uma
função para realizar a conversão e, ao final, exibe o peso original
em quilogramas e o valor correspondente em gramas.
"""

def conv_quilos_gramas(peso):
  conversor = peso * 1000
  return conversor

peso_usuario = float(input("Digite o seu peso: "))

print(f"Quilos: {peso_usuario:.2f} - Gramas: {conv_quilos_gramas(peso_usuario):.2f}")