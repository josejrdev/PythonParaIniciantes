distancia = float(input("Digite a distância que deseja percorrer em KM: "))
if distancia <= 200:
    valorViajem = distancia * 0.50
else: 
    valorViajem = distancia * 0.45
print(f"Valor da viajem: R${valorViajem:.2f}")