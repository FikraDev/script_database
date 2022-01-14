import openpyxl
import psycopg2

try:
    conn = psycopg2.connect(database="base_db", user="dbadmin", password="qrtyac11", host="167.172.255.170", port="5432")
except psycopg2.Error as prntErr:
    print(prntErr)
else:
    print('Connection Successful!')

#conn.commit()
#connection.close()
