import psycopg2

try:
    #you have to be connected to an existing database in postgres to execute any instructions on it
    conn = psycopg2.connect(database="db name", user="dbadmin", password="***", host="ip addr", port="5432")
except psycopg2.Error as err:
    print(err)
else:
    print('Connection Successful!')
    
cursor = conn.cursor()

cursor.execute("SELECT * FROM athletes where year ='2018'")

query_result = cursor.fetchall()

for result in query_result:
    print(result)

conn.commit()
conn.close()
