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
			a,b,ce,d,e,f = data1new.split("-")
			print(type(a))
			print(type(d))

			#save db
			con = db_connect()
			c = con.cursor()
			datet = datetime.datetime.now()
			c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl, B23_Li_23_24_CB_res, B23_Li_23_24_I_res, B23_Li_23_24_P_res, B23_Li_23_24_Q_res, B23_Li_23_24_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
			#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
			con.commit()
			con.close()



def serverMU02():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU02, PORT1))
		b = 1
		while b < 6:
			#recive data from server
			data2 = s2.recv(1024)
			print('MU02:',data2)

# Define a function for the thread
def serverXMU01():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx1:
		sx1.connect((MU01, PORT2))
		ax = 1
		value1x=0
		while ax < 6:
			#covert inetger to string
			value1x = value1x+3
			string1x = str(value1x)

			#stringd = str(value1)+"-"+str(value2)+"-"+str(value3)

			#convert string to bytes data
			data1x = string1x.encode()

			sx1.sendall(data1x)
			time.sleep(2)

def serverXMU02():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx2:
		sx2.connect((MU02, PORT2))
		bx = 1
		value2x=0
		while bx < 6:
			#covert inetger to string
			value2x = value2x+25
			string2x = str(value2x)

			string2x = str(input("Command entry: "))

			#stringd = str(value1)+"-"+str(value2)+"-"+str(value3)

			#convert string to bytes data
			data2x = string2x.encode()

			sx2.sendall(data2x)
			print(data2x)
			time.sleep(5)
			#sx2.close()




# Create two threads as follows
try:
   #_thread.start_new_thread( serverMU01, ( ) )
   #_thread.start_new_thread( serverMU02, ( ) )
   _thread.start_new_thread( serverXMU01, ( ) )
   _thread.start_new_thread( serverXMU02, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
