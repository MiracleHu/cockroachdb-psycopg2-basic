import psycopg2
from conn import db_conn


def deleteData(mobileId):
    try:
        connection = db_conn()

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from mobile where id = %s"""
        cursor.execute(sql_delete_query, (mobileId, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


id4 = 4
id5 = 5
deleteData(id4)
deleteData(id5)
