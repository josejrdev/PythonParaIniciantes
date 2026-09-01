"""
Programa que solicita o nome e o ano de nascimento de uma pessoa e
calcula quantos anos ela terá no dia 31 de dezembro de 2025.
Ao final, exibe uma mensagem de saudação com o nome e a idade calculada.
"""
def saudacao(nome,ano_nascimento):
  idade = 2025 - ano_nascimento
  return (f"Boa noite, {nome}. você terá {idade} anos no dia 31 de dezembro de 2025")
nome_usuario = input("Digite o seu nome: ")
ano_nascimento_usuario = int(input("Digite o ano do seu nascimento: "))
print(saudacao(nome_usuario,ano_nascimento_usuario))