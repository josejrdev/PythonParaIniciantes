"""
Programa que solicita o nome de vários produtos e os armazena em uma
lista. A entrada de "fim", independentemente de letras maiúsculas ou
minúsculas, encerra o cadastro. Ao final, exibe os produtos numerados,
os três primeiros produtos e os dois últimos produtos da lista.
"""
lista_produtos = []
def verificar_parada(valor):
  return valor.lower() == "fim"
while True:
  produto = input("Digite o nome do produto: ")
  if verificar_parada(produto):
    break
  lista_produtos.extend([produto])
for i,v in enumerate(lista_produtos):
  print(f"{i+1}° produto = {v}")
print(f"Primeiros 3 produtos: {lista_produtos[:3]}")
print(f"Últimos 2 produtos: {lista_produtos[-2:]}")