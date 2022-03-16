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

    i=0
    while(i!=1):
        filepath=input("enter file path")
        try:
            i=1
            imgfile=open(filepath, 'rb');
        except:
            print("file does not exist")
            i=0

    #read file
    img=imgfile.read()
    size1=len(img)
    charsize=str(size1)

    #send image size in string format to server
    clientSocket.send((charsize+">").encode())
    #send image to server
    clientSocket.sendall(img)

    #recieve size of compressed image from server
    j=''
    charsize=''
    while(j!=">"):
        j=clientSocket.recv(1).decode()
        charsize=charsize+j
    size=int(charsize[0:-1])

    #recieve image from server and write to file
    with open("optimized"+filepath,"wb") as optimizedImage:
        tempbytes=b''
        img=b''
        while(len(img)<size):
            temp=clientSocket.recv(128000)
            img=img+temp

        optimizedImage.write(img)
        
    optimizedImage.close()

    #size of image
    size2=len(img)

    print("size of image before compression: ", size1)
    print("size of image after compression: ", size2)
