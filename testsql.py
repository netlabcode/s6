#!/user/bin/env python3
import psycopg2

try:
	conn = psycopg2.connect("host='131.180.165.5' dbname='postgres' user='postgres' password='c'")
	print("Connection established")

	cursor = conn.cursor()

	cursor.execute("SELECT name FROM test")

	rows = cursor.fetchall()

	for row in rows:
		print(row)

	cursor.close()

except:
	print("Connection Fail")

