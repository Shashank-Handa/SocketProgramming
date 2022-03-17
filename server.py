from audioop import mul
import socket
import os
import socketserver
from imgcompression import compress
import threading

def multiClientHandler(connectionSocket):
            ThreadId=threading.get_ident()
            with connectionSocket:

                #file to store image
                filepath=str(ThreadId)+".jpg"
                filepath="1"+filepath

                #loop to recieve image size
                j=''
                charsize=''
                while(j!=">"):
                    j=connectionSocket.recv(1).decode()
                    charsize=charsize+j
                size=int(charsize[0:-1])
                print("recieved image size: ", size)

                #loop to recieve image
                with open(filepath, "wb") as myfile:
                    img=b''
                    while(len(img)<size):
                        temp=connectionSocket.recv(128000)
                        img=img+temp
                    myfile.write(img)
                print("recieved image")

                #Compressing image file
                filepath2=compress(filepath)
                print("image compressed")

                #sending compressed image
                myfile=open(filepath2, "rb")
                img2=myfile.read()
                size=len(img2)
                charsize=str(size)
                connectionSocket.send((charsize+">").encode())
                connectionSocket.sendall(img2)

                print("image file sent")
                print("Closing connection with client")

            connectionSocket.close()
            os.remove(filepath)
            os.remove(filepath2)
            


serverPort = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:

    socketserver.TCPServer.allow_reuse_address=True
    serverSocket.bind(('',serverPort))
    serverSocket.listen(4)
    print("Server is running")
    ThreadCount=0
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("connected to client ",addr)
        x=threading.Thread(target=multiClientHandler, args=([connectionSocket]), daemon=True)
        x.start()
        ThreadCount+=1
        print("client at ", addr, "running on thread number ",ThreadCount)

