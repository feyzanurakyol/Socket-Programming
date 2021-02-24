# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:37:26 2020

@author: feyzanur.akyol2016
"""

from datetime import datetime
from socket import *
from time import time

def main():
    servername = 'localhost'
    serverport = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    message = 'Ping'
    counter = 10
    print ('We are gonna send: ', counter, 'pings.\n')
    for i in range(counter+1):

        print('Ping number: ', i, ' remaning pings: ',(counter-i))
        
        timeOne = datetime.now()
        clientSocket.sendto(message.encode('utf-8'), (servername,serverport))
        clientSocket.settimeout(1)
    
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            timeTwo = datetime.now()
            timeRemain = timeOne - timeTwo
            print ("\n--------------------\nMessage: ",modifiedMessage)
            print('Round trip time (RTT): ', (timeRemain.microseconds/1000000) , ' seconds\n--------------------\n\n')
        
        except timeout:
            print('\n--------------------\nTIME OUT\n--------------------\n\n')
            
    if i == 10:
        clientSocket.close()

pass
if __name__ == '__main__':
    main()
    
    