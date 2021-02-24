"""
Created on Mon Jan  4 20:17:44 2021

@author: Feyza
"""

from socket import *
import base64
import ssl 

msg = "\r\n I love computer networks! \r\n\r\n"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
print ("Recived Message: ", recv)
if recv[:3] != b'220':
    print ("220 reply not received from server.\n")

# Send HELO command and print server response.
helo = 'HELO Alice\r\n'
clientSocket.send(helo.encode())
recv1 = clientSocket.recv(1024)
print ("\nHELO command server response: ",recv1)
if recv1[0:3] != b'250':
    print ("250 reply not received from server.\n")

#Send STARTTLS  command 
clientSocket.send(("STARTTLS\r\n".encode()))
recvTls = clientSocket.recv(1024)
print("STARTTLS Response: " + recvTls.decode())
clientSocket = ssl.wrap_socket(clientSocket)

#Username and password information
username = "deneme1530@gmail.com"                    
password = "EK123456"              
base64_str = ("\x00"+username +"\x00"+password).encode()
base64_str =  base64.b64encode(base64_str) #bu ne yapıyo bi baksana
authentMessage = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(authentMessage)
receiveAuth = clientSocket.recv(1024)
print("\nAUTHANTICATION: " + receiveAuth.decode())
if receiveAuth[0:3] != b'235':
    print ("235 reply not received from server.\n")

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <deneme1530@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recvMail = clientSocket.recv(1024)
print ("\nMAIL FROM :" + recvMail.decode())
if recvMail[0:3] != b'250':
    print ("250 reply not received from server.\n")

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <fnuakyol@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recvRcp = clientSocket.recv(1024)
print("\nRCPT TO: " + recvRcp.decode())
if recvRcp[0:3] != b'250':
    print ("250 reply not received from server.\n")

# Send DATA command and print server response.
data = "DATA \r\n"
clientSocket.send(data.encode())
recvData = clientSocket.recv(1024)
print("\nDATA: " + recvData.decode())
if recvData[0:3] != b'354':
    print ("250 reply not received from server.\n")

# Send message data.
clientSocket.send(msg.encode())
#I didn't receive a request message, cuz
#data is not ended yet.

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv_message1 = clientSocket.recv(1024)
print ("\nENDS : " + recv_message1.decode())
if recv_message1[0:3] != b'250':
    print ("250 reply not received from server.\n")

# Send QUIT command and get server response.
clientSocket.send("QUIT \r\n".encode())
message=clientSocket.recv(1024)
print ("\nQUIT " + message.decode())
if message[0:3] != b'221':
    print ("221 reply not received from server.\n")
clientSocket.close()
