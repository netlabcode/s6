#!/user/bin/env python3
import psycopg2

try:
	conn = psycopg2.connect("host='131.180.165.5' dbname='postgres' user='postgres' password='----'")
	print("Connection established")
except:
	print("Connection Fail")

