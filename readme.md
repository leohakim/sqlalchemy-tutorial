# SQL Alchemy Tutorial

SQLAlchemy Tutorial is a Python example code for understand the uses of SQLAlchemy ORM and how Docker Compose handle the
connections between PostgreSQL container and PGAdmin container .

For connect PGAdmin to PostgreSQL Server in docker the IP
address is 0.0.0.0 (like Docker shows when you run the command "docker ps")

## Installation

Use pipenv to install the enviroment with his dependencies:

```bash
pipenv shell
```

Start the containers with start.sh script:

```bash
source start.sh
```

## Usage

#### Set the string connection in base.py

(This string connection works for PostgreSQL Server set in docker-compose.yml)

```python
string_connection = 'postgresql://user:admin@0.0.0.0:5432/sqlalchemy'
```

#### Insert rows into PGSQL db

```bash
python inserts.py
```

#### Execute querys into PGSQL db

```bash
python queries.py
```

## Stop and Destroy Containers

Stop the containers with stop.sh script:

```bash
source stop.sh
```

Destroy the containers with destroy.sh script:

```bash
source destroy.sh
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)