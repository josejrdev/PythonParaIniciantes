"""
SERVIDOR DE CHAT TCP
Este programa cria um servidor que aceita uma conexão e permite
comunicação bidirecional entre servidor e cliente.
O protocolo utilizado é o TCP, que garante entrega confiável.
"""

import socket
import threading

# -------------------------------
# Função que ficará escutando mensagens do cliente
# Essa função roda em uma thread separada para permitir
# que o servidor envie e receba mensagens ao mesmo tempo.
# -------------------------------
def receber(cliente_socket):
    while True:
        try:
            dados = cliente_socket.recv(1024).decode()
            print(f"Cliente: {dados}")
        except:
            print("⚠ Conexão encerrada pelo cliente.")
            cliente_socket.close()
            break


# -------------------------------
# CONFIGURAÇÃO DO SERVIDOR TCP
# -------------------------------
host = "127.0.0.1"  # Endereço local (localhost)
porta = 5000        # Porta escolhida para comunicação

# Criação do socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao IP e porta
servidor.bind((host, porta))

print("Servidor iniciado. Aguardando conexão...")

# Coloca o servidor em modo de escuta (aceita 1 cliente)
servidor.listen(1)

# Aceita a conexão de um cliente
cliente_socket, endereco = servidor.accept()
print(f"Cliente conectado: {endereco}")

# Cria a thread que ficará recebendo mensagens
thread_recebe = threading.Thread(target=receber, args=(cliente_socket,))
thread_recebe.start()

# -------------------------------
# Loop principal para enviar mensagens ao cliente
# -------------------------------
while True:
    mensagem = input("")
    cliente_socket.send(mensagem.encode())
