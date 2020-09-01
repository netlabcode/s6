import binascii
import _thread
import time
import socket


HOST1 = '10.1.0.11'
HOST1B = '10.1.0.12'
HOST1C = '10.1.0.13'
HOST1D = '10.1.0.14'
HOST1E = '10.1.0.15'
HOST1F = '10.1.0.16'
HOST2 = '10.1.0.31'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1B:
			sc1B.connect((HOST1B, PORT1))

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1C:
				sc1C.connect((HOST1C, PORT1))

				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1D:
					sc1D.connect((HOST1D, PORT1))

					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1E:
						sc1E.connect((HOST1E, PORT1))

						with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1F:
							sc1F.connect((HOST1F, PORT1))

							with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
								s1.bind((HOST2,PORTS1))
								s1.listen()
								conn1, addr = s1.accept()
								with conn1:
									print('S1 from:',addr)
									while True:
										a = 1
										while a < 6:
											#recive data from server A
											data1 = sc1.recv(1024)
											data1b = sc1B.recv(1024)
											data1c = sc1C.recv(1024)
											data1d = sc1D.recv(1024)
											data1e = sc1E.recv(1024)
											data1f = sc1F.recv(1024)

											strval1 = "mu01+"+str(data1.decode("utf-8"))
											strval1b = "mu02+"+str(data1b.decode("utf-8"))
											strval1c = "mu03+"+str(data1c.decode("utf-8"))
											strval1d = "mu04+"+str(data1d.decode("utf-8"))
											strval1e = "mu05+"+str(data1e.decode("utf-8"))
											strval1f = "mu06+"+str(data1f.decode("utf-8"))

											datanew1 = strval1.encode()
											datanew2 = strval1b.encode()
											datanew3 = strval1c.encode()
											datanew4 = strval1d.encode()
											datanew5 = strval1e.encode()
											datanew6 = strval1f.encode()


											#send data to server C
											conn1.sendall(datanew1)
											time.sleep(0.1)
											conn1.sendall(datanew2)
											time.sleep(0.1)
											conn1.sendall(datanew3)
											time.sleep(0.1)
											conn1.sendall(datanew4)
											time.sleep(0.1)
											conn1.sendall(datanew5)
											time.sleep(0.1)
											conn1.sendall(datanew6)

											#print('S1:',strval1)
											#print('S2:',strval1b)
							


# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2:
		sc2.connect((HOST1, PORT2))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2B:
			sc2B.connect((HOST1B, PORT2))

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2C:
				sc2C.connect((HOST1C, PORT2))

				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2D:
					sc2D.connect((HOST1D, PORT2))

					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2E:
						sc2E.connect((HOST1E, PORT2))

						with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2F:
							sc2F.connect((HOST1F, PORT2))

							with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
								s2.bind((HOST2,PORTS2))
								s2.listen()
								conn2, addr2 = s2.accept()
								with conn2:
									print('S2 from:',addr2)
									while True:
										b = 1
										while b < 6:
											#recive data from server A
											data2 = conn2.recv(1024)
											data2new = data2.decode("utf-8")
											if 'mu01' in data2new:
												part1,part2 = data2new.split("_")
												print(part2)
												part2x = part2.encode()
												sc2.sendall(part2x)
											elif 'mu02' in data2new:
												part1,part2 = data2new.split("_")
												print(part2)
												part2x = part2.encode()
												sc2B.sendall(part2x)
											elif 'mu03' in data2new:
												part1,part2 = data2new.split("_")
												print(part2)
												part2x = part2.encode()
												sc2C.sendall(part2x)
											elif 'mu04' in data2new:
												part1,part2 = data2new.split("_")
												print(part2)
												part2x = part2.encode()
												sc2D.sendall(part2x)
											elif 'mu05' in data2new:
												part1,part2 = data2new.split("_")
												print(part2)
												part2x = part2.encode()
												sc2E.sendall(part2x)
											elif 'mu06' in data2new:
												part1,part2 = data2new.split("_")
												print(part2)
												part2x = part2.encode()
												sc2F.sendall(part2x)
											else:
												print(".")

											#send data to server C
											#sc2.sendall(data2)
											#sc2B.sendall(data2)
							

						

# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
