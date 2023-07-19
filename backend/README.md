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
- (build) docker-compose up -d --build
- (run) docker-compose -f docker-compose.yml up
- (stop) docker-compose down -v
- (stop all containers) docker-compose down --volumes

### To add database tables
- alembic revision --autogenerate -m “New tables”
- alembic upgrade head

## How to Work (No Docker but db)
- create virtual environment 'python<version> -m venv <virtual-environment-name>'
- activate virtual environment 'source /venv/bin/activate'
- install requirements 'pip install -r requirements.txt'
- start db 'docker-compose -f docker-compose.yml up -d db'
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


