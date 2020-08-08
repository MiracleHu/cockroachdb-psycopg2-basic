import psycopg2


def db_conn():
    connection = psycopg2.connect(user='root',
                                  host="127.0.0.1",
                                  port="26257",
                                  sslmode='disable',
                                  database="test_db",
                                  connect_timeout=10)
    return connection
