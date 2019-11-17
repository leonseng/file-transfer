import settings
from CustomSocket import CustomSocket


def start(serverIp, serverPort, fileName):
    serverAddr = (serverIp, serverPort)

    clientSocket = CustomSocket(0, settings.BYTE_ERROR_RATE)
    print("Initiating request to server {}:{}".format(serverIp, serverPort))
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

