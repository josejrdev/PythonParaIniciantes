listaPalavras = [
  "Computador", "Mobile", "Internet", "Web",
  "Roteamento", "Dados", "WiFi", "Sistema",
  "Aplicativo", "Podcast", "Email", "Software",
  "Hardware", "Processador", "Transistor", "Ebook",
  "Monitor", "Live", "Like", "Youtube", "Intel",
  "Microsoft", "Linux", "Apple", "Android", "Spotify",
  "Whatsapp", "Telegram", "Informação", "Tecnologia"
]
lista10PrimeirasPalavras = listaPalavras[0:10]
lista10UltimasPalavras = listaPalavras[-10:]
listaPalavrasPosicoesPares = []
qtdPalavrasMaisDe7Letras = 0
listaPalavrasComMaisDe7Letras = []
cont = 0
while cont < len(listaPalavras):
  if cont % 2 == 0:
    listaPalavrasPosicoesPares.append(listaPalavras[cont])
  if len(listaPalavras[cont]) > 7:
    qtdPalavrasMaisDe7Letras = qtdPalavrasMaisDe7Letras + 1
    listaPalavrasComMaisDe7Letras.append(listaPalavras[cont])
  cont = cont + 1
print(f"As 10 primeiras palavras são: {lista10PrimeirasPalavras}")
print(f"As 10 últimas palavras são {lista10UltimasPalavras}")
print(f"Palavras em índices pares: {listaPalavrasPosicoesPares}")
print(f"Total de palavras com mais de 7 letras: {qtdPalavrasMaisDe7Letras}")
print(f"As palavras com mais de 7 letras são: {listaPalavrasComMaisDe7Letras}")