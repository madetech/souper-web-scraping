# souper-web-scraping
Collecting information from 
[Service Standard Reports](https://www.gov.uk/service-standard-reports "Service Standard Reports")

Used in analysing the outcomes of Service Assessments and the reports produced.
Looking for patterns in data and stats that are behind them.

e.g, Can we determine if a larger proportion of the Digital Services presented by government DO NOT have appropriate service monitoring in place, in terms of meeting Service Standard number 14, i.e.: Monitoring the status of your service.

## Week 1/2
- Get basic data (reports and section)
- Input into DB
- Flask app to handle requests

## Week 2/2
- Display results
- Do further analysis

## How to Run
- clone repo
- Install docker

**Note: run `make` or `make help` in project root for other useful make options**

### Build and run the DB container
`make start-db`

or

```
cd backend
docker-compose -f docker-compose.yml up -d db
```

### Destroying containers
`make destroy-containers`

or

```
cd backend
docker-compose down -v
```

### Settings up the database
`make db-migrations`

or

```
cd backend
alembic upgrade head
```

### Generating Alembic migrations

This is only necessary when making changes to models/schema
`alembic revision --autogenerate -m “<descriptive message here>”`

## How to Work (No Docker but db)
- create virtual environment `python<version> -m venv <virtual-environment-name>`
- activate virtual environment `source /venv/bin/activate`
- install python dependencies: `make pinstall` from project root or `pip install -r requirements.txt`
- start db: `make start-db` from project root or `docker-compose -f docker-compose.yml up -d db`
- run app through uvicorn to make it async for requests (uvicorn main:app --reload) *asgi server
- Run tests        

## Plan
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

## Outputs
- JSON output of passes per service (assessment vs reassessment)
- Plotly graph of pass and failure

## Testing (Arrange, Act, Assert)
- Functional Test on API endpoints
- Mocking service


