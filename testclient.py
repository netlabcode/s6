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
#url = "opc.tcp://srv786:62640/IntegrationObjects/ServerSimulator"

client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=3;i=1")
val2 = client.get_node("ns=3;i=2")
val3 = client.get_node("ns=3;i=3")

#val1 = client.get_node("ns=7;s=PF.v_res")
#val2 = client.get_node("ns=7;s=PF.cb_ctrl")


value = 0
while value < 3:
    value1 = val1.get_value()
    value2 = val2.get_value()
    value3 = val3.get_value()
    print(value1)
    print(value2)
    print(value3)
    print("===")
    time.sleep(1)
