cont = 1
soma15 = 0
soma16a30 = 0
soma31a45 = 0
soma46a60 = 0
somaAcima60 = 0
while cont <= 15:
  idade = int(input("Digite a idade da pessoa: "))
  if idade <= 15:
    soma15 = soma15 + 1
  elif idade >= 16 and idade <= 30:
    soma16a30 = soma16a30 + 1
  elif idade >= 31 and idade <= 45:
    soma31a45 = soma31a45 + 1
  elif idade >= 46 and idade <= 60:
    soma46a60 = soma46a60 + 1
  else:
    somaAcima60 = somaAcima60 + 1
  cont = cont + 1
perPessoasFaixa1e5 = (soma15 + somaAcima60) / 15
print(f"Até 15 anos: {soma15} pessoas")
print(f"De 16 a 30 anos: {soma16a30} pessoas")
print(f"De 31 a 45 anos: {soma31a45} pessoas")
print(f"De 46 a 60 anos: {soma46a60} pessoas")
print(f"Acima de 60 anos: {somaAcima60} pessoas")
print(f"Percentagem de pessoas Primeira e Última faixas: {perPessoasFaixa1e5:.1%}")