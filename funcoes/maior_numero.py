def maior_numero(n_1, n_2, n_3):
  if n_1 >= n_2 and n_1 >= n_3:
    return (f"{n_1} é maior.")
  elif n_2 >= n_1 and n_2 >= n_3:
    return (f"{n_2} é maior.")
  elif n_3 >= n_1 and n_3 >= n_2:
    return (f"{n_3} é maior.")
n_1 = int(input("Digite o primeiro número: "))
n_2 = int(input("Digite o segundo número: "))
n_3 = int(input("Digite o terceiro número: "))
print(maior_numero(n_1,n_2,n_3))