def fatorial(x):
    f = 1
    while x > 1:
        f = f * x
        x = x - 1
    return f
print(fatorial(0))