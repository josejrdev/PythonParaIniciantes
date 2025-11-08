n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 >= n2 and n1 >= n3:
    print(f"{n1} é o maior")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} é o maior")
elif n3 >= n1 and n3 >= n2:
    print(f"{n3} é o maior")
if n1 <= n2 and n1 <= n3:
    print(f"{n1} é o menor")
elif n2 <= n1 and n2 <= n3:
    print(f"{n2} é o menor")
elif n3 <= n1 and n3 <= n2:
    print(f"{n3} é o menor")