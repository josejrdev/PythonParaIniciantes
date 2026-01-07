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