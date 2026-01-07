def fatorial(n):
    fat = 1 
    x = 1
    while x <=n :
        fat = fat * x
        x = x + 1
    return fat
print(fatorial(4))