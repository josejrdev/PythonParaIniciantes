lista_valores_inteiros_positivos = []
def verificar_parada(v,valor_parada=0):
  return v == valor_parada
def verificar_negativo(v,valor_comp=0):
  return v < 0
while True:
  valor = int(input("Digite o valor(Deve ser inteiro e positivo, 0 encerra): "))
  if verificar_parada(valor):
    break
  elif verificar_negativo(valor):
    print("Valor inválido, Digite um valor inteiro positivo.")
  else:
    lista_valores_inteiros_positivos.append(valor)
maior_valor = max(lista_valores_inteiros_positivos)
menor_valor = min(lista_valores_inteiros_positivos)
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")