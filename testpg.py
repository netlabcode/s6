import psycopg2
from datetime import datetime
import time
 
conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")

#Check Connection
if conn is not None:
    print('Connection established to PostgreSQL.')
else:
    print('Connection not established to PostgreSQL.')


#Setting auto commit 
conn.autocommit = True

cursor = conn.cursor()
cursor.execute('''SELECT value from objects WHERE id=1''')
result = cursor.fetchone();
print(result[0])

#Select Data
"""
record1 = result[0]
x = 1
while x < 6:
	cursor.execute('''SELECT value from objects WHERE id=1''')
	result = cursor.fetchone();
	if record1 != result[0]:
		print(result[0])
		record1 = result[0]
	time.sleep(1)
"""






#Creating a cursor object using the cursor() method
cursor = conn.cursor()

dt = datetime.now()

inserted_values = (
        dt
    )


# INSTER VALUE TO TABLE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
cursor.execute('''INSERT INTO s17m1(cb_ctrl) VALUES (3)''')


a=2
b=3

inserted_values = (
        		a,
        		b
    		)

cursor.execute(" INSERT INTO s17m1(v_ctrl, v_res) VALUES (%s,%s)", inserted_values)



"""
# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO test(val, dec, dtime) VALUES (33, -999.123456, dt)''')
"""

"""
cursor.close()
"""
conn.close()