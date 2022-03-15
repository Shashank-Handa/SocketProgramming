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

filepath=""
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

clientSocket.send(img)

optimizedImage=open("optimized"+filepath,"wb")
img2=clientSocket.recv(470000)
while(img!=b''): 
    optimizedImage.write(img2)
    img2=clientSocket.recv(470000)
optimizedImage.close()

clientSocket.close()
