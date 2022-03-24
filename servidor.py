#encoding:utf-8

import socket 
HOST = "127.0.0.1"
PORT = 5757

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
con, cliente = s.accept()
print("O seguinte cliente se conectou ao servidor:", cliente)
nome_arq = con.recv(1024).decode('utf-8')
print(nome_arq)
dados_arq = con.recv(10000000)
with open(nome_arq, "ab") as g:
   g.write(dados_arq)
   print("Arquivo recebido com sucesso!")
s.close()

