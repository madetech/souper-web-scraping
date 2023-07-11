# souper-web-scraping
Collecting information from Service Assessment reports

## How to Run
- clone repo
- Install docker
- (build) docker-compose up -d --build
- (run) docker-compose -f docker-compose.yml up
- (stop) docker-compose down -v  


## How to Work (No Docker)
- activate virtual environment 'source /venv/bin/activate'
- install requirements 'pip install -r requirements.txt'
- START DB //!TODO Add docker-compose option for just db
  - docker-compose -f docker-compose.yml up -d db ?
- run app through uvicorn to make it async for requests (uvicorn main:app --reload) *asgi server
- Run tests        

## Plan
- API (FastAPI)
- ORM (SQL Alchemy)
- Database to cache data (Postgres)
- Docker image for db
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


