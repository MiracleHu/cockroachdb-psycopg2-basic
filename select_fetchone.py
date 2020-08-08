import psycopg2
from conn import db_conn
'''
Using cursor.fetchone
1. Use a cursor.fetchone() to retrieve only a single row from the PostgreSQL table in Python.
2. You can also use cursor.fetchone() to fetch the next row of a query result set. This method returns a single tuple.
3. It can return a none if no rows are available in the resultset.
4. The cursor.fetchall() and fetchmany() method internally uses this method.
'''
try:
   connection = db_conn()

   PostgreSQL_select_Query = "select * from mobile"
   cursor = connection.cursor()

   cursor.execute(PostgreSQL_select_Query)

   mobile_records_one = cursor.fetchone()
   print ("Printing first record", mobile_records_one)

   mobile_records_two = cursor.fetchone()
   print("Printing second record", mobile_records_two)

except (Exception, psycopg2.Error) as error :
    print ("Error while getting data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
