import socket
import os
import socketserver
from imgcompression import compress
import math
serverPort = 12000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket :
    socketserver.TCPServer.allow_reuse_address=True
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print("Server is running")
    while True:
        connectionSocket, addr = serverSocket.accept()
        with connectionSocket:
            filepath="temp.jpg"
            filepath="1"+filepath
            
            print("opened")
            j=''
            charsize=''
            while(j!=">"):
                j=connectionSocket.recv(1).decode()
                charsize=charsize+j
            size=int(charsize[0:-1])
            with open(filepath, "wb") as myfile:
                tempbytes=b''
                img=b''
                while(len(img)<size):
                    
                    temp=connectionSocket.recv(128000)
                    img=img+temp
                myfile.write(img)
            
    
                    
                    
            """img=connectionSocket.recv(470000)
            with open(filepath, "wb") as myfile:
                while(img!=b''): 
                    myfile.write(img)
                    try:
                        img=connectionSocket.recv(470000)
                    except:
                        break;
                    print("revieve loop")   
                print("loop exited")
            myfile.close()
            print("file closed")"""
            filepath2=compress(filepath)

            myfile=open(filepath2, "rb")
            img2=myfile.read()
            size=len(img2)
            charsize=str(size)
            connectionSocket.send((charsize+">").encode())
            connectionSocket.sendall(img2)

            print("done")
        connectionSocket.close()
        os.remove(filepath)
        os.remove(filepath2)
