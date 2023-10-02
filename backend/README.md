## Building & running the database

1. Clone repo
1. Install docker
1.  Build and run the DB container

    `make start-db`

    or

    ```
    cd backend
    docker-compose -f docker-compose.yml up -d db
    ```

1. Setting up the database

    `make db-migrate`

    or

    ```
    cd backend
    alembic upgrade head
    ```

**Note: run `make` or `make help` in project root for other useful make options**

### Database operations and maintenance

#### Generating Alembic migrations

This is only necessary when making changes to models/schema

`alembic revision --autogenerate -m “<descriptive message here>”`

#### Destroying containers

If you need to teardown the DB:

`make destroy-containers`

or

```
cd backend
docker-compose down -v
```

## Building & running the API
1. Create virtual environment `python3 -m venv venv`
1. Activate virtual environment `source /venv/bin/activate`
1. Install python dependencies: `make pinstall` from repository root or `pip install -r requirements.txt` from backend directory
1. Start db: `make start-db` from repository root or `docker-compose -f docker-compose.yml up -d db` from backend directory
1. Run app using uvicorn: `uvicorn main:app --reload`

### Note for running the application!
- if you are running into a module not found error for 'VaderSentiment'
  we have currently found that installing vader outside of the VENV allows it to work.
  looking for permanent solution 
  
-pip3 install vaderSentiment

## Run tests

From repository root: `make ptest`

or

```
cd backend
pytest -v
```


### Set up pre-commit hooks (run commands in the backend DIR)
- pre-commit install

### Plan
- API (FastAPI)
- ORM (SQL Alchemy)
- Database to cache data (Postgres)
- Docker image for db
- Alembic for database migrations
- CRON running to update data
- Testing (PyTest):
  - Test alive
  - Test DB connection successful
  - Test data is present in db
- Reload end-point must be not be able to run until
  previous reload is complete

### Outputsß
- JSON output of passes per service (assessment vs reassessment)
- Plotly graph of pass and failure

### Testing (Arrange, Act, Assert)
- Functional Test on API endpoints
- Mocking service


