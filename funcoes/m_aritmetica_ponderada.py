lista_notas_pesos = []
lista_notas = []
def verificar_parada(n):
  return n == 3
def media_ponderada_lista(lista):
  calc_media_ponderada = ((lista[0] * lista[1]) + (lista[2] * lista[3]) + (lista[4] * lista[5])) / (lista[1] + lista[3] + lista[5])
  return calc_media_ponderada
def media_aritmetica_lista(lista,qtd_notas):
  calc_media_aritmetica = (lista[0] + lista[1]) / qtd_notas
  return calc_media_aritmetica
while True:
  print("Menu de opções e seus respectivos códigos")
  print("Média aritmética: 1 | Média ponderada: 2 | Sair: 3")
  opcao_usuario = int(input("Digite a opção desejada: "))
  if verificar_parada(opcao_usuario):
    break
  elif opcao_usuario == 2:
    cont = 1
    while cont <= 3:
      nota = float(input(f"Digite a {cont}° nota: "))
      peso = float(input(f"Digite o peso da {cont}° nota: "))
      lista_notas_pesos.append(nota)
      lista_notas_pesos.append(peso)
      cont = cont + 1
    media_ponderada = media_ponderada_lista(lista_notas_pesos)
    print(f"A média ponderada é {media_ponderada:.2f}")
    lista_notas_pesos = []
  elif opcao_usuario == 1:
    cont = 1
    while cont <= 2:
      nota = float(input(f"Digite a {cont}° nota: "))
      lista_notas.append(nota)
      cont = cont + 1
    media_aritmetica = media_aritmetica_lista(lista_notas,len(lista_notas))
    print(f"A média aritmética é {media_aritmetica:.2f}")
    lista_notas = []
  else:
    print("Opção inválida.")