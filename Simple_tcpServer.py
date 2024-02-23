from socket import *

def encriptar(mensagem, num = 3):
    novaMensagem = ''
    for letra in mensagem:
        novaMensagem += chr(ord(letra) - num);
    return novaMensagem;


def decriptar(mensagem, num = 3):
    novaMensagem = ''
    for letra in mensagem:
        novaMensagem += chr(ord(letra) + num);
    return novaMensagem;

G = 3
N = 7
y = 50000
R2 = (G**y) % N 

serverPort = 1200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.

connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)
received = str(sentence,"utf-8")
K = (int(received)**y) %N
print('K: ', K)
connectionSocket.send(bytes(str(R2),"utf-8"))

while True:
    print("\nWaiting for message:\n")
    sentence = connectionSocket.recv(65000)
    received = str(sentence,"utf-8")
    print("Received: ", received, "\n Decriptar:",decriptar(received, int(K)));
    connectionSocket.send(bytes(received,"utf-8"))
    print ("Sent back to Client: ", received)

connectionSocket.close()


