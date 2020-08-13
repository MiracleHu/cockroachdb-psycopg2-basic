
## Quick Start Using Pipenv

``` bash
# Install pipenv if there is no pipenv
$ pip3 install pipenv

# Activate venv
$ pipenv shell

# Install dependencies in Pipfile
# if there is no Pipfile, you can install manully and a Pipfile will be created and save all the dependence packages:
# $ pipenv install flask flask_restful flask_jwt
# if your project dependencies file is requirements.txt, you can use this :
# $ pipenv install -r /path/to/your/requirements.txt
$ pipenv install # pipenv install psycopg2-binary

# setup DB
$ docker-compose up

# Access CockroachDB running on a Docker container, user docker ps to check the name
$ docker exec -it {CONTAINER_NAME or ID} /bin/bash

# Ater entering CockroachDB docker container, run db shell
$ ./cockroach sql --insecure

# Show databases in CockroachDB shell
$ SHOW DATABASES;

# Create a database in CockroachDB shell
$ CREATE DATABASE test_db;

# Show tables in CockroachDB shell
$ use test_db;
$ show tables;

# Quit cockroachDB shell
$ \q

# Quit docker container
$ exit


# Database WebUI, check your docker container setting
'http://localhost:8081/#/overview/list'

# Run script 
$ python app.py

# tricks for debugging:
# Enter python environment
$ python

# Run the script 
$ >>> exec(open('main.py').read())

# Then you can get access the variable directly
$ >>> x

# Or you can wrap main as a module
$ >>> import main
$ >>> main.x

```

## The result set returned by the stored procedure using the  fetchone(),  fetchall(), or  fetchmany() method
- ### The fetchone() fetches the next row in the result set. It returns a single tuple or None when no more row is available.

- ### The fetchmany(size=cursor.arraysize) fetches the next set of rows specified by the size parameter. If you omit this parameter, the arraysize will determine the number of rows to be fetched. The  fetchmany() method returns a list of tuples or an empty list if no more rows available.

- ### The fetchall() fetches all rows in the result set and returns a list of tuples. If there are no rows to fetch, the  fetchall() method returns an empty list.