#!/user/bin/env python3
import psycopg2

try:
	conn = psycopg2.connect("host='131.180.165.5' dbname='sample' user='postgres' password='Rahasia123'")
	print("Connection established")
except:
	print("Connection Fail")

