import socket
import sys

import settings
from CustomSocket import CustomSocket


def start(bindPort):    
    serverSocket = CustomSocket(bindPort, 0)
    print("Server listening on {}:{}".format("0.0.0.0", bindPort))

    # wait for client request
    data, clientAddr = serverSocket.recvfrom(settings.BUFFER_SIZE)
    print("Received request from {}:\n{}".format(clientAddr, data))
        
    if settings.RUN_DEMO == 1:
        serverSocket.sendto(b"hello", clientAddr)
    elif settings.RUN_DEMO == 2:
        with open(settings.TEST_FILES_DIR + "test.jpg", 'rb') as f:
            while True:
                chunk = f.read(settings.BUFFER_SIZE)            
                if chunk:
                    serverSocket.sendto(chunk, clientAddr) 
                else:                
                    serverSocket.sendto(settings.TEST_EOF, clientAddr)
                    print("File sent")
                    break

    else:
        ############################
        # Student's code goes here #
        ############################
        pass
