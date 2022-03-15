import socket
import os
from imgcompression import compress
serverPort = 12000
serverSocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is running")
while True:
    connectionSocket, addr = serverSocket.accept()

    filepath="temp"
    filepath="1"+filepath
    myfile=open(filepath, "wb")
    print("opened")

    img=connectionSocket.recv(470000)
    while(img!=b''): 
        myfile.write(img)
        img=connectionSocket.recv(470000)
    myfile.close()

    filepath2=compress(filepath)

    myfile=open(filepath, "rb")
    connectionSocket.send(myfile)

    print("done")
    os.remove(filepath)
    os.remove(filepath2)
    connectionSocket.close()
