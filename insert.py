import psycopg2
from psycopg2 import Error
from conn import db_conn

try:
    connection = db_conn()

    cursor = connection.cursor()
    """
    We used a parameterized query to pass parameter values at execution time. 
    In the end, we make our changes persistent into the database using the cursor.commit method.
    Using a parameterized query we can pass python variables as a query parameter in which we use placeholders (%s) for parameters

    https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/#What_is_parameterized_query_in_python

    """
    postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
    record_to_insert = (5, 'One Plus 6', 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, Error) as error:
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
