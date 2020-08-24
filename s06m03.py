#!/user/bin/env python3
from opcua import Client
from opcua import ua
import socket
import binascii
import _thread
import time


HOST = ''
PORT1 = 991
PORT2 = 992


#OPC ACCESS
url = "opc.tcp://10.1.0.99:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=227")
val2 = client.get_node("ns=2;i=228")
val3 = client.get_node("ns=2;i=229")
val4 = client.get_node("ns=2;i=230")
val5 = client.get_node("ns=2;i=231")
val6 = client.get_node("ns=2;i=232")
val7 = client.get_node("ns=2;i=233")
val8 = client.get_node("ns=2;i=234")
val9 = client.get_node("ns=2;i=235")
val10 = client.get_node("ns=2;i=236")
val11 = client.get_node("ns=2;i=237")
val12 = client.get_node("ns=2;i=238")
val13 = client.get_node("ns=2;i=239")


# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT1))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2
				while a < 6:

					#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()
					value7 = val7.get_value()
					value8 = val8.get_value()
					value9 = val9.get_value()
					value10 = val10.get_value()
					value11 = val11.get_value()
					value12 = val12.get_value()
					value13 = val13.get_value()

					#covert inetger to string
					#stringd = str(value)

					stringd = str(value1)+"-"+str(value2)+"-"+str(value3)+"-"+str(value4)+"-"+str(value5)+"-"+str(value6)+"-"+str(value7)+"-"+str(value8)+"-"+str(value9)+"-"+str(value10)+"-"+str(value11)+"-"+str(value12)+"-"+str(value13)

					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)
					time.sleep(1)


# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT2))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				while b < 6:
					data2 = conn2.recv(1024)
					print('Data:',data2)





# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass