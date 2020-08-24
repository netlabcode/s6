from opcua import Server
from opcua import ua
from opcua import Client
from random import randint
import datetime
import time

server = Server()
url = "opc.tcp://0.0.0.0:8899/freeopcua/server/"
server.set_endpoint(url)

name="OPC_UA_SERVER"
addspace = server.register_namespace(name)

#Define Variant Data Type  2 = Integer ; 4 = float
variant = None
variant = ua.Variant(0, ua.VariantType.Int16)

variant2 = None
variant2 = ua.Variant(0, ua.VariantType.Float)



node = server.get_objects_node()
Param = node.add_object(addspace,"Substation")


S3_M3_B25_TR_tap_mode = Param.add_variable(addspace,"S3_M3_B25_TR_tap_mode",variant2)
S3_M3_B25_TR_tap_mode.set_writable(True)
S3_M3_B25_TR_tap = Param.add_variable(addspace,"S3_M3_B25_TR_tap",variant2)
S3_M3_B25_TR_tap.set_writable(True)
S3_M3_B25_TR_tap_res = Param.add_variable(addspace,"S3_M3_B25_TR_tap_res",variant2)
S3_M3_B25_TR_tap_res.set_writable(True)
S3_M3_B25_TR_Ld_res = Param.add_variable(addspace,"S3_M3_B25_TR_Ld_res",variant2)
S3_M3_B25_TR_Ld_res.set_writable(True)
S3_M3_B25_TR_f_res = Param.add_variable(addspace,"S3_M3_B25_TR_f_res",variant2)
S3_M3_B25_TR_f_res.set_writable(True)
S3_M3_B25_TR_V_res = Param.add_variable(addspace,"S3_M3_B25_TR_V_res",variant2)
S3_M3_B25_TR_V_res.set_writable(True)
S3_M4_B25_Li_25_26_CB = Param.add_variable(addspace,"S3_M4_B25_Li_25_26_CB",variant2)
S3_M4_B25_Li_25_26_CB.set_writable(True)
S3_M4_B25_Li_25_26_CB_res = Param.add_variable(addspace,"S3_M4_B25_Li_25_26_CB_res",variant2)
S3_M4_B25_Li_25_26_CB_res.set_writable(True)
S3_M4_B25_Li_25_26_P_res = Param.add_variable(addspace,"S3_M4_B25_Li_25_26_P_res",variant2)
S3_M4_B25_Li_25_26_P_res.set_writable(True)
S3_M4_B25_Li_25_26_Q_res = Param.add_variable(addspace,"S3_M4_B25_Li_25_26_Q_res",variant2)
S3_M4_B25_Li_25_26_Q_res.set_writable(True)
S3_M4_B25_Li_25_26_I_res = Param.add_variable(addspace,"S3_M4_B25_Li_25_26_I_res",variant2)
S3_M4_B25_Li_25_26_I_res.set_writable(True)
S3_M5_B37_TR_CB = Param.add_variable(addspace,"S3_M5_B37_TR_CB",variant2)
S3_M5_B37_TR_CB.set_writable(True)
S3_M5_B37_TR_CB_res = Param.add_variable(addspace,"S3_M5_B37_TR_CB_res",variant2)
S3_M5_B37_TR_CB_res.set_writable(True)
S3_M6_B37_G8_CB = Param.add_variable(addspace,"S3_M6_B37_G8_CB",variant2)
S3_M6_B37_G8_CB.set_writable(True)
S3_M6_B37_G8_CB_res = Param.add_variable(addspace,"S3_M6_B37_G8_CB_res",variant2)
S3_M6_B37_G8_CB_res.set_writable(True)
S3_M6_B37_G8_P_ctrl = Param.add_variable(addspace,"S3_M6_B37_G8_P_ctrl",variant)
S3_M6_B37_G8_P_ctrl.set_writable(True)
S3_M6_B37_G8_P_res = Param.add_variable(addspace,"S3_M6_B37_G8_P_res",variant2)
S3_M6_B37_G8_P_res.set_writable(True)
S3_M6_B37_G8_Q_res = Param.add_variable(addspace,"S3_M6_B37_G8_Q_res",variant2)
S3_M6_B37_G8_Q_res.set_writable(True)
S3_M6_B37_G8_V_ctrl = Param.add_variable(addspace,"S3_M6_B37_G8_V_ctrl",variant)
S3_M6_B37_G8_V_ctrl.set_writable(True)
S3_M6_B37_G8_V_res = Param.add_variable(addspace,"S3_M6_B37_G8_V_res",variant2)
S3_M6_B37_G8_V_res.set_writable(True)
S3_M6_B37_G8_f_res = Param.add_variable(addspace,"S3_M6_B37_G8_f_res",variant2)
S3_M6_B37_G8_f_res.set_writable(True)
S3_M6_B37_G8_Ld_res = Param.add_variable(addspace,"S3_M6_B37_G8_Ld_res",variant2)
S3_M6_B37_G8_Ld_res.set_writable(True)


server.start()

print("Server start at {}".format(url))

"""
i = 1
while i < 5:

    time.sleep(0.001)

 

server.stop()
"""


"""
idx = server.register_namespace(uri)
server.start()
objects = server.get_objects_node()
self.pfGroup = objects.add_object(idx, "PF")
pfVar = self.pfGroup.add_variable(idx, var.aliasName, variant)

"""

