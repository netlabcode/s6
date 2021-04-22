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
url = "opc.tcp://srv785.tudelft.net:53530/OPCUA/SimulationServer"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=7;i=1")
val2 = client.get_node("ns=7;i=2")


value=0
val1.set_value(value, ua.VariantType.Int16)

