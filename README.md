# souper-web-scraping
The main aim of this project is to collect information from 
[Service Standard Reports](https://www.gov.uk/service-standard-reports "Service Standard Reports").

The information is to be used in analysing the outcomes of Service Assessments and the reports produced.
This will enable us to look for patterns in data and stats that are currently obscured.

e.g, Can we determine if a larger proportion of the Digital Services presented by government do not have appropriate service monitoring in place in terms of meeting Service Standard number 14, i.e.: Monitoring the status of your service.

# Quick setup
The application consists of three components: frontend, backend and database.
The single command to start all three parts is:

`docker-compose up --build --force-recreate -d`

In your project directory you will need a .env, like the .env.example. Ask a project colleague for specific information about filling in the template.

The web interface will be visible at the REACT_APP_FRONTEND specified in your .env file. To start a scrape, go to `BACKEND_HOST:REACT_APP_BACKEND_PORT/scrape` (the 'Run scrape' button doesn't actually run a scrape yet). It may take a while. Once completed you will see entries in your database and the REACT_APP_FRONTEND address will show a list of reports scraped and some of their information.

# Design information
The database is Postgres, and database migrations make use of [Alembic] (https://alembic.sqlalchemy.org/en/latest/ "Alembic") which works with SLQAlchemy.
The frontend is built with React, and the backend is written in Python (requires Python >= 3.10).

The application has been containerized to make for easier hosting.

# Running locally
To run the application locally outside containers, see backend/README and frontend/README.