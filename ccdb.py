import binascii
import _thread
import time
import socket
import time
import sqlite3
from sqlite3 import Error
import datetime


HOST2 = '10.1.0.31'
PORT1 = 881
PORT2 = 883


def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file, timeout=10)
	except Error as e:
		print(e)
	return conn

def db_connect():
	datafile="cc.db"
	con = create_connection(datafile)
	return con

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((HOST2, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data1 = s1.recv(1024)
			data1new = data1.decode("utf-8")

			#save db
			con = db_connect()
			c = con.cursor()
			datet = datetime.datetime.now()

			#print(data1new)


			if 'mu01' in data1new:
				try:
					n,a,b,ce,d,e,f = data1new.split("+")
					c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl, B23_Li_23_24_CB_res, B23_Li_23_24_I_res, B23_Li_23_24_P_res, B23_Li_23_24_Q_res, B23_Li_23_24_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
					print(a)
				except Exception:
					print("mu1")
					pass
			elif 'mu02' in data1new:
				try:
					n,a,b,ce,d,e,f = data1new.split("+")
					c.execute("INSERT INTO mu02(xtime, B23_Li_22_23_CB_ctrl, B23_Li_22_23_CB_res, B23_Li_22_23_I_res, B23_Li_22_23_P_res, B23_Li_22_23_Q_res, B23_Li_22_23_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
					print(a)
				except Exception:
					print("mu2")
					pass
			elif 'mu03' in data1new:
				try:
					n,a,b,ce,d,e,f,g,h,i,j,k,l,m = data1new.split("+")
					c.execute("INSERT INTO mu03(xtime, B23_Ld_V_res, B23_Tr_CB_ctrl, B23_Tr_CB_res, B23_Tr_f_res, B23_Tr_hv_P_res, B23_Tr_hv_Q_res, B23_Tr_Ld_res, B23_Tr_lv_P_res, B23_Tr_lv_Q_res, B23_Tr_tap, B23_Tr_tap_ctrl, B23_Tr_tap_mode, B23_Tr_tap_res) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datet,float(a),int(b),int(ce),float(d),float(e),float(f),float(g),float(h),float(i),int(j),int(k),int(l),int(m)))
					print(a)
				except Exception:
					print("mu3")
					pass
			elif 'mu04' in data1new:
				try:
					n,a,b,ce,d,e,f = data1new.split("+")
					c.execute("INSERT INTO mu04(xtime, B23_Ld_CB_ctrl, B23_Ld_CB_res, B23_Ld_I_res, B23_Ld_P_res, B23_Ld_Q_res, B23_Tr_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
					print(a)
				except Exception:
					print("mu4")
					pass
			elif 'mu05' in data1new:
				try:
					n,a,b = data1new.split("+")
					c.execute("INSERT INTO mu05(xtime, B36_Tr_CB_ctrl, B36_Tr_CB_res) VALUES (?,?,?)",(datet,int(a),int(b)))
					print(a)
				except Exception:
					print("mu5")
					pass
			elif 'mu06' in data1new:
				try:
					n,a,b,ce,d,e,f,g,h,i = data1new.split("+")
					c.execute("INSERT INTO mu06(xtime, B36_G7_CB_ctrl, B36_G7_CB_res, B36_G7_f_res, B36_G7_Ld_res, B36_G7_P_ctrl, B36_G7_P_res, B36_G7_Q_res, B36_G7_V_ctrl, B36_G7_V_res) VALUES (?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g),float(h),float(i)))
					print(a)
				except Exception:
					print("mu6")
					pass
			else:
				print('.')

			con.commit()
			con.close()

			#print('Data:',data1new)
			#print(type(data1new))


# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((HOST2, PORT2))
		x = 1
		value=0
		while x < 6:

			time.sleep(1)

			#covert inetger to string
			value = value+5
			stringd = str(value)

			#stringd = str(value1)+"-"+str(value2)+"-"+str(value3)

			#convert string to bytes data
			data2 = stringd.encode()

			s2.sendall(data2)






# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   #_thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
