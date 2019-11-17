import argparse

import client
import server

parser = argparse.ArgumentParser(description='File transfer code.')
parser.add_argument('-s', action="store_true", help='Start program as server')
parser.add_argument('input', nargs='*')

args = parser.parse_args()

isServer = args.s

if isServer:
    if len(args.input) != 1:
        print("ERROR: Invalid input(s).")
        print("Usage:")
        print("\tpython student_code.py -c <server port>")
        sys.exit(1)

    try:
        bindPort = int(args.input[0])
    except ValueError:
        print("ERROR: server port must be between 1024 and 65535.")

    server.start(bindPort)

else:
    if len(args.input) != 3:
        print("ERROR: Invalid input(s).")
        print("Usage:")
        print("\tpython student_code.py <server IP> <server port> <filename>")
        sys.exit(1)

    serverIp = args.input[0]
    try:
        serverPort = int(args.input[1])
    except ValueError:
        print("ERROR: server port must be between 1024 and 65535.")

    fileName = args.input[2]

    client.start(serverIp, serverPort, fileName)