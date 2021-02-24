from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',80)) 
serverSocket.listen(10)
#Fill in start
#Fill in end
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode('utf-8')
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)
        

        #Send one HTTP header line into socket
        connectionSocket.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
        connectionSocket.sendall(b'Content-Type: text/html/r/n')

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.sendall(outputdata[i].encode('utf-8'))
                                  
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.sendall(b'404 Not Found')
        print("\n404 Not Found\n\n")

        #Close client socket
        connectionSocket.close()

serverSocket.close()
