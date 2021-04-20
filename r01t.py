import socket
import os
import _thread
import time

ServerSocket = socket.socket()
host = ''
port = 8801
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = "a"
        datax = data.encode()
        if not data:
            break
        try:
            connection.sendall(datax)
            time.sleep(1)
        except:
            connection.close()

    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    _thread.start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()