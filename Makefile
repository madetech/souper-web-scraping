backend_dir := backend
frontend_dir := frontend

help: ## Shows this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'

install: pinstall jsinstall ## Installs all dependencies

pinstall: ## Installs python dependencies
	cd $(backend_dir) && pip3 install -r requirements.txt

jsinstall: ## Installs Javascript dependencies
	cd $(frontend_dir) && npm install

start-db: ## Starts the DB container
	docker-compose -f docker-compose.yml up -d db

build-containers: ## Builds Docker containers (does not start containers)
	docker-compose -f docker-compose.yml build

destroy-containers: ## Destroys Docker containers and volumes
	docker-compose -f docker-compose.yml down -v

rebuild-containers: destroy-containers build-containers ## Destroys Docker containers and rebuilds them (does not start containers)

 # The wait_until function periodically checks if the DB is ready to accept connections. The timeout can be adjusted (30s default; see scripts/wait-until.sh).
rebuild-containers-and-migrate-db: rebuild-containers ## Rebuilds containers and runs DB migrations
	source $(backend_dir)/.env && \
	source scripts/wait-until.sh && \
	cd $(backend_dir) && \
	wait_until "docker-compose exec -T -e PGPASSWORD=$${POSTGRES_PASSWORD} db psql -U $${POSTGRES_USER} $${POSTGRES_DB} -c 'select 1'" && \
	alembic upgrade head

db-migrate: ## Runs database migrations
	cd $(backend_dir) && \
	alembic upgrade head

ptest: ## Run backend tests
	cd $(backend_dir) && pytest -v

jstest: ## Run frontend tests
	cd $(frontend_dir) && CI=true npm test

prun: ## Runs the backend
	cd $(backend_dir) && uvicorn main:app --reload

jsrun: ## Runs the frontend
	cd $(frontend_dir) && npm start