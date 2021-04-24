pipenv shell 
docker run -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=user -e POSTGRES_DB=sqlalchemy -p 5432:5432 -d postgres
