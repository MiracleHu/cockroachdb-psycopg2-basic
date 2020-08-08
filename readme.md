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

# Run script 
$ python app.py


```
