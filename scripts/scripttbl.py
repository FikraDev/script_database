import psycopg2
import openpyxl

try:
    # you have to be connected to an existing database in postgres to execute any instructions on it
    conn = psycopg2.connect(database="db name", user="dbadmin",password="***", host="ip addr", port="5432")
except psycopg2.Error as err:
    print(err)
else:
    print('Connection Successful!')

try:
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE athletes(
    name varchar(50) not null,
    country varchar(25) not null,
    sport varchar(50) not null,
    year varchar(255) not null,
    earnings varchar(255) not null
    );''')
except psycopg2.Error as err:
    print(err)
else:
    print("Table Created Successfully")

# #adding data to the database

csvbook = openpyxl.load_workbook(
    r"C:\Users\fikra\pyprojects\dbproj\newrichathletes.xlsx")

sheet_with_data = csvbook['Worksheet']

for i in sheet_with_data.values:
    cursor.execute('''INSERT INTO athletes (name, country, sport, year, earnings) values (%s, %s, %s, %s, %s);''',
                   (i[0], i[1], i[2], i[3], i[4]))

print("Data inserted into Database")

conn.commit()
conn.close()
