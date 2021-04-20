import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.1.0.11'
HOST2 = '100.1.0.12'
HOST3 = '100.1.0.13'
HOST4 = '100.1.0.14'
RHOST = '131.180.165.21'

PORT2 = 994
PORTS2 = 8801


# Define a function for the thread
def serverOne():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sr:
        sr.connect((RHOST, PORTS2))

        while True:
           try:
               data2 = sr.recv(1024)
               data2new = data2.decode("utf-8")
               print(data2new)
               time.sleep(1)
           except:
              print("Close connection")
              sr.close()
              time.sleep(2)
              print("Restarting . . . ")
              serverOne()
        
							
# Create two threads as follows
try:
   serverOne()

except:
   print ("Error: unable to start server")

while 1:
   pass