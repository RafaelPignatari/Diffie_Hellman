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
X = 10

R1 = (G**X) % N


from socket import *
serverName = "10.1.70.24"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('R1 =>' , R1);
clientSocket.send(bytes(str(R1), "utf-8"))
modifiedSentence = clientSocket.recv(1024)
R2 = str(modifiedSentence,"utf-8")
k = (int(R2)**X) % N
print ("K : ", k)

while True:
    sentence = input("Message: ")

    if(sentence == ""):
        break

    clientSocket.send(bytes(encriptar(sentence, int(k)), "utf-8"))

    modifiedSentence = clientSocket.recv(1024)
    received = str(modifiedSentence, "utf-8")
    print ("Received from Make Upper Case Server: ", decriptar(received, int(k)))

clientSocket.close()

