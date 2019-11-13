import settings
from CustomSocket import CustomSocket


serverAddr = (settings.SERVER_IP, settings.SERVER_BIND_PORT)

clientSocket = CustomSocket(settings.CLIENT_BIND_PORT, settings.BYTE_ERROR_RATE)
print("Initiating request to server {}:{}".format(settings.SERVER_IP, settings.SERVER_BIND_PORT))
clientSocket.sendto(b"hello", serverAddr)

if settings.RUN_DEMO == 1:
    while True:
        data, addr = clientSocket.recvfrom(settings.BUFFER_SIZE)
        print("Rx: {} from {}".format(data, addr))
elif settings.RUN_DEMO == 2:
    with open("/tmp/rx_test.jpg", "wb") as f:
        while True:
            data, addr = clientSocket.recvfrom(settings.BUFFER_SIZE)
            if data == settings.TEST_EOF:
                print("File received")
                break
            else:
                f.write(data)
else:
    ############################
    # Student's code goes here #
    ############################
    pass

