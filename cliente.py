#encoding:utf-8

import socket 

HOST = "127.0.0.1"
PORT = 5757
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))
nome_arq = input("Arquivo a ser enviado:")
with open(nome_arq, "rb") as l:
    leitura = l.read()
    c.send(nome_arq.encode('utf-8'))
    c.send(leitura)
    c.close()

