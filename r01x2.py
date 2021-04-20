import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 8801
 




"""
s1 = socket.socket()
host = socket.gethostname()

def server():
    s1.bind(('',PORT1))
    s1.listen()
    conn1, addr = s1.accept()
    while True:
        print('Server 1 from:',addr)
        #Format: mu01_id+value
        cursor.execute('''SELECT value from objects WHERE id=1''')
        result = cursor.fetchone()
        if record1 != result[0]:
            print(result[0])
            string = "mu01_"+str(r1)+"+"+str(result[0])
            datax = string.encode()
            conn1.sendall(datax)
            print(string)
            record1 = result[0]
    s1.close()
    server()

server()
"""
def serverX():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
            s1.bind(('',PORT1))
            s1.listen()
            conn1, addr = s1.accept()
            with conn1:
                print('Server 1 from:',addr)

                conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")
                  
                cursor = conn.cursor()
                
                #Value id 1-7
                cursor.execute('''SELECT value from objects WHERE id=1''')
                result = cursor.fetchone()
                record1 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=2''')
                result = cursor.fetchone()
                record2 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=3''')
                result = cursor.fetchone()
                record3 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=4''')
                result = cursor.fetchone()
                record4 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=5''')
                result = cursor.fetchone()
                record5 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=6''')
                result = cursor.fetchone()
                record6 = result[0]

                #Value code
                cursor.execute('''SELECT code from objects WHERE id=1''')
                result = cursor.fetchone()
                r1 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=2''')
                result = cursor.fetchone()
                r2 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=3''')
                result = cursor.fetchone()
                r3 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=4''')
                result = cursor.fetchone()
                r4 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=5''')
                result = cursor.fetchone()
                r5 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=6''')
                result = cursor.fetchone()
                r6 = result[0]

                while True:
                    data = "a"
                    datax = data.encode()
                    try:
                        


                        """
                        cursor.execute('''SELECT value from objects WHERE id=1''')
                        result = cursor.fetchone()
                        if record1 != result[0]:
                            print(result[0])
                            string = "mu01_"+str(r1)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record1 = result[0]
                        """

                        conn1.sendall(datax)
                        print(r1)
                        conn.close()
                        time.sleep(1)
                        
                    except:
                        conn1.close()
                        conn.close()
                        print("Connection Close")
                        break
                
                conn1.close()
                print("Restart Server")
                conn.close()
                s1.close()
                time.sleep(1)
                serverX()

serverX()
            


"""
def serverX():                   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.bind(('',PORT1))
        s1.listen()
        conn1, addr = s1.accept()
        with conn1:
            print('Server 1 from:',addr)

            while True:
                #Format: mu01_id+value
                cursor.execute('''SELECT value from objects WHERE id=1''')
                result = cursor.fetchone()
                if record1 != result[0]:
                    print("a")
                a = 1
                while a < 6:

                    #Format: mu01_id+value
                    cursor.execute('''SELECT value from objects WHERE id=1''')
                    result = cursor.fetchone()
                    if record1 != result[0]:
                        print(result[0])
                        string = "mu01_"+str(r1)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record1 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=2''')
                    result = cursor.fetchone()
                    if record2 != result[0]:
                        print(result[0])
                        string = "mu02_"+str(r2)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record2 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=3''')
                    result = cursor.fetchone()
                    if record3 != result[0]:
                        print(result[0])
                        string = "mu03_"+str(r3)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record3 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=4''')
                    result = cursor.fetchone()
                    if record4 != result[0]:
                        print(result[0])
                        string = "mu04_"+str(r4)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record4 = result[0]
                        
                    cursor.execute('''SELECT value from objects WHERE id=5''')
                    result = cursor.fetchone()
                    if record5 != result[0]:
                        print(result[0])
                        string = "mu04_"+str(r5)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record5 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=6''')
                    result = cursor.fetchone()
                    if record6 != result[0]:
                        print(result[0])
                        string = "mu04_"+str(r6)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record6 = result[0]
            s1.close()

            serverX()
try:
    serverX()
except:
   print ("Error: unable to start thread")
   conn.close()


while 1:
   pass
"""

