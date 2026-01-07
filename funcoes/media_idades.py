lista_idades = []
qtd_pessoas = 1
def verificar_parada(n):
  return n == 0
def verificar_validade(n):
  return n < 0
def media(soma,vezes):
  calc_media = soma / vezes
  return calc_media
while True:
  print("Digite as idades, 0 encerra o programa.")
  idade = int(input(f"Digite a idade da {qtd_pessoas}° pessoa: "))
  while verificar_validade(idade):
    print("Idade inválida, digite um valor válido.")
    idade = int(input(f"Digite a idade da {qtd_pessoas}° pessoa: "))
  if verificar_parada(idade):
    break
  lista_idades.append(idade)
  qtd_pessoas = qtd_pessoas + 1
media_idades = media(sum(lista_idades),qtd_pessoas)
print(f"A média de idade das pessoas é: {media_idades:.2f}")