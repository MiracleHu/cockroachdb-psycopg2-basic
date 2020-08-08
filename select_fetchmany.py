import psycopg2
from conn import db_conn
'''
In most of the situation retrieving all of the rows from a table can be time-consuming if the table contains thousands of rows.

So a better alternative is to retrieve a few rows using a cursor.fetchmany().

Syntax of fetchmany():
    cursor.fetchmany([size=cursor.arraysize])

1. Here size is the number of rows to be retrieved.

2. This method fetches the next set of rows from a query result. fetchmany() method return a list of tuple contains the rows.

3. fetchmany returns an empty list when no more rows are available in the table.
   The number of rows to fetch depends on the SIZE argument. A ProgrammingError raised 
   if the previous call to execute*() did not produce any result set or no call issued yet.

4. fetchmany() returns fewer rows if the table contains the less number of rows specified by SIZE argument.
'''
try:
   connection = db_conn()

   print("Selecting rows from mobile table using cursor.fetchall")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from mobile"

   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchmany(2)
   
   print("Printing 2 rows")
   for row in mobile_records:
       print("Id = ", row[0], )
       print("Model = ", row[1])
       print("Price  = ", row[2], "\n")

   mobile_records = cursor.fetchmany(2)
   
   print("Printing next 2 rows")
   for row in mobile_records:
       print("Id = ", row[0], )
       print("Model = ", row[1])
       print("Price  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")