"""
Programa que solicita uma senha ao usuário repetidamente até que a
senha correta seja informada. A cada tentativa, armazena a senha
digitada em uma lista de histórico e incrementa o contador de
tentativas. Ao final, exibe a quantidade de tentativas realizadas e
o histórico das senhas digitadas.
"""
senha = "IFPE420ads1noite"
qtdTentativas = 0
listaHistoricoSenhas = []
while True:
  senhaUsuario = input("Digite a senha: ")
  listaHistoricoSenhas.append(senhaUsuario)
  qtdTentativas = qtdTentativas + 1
  if senhaUsuario == senha:
    break
print(f"Tentativas: {qtdTentativas}")
print(f"Histórico de senhas digitadas: {listaHistoricoSenhas}")