import psycopg2
from conn import db_conn

def updateInBulk(records):
    try:
        connection = db_conn()
        cursor = connection.cursor()

        # Update multiple records
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.executemany(sql_update_query, records)
        connection.commit()
        # Use cursor.rowcount to get the total number of rows affected by the executemany() method
        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

tuples = [(750, 2), (950, 1)]
updateInBulk(tuples)
