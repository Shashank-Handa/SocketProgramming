from http import client
import socket
<<<<<<< HEAD
serverName="10.0.0.1"
serverPort="12000"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((serverName, serverPort))

    #accept file path and open file
    filepath=input("enter file path")
    i=0
    while(i!=1):
        try:
            i=1
            img=open(filepath, 'rb');
        except:
            print("file does not exist")
            i=0
    
    clientSocket.send(filepath.encode())
    clientSocket.send(img)

    clientSocket.close()
=======
serverName="10.0.2.5"
serverPort=12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence=input("enter file path :")

clientSocket.send(sentence.encode())

modified=clientSocket.recv(1024)
print("from server: ", modified.decode())
clientSocket.close()
>>>>>>> c02d1589c1f784473ee128c603bf0790d1acb4f1
