print("1. Média Aritmética, 2. Média Ponderada, 3. Sair")
opcaoUsuario = int(input("Digite a opção Desejada: "))
while opcaoUsuario < 1 or opcaoUsuario > 3:
  opcaoUsuario = int(input("Digite uma opção válida: "))
if opcaoUsuario == 1:
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))
  mediaAritmetica = (nota1 + nota2) / 2
  print(f"Média aritmética: {mediaAritmetica:.2f}")
elif opcaoUsuario == 2:
  nota1 = float(input("Digite a primeira nota: "))
  peso1 = float(input("Digite o primeiro peso: "))
  nota2 = float(input("Digite a segunda nota: "))
  peso2 = float(input("Digite o segundo peso: "))
  nota3 = float(input("Digite a terceira nota: "))
  peso3 = float(input("Digite o terceiro peso: "))
  mediaPonderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
  print(f"Média ponderada: {mediaPonderada:.2f}")
else:
  print(f"Fim do programa.")