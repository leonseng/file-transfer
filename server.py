import socket
import sys

import settings as const
from CustomSocket import CustomSocket


serverSocket = CustomSocket(settings.SERVER_BIND_PORT, 0)
print("Server started on {}:{}".format(settings.SERVER_IP, settings.SERVER_BIND_PORT))

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
