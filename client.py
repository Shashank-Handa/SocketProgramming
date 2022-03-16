from http import client
from pydoc import cli
import socket
import math
serverName="10.0.2.5"
serverPort=12000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
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
    size1=len(img)
    charsize=str(size1)
    clientSocket.send((charsize+">").encode())
    clientSocket.sendall(img)

    j=''
    charsize=''
    while(j!=">"):
        j=clientSocket.recv(1).decode()
        charsize=charsize+j
    size=int(charsize[0:-1])

    with open("optimized"+filepath,"wb") as optimizedImage:
        tempbytes=b''
        img=b''
        while(len(img)<size):
            temp=clientSocket.recv(128000)
            img=img+temp

        optimizedImage.write(img)
    
    """with open("optimized"+filepath,"wb") as optimizedImage:
        img2=clientSocket.recv(470000)
        while(img2!=b''): 
            print("recieveloop")
            optimizedImage.write(img2)
            img2=clientSocket.recv(470000)"""
        
    optimizedImage.close()
    img2=open("optimized"+filepath,"rb").read()
    size2=len(img2)

    print("size of image before compression: ", size1)
    print("size of image after compression: ", size2)
