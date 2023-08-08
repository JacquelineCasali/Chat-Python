# comunicação de duas portas
import socket

servidor =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# endereço
servidor.bind(('localhost',8800))

servidor.listen()

cliente,end = servidor.accept()
print('Digite tt para terminar o chat')
terminado= False
while not terminado:
    msg= cliente.recv(1024).decode('utf-8')
    if msg =='tt':
        terminado=True
    else:
        print(msg)
        cliente.send(input('Mensagem: ').encode('utf-8'))
cliente.close()
servidor.close()       