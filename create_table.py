import psycopg2
from psycopg2 import Error

try:
    dsn = 'postgresql://root@localhost:26257/test_db?sslmode=disable'
    connection = psycopg2.connect(dsn)
    # connection = psycopg2.connect(user='root',
    #                               host="127.0.0.1",
    #                               port="26257",
    #                               sslmode='disable',
    #                               database="test_db",
    #                               connect_timeout=10)

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS mobile 
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
