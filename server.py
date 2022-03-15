import socket
from os import remove
import PIL
serverPort = 12000
serverSocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is running")
while True:
    connectionSocket, addr = serverSocket.accept()
    filepath = connectionSocket.recv(1024).decode()

    myfile=open("1"+filepath, "wb")
    
    img=connectionSocket.recv(1024)

    myfile.write(img)
    myfile.close()

    imgfile=PIL.Image.open("1"+filepath)

    connectionSocket.close()
