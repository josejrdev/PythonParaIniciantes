"""
CLIENTE DE CHAT TCP
Este programa se conecta ao servidor TCP e permite troca
de mensagens bidirecional entre cliente e servidor.
"""

import socket
import threading

# -------------------------------
# Função para receber mensagens do servidor
# Ela deve ser executada em paralelo ao envio, por isso usamos thread
# -------------------------------
def receber(socket_cliente):
    while True:
        try:
            dados = socket_cliente.recv(1024).decode()
            print(f"Servidor: {dados}")
        except:
            print("⚠ Conexão encerrada pelo servidor.")
            socket_cliente.close()
            break


# -------------------------------
# CONFIGURAÇÃO DO CLIENTE TCP
# -------------------------------
host = "127.0.0.1"   # Mesmo IP do servidor
porta = 5000         # Mesma porta do servidor

# Criação do socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão ao servidor
cliente.connect((host, porta))
print("Conectado ao servidor!")

# Criação da thread de recebimento
thread_recebe = threading.Thread(target=receber, args=(cliente,))
thread_recebe.start()

# -------------------------------
# Loop principal para enviar mensagens ao servidor
# -------------------------------
while True:
    mensagem = input("")
    cliente.send(mensagem.encode())
