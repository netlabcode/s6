#!/user/bin/env python3
from opcua import Client
from opcua import ua
import socket
import binascii
import _thread
import time


HOST = ''


#OPC ACCESS
url = "opc.tcp://131.180.165.5:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=213")
val2 = client.get_node("ns=2;i=214")
val3 = client.get_node("ns=2;i=215")
val4 = client.get_node("ns=2;i=216")
val5 = client.get_node("ns=2;i=217")
val6 = client.get_node("ns=2;i=218")


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

	print(value1,value2,value3,value4,value5,value6)

	time.sleep(1)

