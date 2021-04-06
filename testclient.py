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
url = "opc.tcp://srv786.tudelft.net:53530/OPCUA/SimulationServer"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=213")
val2 = client.get_node("ns=2;i=213")



value = 0
while value < 3:
    value1 = val1.get_value()
    value2 = val2.get_value()
    print(value1)
    print(value2)
    print("===")
    time.sleep(1)
