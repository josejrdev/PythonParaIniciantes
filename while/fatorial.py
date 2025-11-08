#6! = 6 * 5 * 4 * 3 * 2 * 1
#ou...
#6! = 1 * 2 * 3 * 4 * 5 * 6
#8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 0! = 1
n = int(input('Digite o valor de n: '))

contador = 1
fatorial = 1

while contador <= n:
  fatorial = fatorial * contador
  contador = contador + 1
print(fatorial)