import binascii
import _thread
import time
import socket
import time
import sqlite3
from sqlite3 import Error
import datetime

#Predefined parameters
HOST2 = '10.1.0.31'
MU01 = '10.1.0.11'
MU02 = '10.1.0.12'
PORT1 = 991
PORT2 = 992

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file, timeout=10)
	except Error as e:
		print(e)
	return conn

def db_connect():
	datafile="s06.db"
	con = create_connection(datafile)
	return con


# Define a function for the thread
def serverMU01():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((MU01, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data1 = s1.recv(1024)

			#parsing data
			data1new = data1.decode("utf-8")

			print (data1new)

			"""
			a,b,ce,d,e,f = data1new.split("-")

			#save db
			con = db_connect()
			c = con.cursor()
			datet = datetime.datetime.now()
			c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl, B23_Li_23_24_CB_res, B23_Li_23_24_I_res, B23_Li_23_24_P_res, B23_Li_23_24_Q_res, B23_Li_23_24_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
			#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
			con.commit()
			con.close()
			
			try: 
				
			except Exception:
				print("mu01")
				pass
			"""



def serverMU02():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU02, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				a,b,ce,d,e,f = data1new.split("-")
				#save db
				con = db_connect()
				c = con.cursor()
				datet = datetime.datetime.now()
				c.execute("INSERT INTO mu02(xtime, B23_Li_22_23_CB_ctrl, B23_Li_22_23_CB_res, B23_Li_22_23_I_res, B23_Li_22_23_P_res, B23_Li_22_23_Q_res, B23_Li_22_23_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu02")
				pass




# Create two threads as follows
try:
   _thread.start_new_thread( serverMU01, ( ) )
   _thread.start_new_thread( serverMU02, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
