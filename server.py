import socket
from os import remove
serverPort = 12000
serverSocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is running")
while True:
    connectionSocket, addr = serverSocket.accept()
    filepath=""
    char=""
    while(char!=">"):
        filepath+=char
        char = connectionSocket.recv(1).decode()
    
    input(filepath)

    myfile=open("1"+filepath, "wb")
    print("opened")

    img=connectionSocket.recv(470000)
    while(img!=b''): 
        myfile.write(img)
        img=connectionSocket.recv(470000)
    myfile.close()
    print("done")
    connectionSocket.close()