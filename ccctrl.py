import binascii
import _thread
import time
import socket
import time
import sqlite3
from sqlite3 import Error
import datetime

#Predefined parameters
HOST = '10.1.0.31'
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
	datafile="s06.db"
	con = create_connection(datafile)
	return con


# Define a function for the thread
def ccControl():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx1:
		sx1.connect((HOST, PORT2))
		ax = 1
		value1x=0
		while ax < 6:
			#covert inetger to string
			value1x = value1x+3
			string1x = str(value1x)

			#stringd = str(value1)+"-"+str(value2)+"-"+str(value3)
			print("Format: mu01_id+value")
			string1x = str(input("Command entry: "))

			#convert string to bytes data
			data1x = string1x.encode()

			sx1.sendall(data1x)
			time.sleep(1)


# Create two threads as follows
try:
   #_thread.start_new_thread( serverMU01, ( ) )
   #_thread.start_new_thread( serverMU02, ( ) )
   _thread.start_new_thread( ccControl, ( ) )
   #_thread.start_new_thread( serverXMU02, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
