"""
Programa que realiza uma operação matemática entre dois números de
acordo com um código informado pelo usuário. O código 1 calcula a
média, o código 2 calcula a diferença entre o maior e o menor número,
o código 3 calcula o produto e o código 4 realiza a divisão.
Caso seja informado um código diferente de 1 a 4, o programa informa
que o código é inválido e apresenta as opções disponíveis.
"""
def escolha(n_1, n_2, codigo):
  if codigo == 1:
    return media(n_1,n_2)
  elif codigo == 2:
    return diferenca_maior_menor(n_1, n_2)
  elif codigo == 3:
    return produto(n_1, n_2)
  elif codigo == 4:
    return divisao(n_1, n_2)
  else:
    return codigo_invalido(codigo)
def media(n_1,n_2):
  calc_media = (n_1 + n_2) / 2
  return calc_media
def diferenca_maior_menor(n_1,n_2):
  if n_1 > n_2:
    diferenca = n_1 - n_2
    return diferenca
  elif n_2 > n_1:
    diferenca = n_2 - n_1
    return diferenca
  else:
    diferenca = "Números Iguais"
    return diferenca
def produto(n_1, n_2):
  produto = n_1 * n_2
  return produto
def divisao(n_1, n_2):
  if n_2 != 0:
    divisao = n_1 / n_2
    return divisao
  else:
    divisao = "Divisão por zero"
    return divisao
def codigo_invalido(codigo):
  titulo = f"Você digitou {codigo}, esse código é inválido."
  mensagem = "\nDigite apenas códigos válidos, 1(Média), 2(Diferença), 3(Produto) ou 4(Divisão)."
  return titulo + mensagem
n_1 = int(input("Digite o primeiro número: "))
n_2 = int(input("Digite o segundo número: "))
codigo = int(input("Digite o código(1,2,3 ou 4): "))
print(escolha(n_1, n_2, codigo))