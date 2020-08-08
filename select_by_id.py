import psycopg2
from conn import db_conn

def getMobileDetails(mobileID):
    try:
        connection = db_conn()

        print("Using Python variable in PostgreSQL select Query")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from mobile where id = %s"

        cursor.execute(postgreSQL_select_Query, (mobileID,))
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            print("Id = ", row[0], )
            print("Model = ", row[1])
            print("Price  = ", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed \n")

getMobileDetails(1)
getMobileDetails(2)