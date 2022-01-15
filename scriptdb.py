import openpyxl
import psycopg2
import time


try:
    conn = psycopg2.connect(database="rich_sports", user="dbadmin", password="qrtyac11", host="167.172.255.170", port="5432")
except psycopg2.Error as prntErr:
    print(prntErr)
else:
    print('Connection Successful!')


conn.autocommit=True

cursor = conn.cursor()

# #create database

# sql_stmt = "CREATE DATABASE rich_sports";

# cursor.execute(sql_stmt)

# #create table



# cursor.execute('''CREATE TABLE athletes(
# name varchar(50) not null,
# country varchar(25) not null,
# sport varchar(50) not null,
# year bigint not null,
# earnings numeric not null
# );''')

# #adding data to the database

csvbook = openpyxl.load_workbook(r"C:\Users\Ryan\pyprojects\dbproj\newrichathletes.xlsx")

sheet_with_data = csvbook['Worksheet']

for i in sheet_with_data.values:
    cursor.execute("INSERT INTO athletes (name, country, sport, year, earnings) values (%s, %s, %s, %s, %s,);",(i[0], i[1], i[2], i[3], i[4]))


# print("Database Created")
# print("Table Created")
print("Data inserted into Database")



conn.commit()
conn.close()
