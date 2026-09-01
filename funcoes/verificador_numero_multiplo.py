"""
Função que verifica se o primeiro número é múltiplo do segundo,
utilizando o operador de módulo (%) para verificar se a divisão
entre eles possui resto igual a zero.
"""
def multiplo (p,s):
    return p % s == 0
print(multiplo(5,5))