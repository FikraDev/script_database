import psycopg2

try:
    #you have to be connected to an existing database in postgres to execute any instructions on it
    conn = psycopg2.connect(database="db name", user="dbadmin", password="***", host="ip addr", port="5432")
except psycopg2.Error as err:
    print(err)
else:
    print('Connection Successful!')

cursor = conn.cursor()


#create database

conn.autocommit=True

sql_stmt = "CREATE DATABASE rich_sports";

cursor.execute(sql_stmt)
