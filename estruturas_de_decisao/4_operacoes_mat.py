"""
Algoritmo que recebe dois números do usuário e uma operação matematica
de acordo com a operação escolhida pelo usuário, realiza o calculo.
a operação escolhida deve ser necessariamente soma(+), subtração(-),
multiplicação(*) ou divisão(/). 
"""

# Coletando o primeiro número
n1 = int(input("Digite o primeiro número: "))

# Colentando o segundo número
n2 = int(input("Digite o segundo número: "))

# Coletando a operação desejada
operacao = input("Qual operação deseja realizar? ")

# 
calculo = 0

# estrutura condicional com if/elif/else para decidir qual o calculo será feito
if operacao == "+":
    calculo = n1 + n2
elif operacao == "-":
    calculo = n1 - n2
elif operacao == "*":
    calculo = n1 * n2
elif operacao == "/":
    # Realiza o calculo de divisão apenas se o n2 for diferente de zero
    if n2 != 0: 
        calculo = n1 / n2
    # se n2 for igual a 0, calculo continua sendo 0
    else:
        calculo = 0
else:
    # Se a operação for inválida, exibe uma mensagem de operação inválida
    print("Operação inválida.")

# Exibe o resultado final
print(f"Resultado: {calculo}")