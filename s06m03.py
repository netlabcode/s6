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
PORT3 = 993
PORT4 = 994


#OPC ACCESS
url = "opc.tcp://10.1.0.99:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=224")
val2 = client.get_node("ns=2;i=225")
val3 = client.get_node("ns=2;i=226")
val4 = client.get_node("ns=2;i=227")
val5 = client.get_node("ns=2;i=228")
val6 = client.get_node("ns=2;i=229")
val7 = client.get_node("ns=2;i=230")
val8 = client.get_node("ns=2;i=231")
val9 = client.get_node("ns=2;i=232")
val10 = client.get_node("ns=2;i=233")
val11 = client.get_node("ns=2;i=234")
val12 = client.get_node("ns=2;i=235")
val13 = client.get_node("ns=2;i=236")


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

				stringd = str(value1)+"+"+str(value2)+"+"+str(value3)+"+"+str(value4)+"+"+str(value5)+"+"+str(value6)+"+"+str(value7)+"+"+str(value8)+"+"+str(value9)+"+"+str(value10)+"+"+str(value11)+"+"+str(value12)+"+"+str(value13)

				#convert string to bytes data
				data1 = stringd.encode()

				#send data back to client
				conn1.sendall(data1)

				#print('S1:',data1)
				time.sleep(1)

				"""
				while a < 6:

					#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()

					#covert inetger to string
					#stringd = str(value)

					stringd = str(value1)+"-"+str(value2)+"-"+str(value3)+"-"+str(value4)+"-"+str(value5)+"-"+str(value6)

					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)
					time.sleep(1)
				"""

# Define a function for the thread
def serverOneCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT3))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2

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

				stringd = str(value1)+"+"+str(value2)+"+"+str(value3)+"+"+str(value4)+"+"+str(value5)+"+"+str(value6)+"+"+str(value7)+"+"+str(value8)+"+"+str(value9)+"+"+str(value10)+"+"+str(value11)+"+"+str(value12)+"+"+str(value13)


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
				data2 = conn2.recv(1024)
				data3 = data2.decode("utf-8")
				a,b = data3.split("+")


				value = int(b)
				check = int(a)
				if check == 224:
					val1.set_value(value, ua.VariantType.Int16)
					print('Value 224 set to:',value)
				elif check == 225:
					val2.set_value(value, ua.VariantType.Int16)
					print('Value 225 set to:',value)
				elif check == 226:
					val3.set_value(value, ua.VariantType.Float)
					print('Value 226 set to:',value)
				elif check == 227:
					val4.set_value(value, ua.VariantType.Float)
					print('Value 227 set to:',value)
				elif check == 228:
					val5.set_value(value, ua.VariantType.Float)
					print('Value 228 set to:',value)
				elif check == 229:
					val6.set_value(value, ua.VariantType.Float)
					print('Value 229 set to:',value)
				elif check == 230:
					val7.set_value(value, ua.VariantType.Int16)
					print('Value 230 set to:',value)
				elif check == 231:
					val8.set_value(value, ua.VariantType.Float)
					print('Value 231 set to:',value)
				elif check == 232:
					val9.set_value(value, ua.VariantType.Float)
					print('Value 232 set to:',value)
				elif check == 233:
					val10.set_value(value, ua.VariantType.Float)
					print('Value 233 set to:',value)
				elif check == 234:
					val11.set_value(value, ua.VariantType.Float)
					print('Value 234 set to:',value)
				elif check == 235:
					val12.set_value(value, ua.VariantType.Float)
					print('Value 235 set to:',value)
				elif check == 236:
					val13.set_value(value, ua.VariantType.Float)
					print('Value 236 set to:',value)
				else:
						print(".")

def serverTwoCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT4))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				data2 = conn2.recv(1024)
				data3 = data2.decode("utf-8")
				a,b = data3.split("+")


				value = int(b)
				check = int(a)
				if check == 224:
					val1.set_value(value, ua.VariantType.Int16)
					print('Value 224 set to:',value)
				elif check == 225:
					val2.set_value(value, ua.VariantType.Int16)
					print('Value 225 set to:',value)
				elif check == 226:
					val3.set_value(value, ua.VariantType.Float)
					print('Value 226 set to:',value)
				elif check == 227:
					val4.set_value(value, ua.VariantType.Float)
					print('Value 227 set to:',value)
				elif check == 228:
					val5.set_value(value, ua.VariantType.Float)
					print('Value 228 set to:',value)
				elif check == 229:
					val6.set_value(value, ua.VariantType.Float)
					print('Value 229 set to:',value)
				elif check == 230:
					val7.set_value(value, ua.VariantType.Int16)
					print('Value 230 set to:',value)
				elif check == 231:
					val8.set_value(value, ua.VariantType.Float)
					print('Value 231 set to:',value)
				elif check == 232:
					val9.set_value(value, ua.VariantType.Float)
					print('Value 232 set to:',value)
				elif check == 233:
					val10.set_value(value, ua.VariantType.Float)
					print('Value 233 set to:',value)
				elif check == 234:
					val11.set_value(value, ua.VariantType.Float)
					print('Value 234 set to:',value)
				elif check == 235:
					val12.set_value(value, ua.VariantType.Float)
					print('Value 235 set to:',value)
				elif check == 236:
					val13.set_value(value, ua.VariantType.Float)
					print('Value 236 set to:',value)
				else:
						print(".")




# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverOneCC, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverTwoCC, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass