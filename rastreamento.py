divida = 0 # 0
compra = 100 # 100
divida = divida + compra # era 0, recebeu 100
compra = 200 # era 100, recebeu 200
divida = divida + compra # era 100, recebeu 300
compra = 300 # era 200, recebeu 300
divida = divida + compra # era 300, recebeu 600
compra = compra - compra
print(divida)