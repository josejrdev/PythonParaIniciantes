n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
escolha = int(input("Qual a sua escolha? "))
if escolha == 1:
  media = n1 + n2 / 2
  print(f"Média: {media:.2f}")
elif escolha == 2:
  if n1 > n2:
    diferenca = n1 - n2
    print(f"Diferença: {diferenca}")
  else:
    diferenca = n2 - n1
    print(f"Diferença: {diferenca}")
elif escolha == 3:
  produto = n1 * n2
  print(f"Produto: {produto}")
elif escolha == 4:
  divisao = n1 / n2
  print(f"Divisão do primeiro pelo segundo: {divisao}")
else:
  print(f"Opção inválida, fim do programa.")