import psycopg2
import sys
# need sys.path to parse the utils package
sys.path.extend(["/Users/huanlehu/Documents/Tut_Learning/DockerTut/docker_CockroachDB"])
from utils.conn import db_conn

try:
   connection = db_conn()
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from mobile"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
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

'''
Note: In the above example, we used cursor.fetchall() to get all the rows of a database table.

Use cursor.execute() to run a query then use.

cursor.fetchall() to fetch all rows.
cursor.fetchone() to fetch single row.
cursor.fetchmany(SIZE) to fetch limited rows
'''