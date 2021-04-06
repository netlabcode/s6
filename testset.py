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
val1 = client.get_node("ns=3;i=1008")
val2 = client.get_node("ns=3;i=1009")


value=0
val2.set_value(value, ua.VariantType.Int16)

