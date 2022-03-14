from http import client
from pydoc import cli
import socket
serverName="10.0.2.5"
serverPort=12000
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("successfully connected")
#accept file path and open file
filepath=input("enter file path")
i=0
while(i!=1):
    try:
        i=1
        imgfile=open(filepath, 'rb');
    except:
        print("file does not exist")
        i=0
img=imgfile.read()

clientSocket.send((filepath+">").encode())

clientSocket.send(img)