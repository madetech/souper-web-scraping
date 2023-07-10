# souper-web-scraping
Collecting information from Service Assessment reports

## How to Run
- clone repo
- activate venv source /venv/bin/activate
- install requirements (pip install -r requirements.txt)
- run db (docker-compose up) *need docker
- run app through uvicorn to make it async and handle lots or requests (uvicorn main:app --reload) *asgi

## Plan
- API (FastAPI)
- ORM (SQL Alchemy)
- Database to cache data (Postgres)
- Docker image for db
- CRON running to update data
- Testing:
-- TODO
-- Reload end-point must be massively limited and locked-down

## Outputs
- JSON output of passes per service (assessment vs reassessment)
- Plotly graph of pass and failure

## Testing (Arrange, Act, Assert)
- Functional Test on API endpoints
- Mocking service


