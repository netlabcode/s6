#!/user/bin/env python3
import psycopg2

try:
	conn = psycopg2.connect("host='127.0.0.1' dbname='sample' user='postgres' password='Rahasia123'")
	print("Connection established")
except:
	print("Connection Fail")

