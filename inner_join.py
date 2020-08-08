import psycopg2
from conn import db_conn

def get_doctors(hospital_id):
    try:
        connection = db_conn()

        print("Using Python variable in PostgreSQL select Query")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from doctor inner join hospital on doctor.Hospital_Id = hospital.Hospital_Id where doctor.Hospital_Id = %s"

        cursor.execute(postgreSQL_select_Query, (hospital_id,))
        records = cursor.fetchall()
        for row in records:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed \n")


get_doctors(2)