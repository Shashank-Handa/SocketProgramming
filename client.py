from http import client
import socket
serverName="10.0.2.5"
serverPort=12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence=input("enter file path :")

clientSocket.send(sentence.encode())

modified=clientSocket.recv(1024)
print("from server: ", modified.decode())
clientSocket.close()
