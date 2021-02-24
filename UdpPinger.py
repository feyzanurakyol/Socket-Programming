# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:29:24 2020

@author: feyzanur.akyol2016
"""

import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',12000))

while True:
    rand = random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    if rand < 4:
        continue
    serverSocket.sendto(message, address)