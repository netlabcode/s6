#!/user/bin/env python3
import psycopg2

try:
	conn = psycopg2.connect("host='131.180.165.5' dbname='sample' user='postgres' password='crpg'")
	print("Connection established")
except:
	print("Connection Fail")

