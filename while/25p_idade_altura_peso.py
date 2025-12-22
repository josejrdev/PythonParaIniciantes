cont = 1
pessoasMais50 = 0
somaAlturas = 0.0
qtdPessoasPesoMenor40 = 0
qtdPessoasEntre10e20 = 0
while cont <= 25:
    idade = int(input("Digite a idade da pessoa: "))
    altura = float(input("Digite a altura da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    if idade > 50:
        pessoasMais50 = pessoasMais50 + 1
    elif idade >= 10 and idade <= 20:
        somaAlturas = somaAlturas + altura
        qtdPessoasEntre10e20 = qtdPessoasEntre10e20 + 1
    if peso < 40:
        qtdPessoasPesoMenor40 = qtdPessoasPesoMenor40 + 1
    cont = cont + 1
mediaAlturas10e20 = somaAlturas / qtdPessoasEntre10e20
percentagemPessoasPesoMenor40 = qtdPessoasPesoMenor40 / 25
print(f"Quantidade de pessoas com idade superior a 50: {pessoasMais50}")
print(f"A média das alturas das pessoas entre 10 e 20 é {mediaAlturas10e20}")
print(f"A percentagem de pessoas com peso menor que 40 é: {percentagemPessoasPesoMenor40:.1%}")