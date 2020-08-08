import psycopg2
from conn import db_conn

'''
Cursor.executemany() to insert, update and delete multiple rows into the PostgreSQL table
The cursor.executemany() method executes the database query against all the parameters.

For example, Most of the time you required to run the same query multiple times but with different data. 
Like update attendance of the student, here attendance percentage is different but the SQL query is the same.

Use cursor.executemany() method to insert, update, delete multiple rows of a table using a single query.
Syntax of executemany():

  executemany(query, vars_list)

1. Here query can be any DML query (Insert, update, delete)
2. The vars_list is nothing but the list of tuples as an input to the query.
3. Each tuple in this list contains a single row of data to be inserted or updated into a table.

'''
def bulkInsert(records):
    try:
        connection = db_conn()
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO mobile (id, model, price) 
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows rows, execute() only insert one row
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".format(error))

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


records_to_insert = [(1, 'Apple iPhone X', 1000), (2, 'Samsung Galaxy', 900)]
bulkInsert(records_to_insert)
