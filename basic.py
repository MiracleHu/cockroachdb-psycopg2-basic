import psycopg2

try:
    dsn = 'postgresql://root@localhost:26257/test_db?sslmode=disable'
    connection = psycopg2.connect(dsn)
    # connection = psycopg2.connect(user = 'root',
    #                               host = "127.0.0.1",
    #                               port = "26257",
    #                               sslmode = 'disable',
    #                               database = "test_db",
    #                               connect_timeout=10)


    # #cursor = connection.cursor()
    # 1. Using connection.cursor() we can create a cursor object which allows us to execute PostgreSQL command through Python source code.
    # 2. We can create as many cursors as we want from a single connection object. Cursors created from the same connection are not isolated,
    #    ****i.e., any changes done to the database by a cursor are immediately visible by the other cursors!!!****
    # 3. Cursors are not thread-safe.

    # After this, we printed PostgreSQL Connection properties using a connection.get_dsn_parameters().
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    #  #cursor.execute()
    # Using the cursor’s execute method we can execute a database operation or query.
    # Execute method takes a SQL query as a parameter.
    # We can retrieve query result using cursor methods such as fetchone(), fetchmany(), fetcthall().
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        #  ##cursor.close()  and connection.close()
        # It is always good practice to close the cursor and connection object once your work gets completed to avoid database issues.
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
