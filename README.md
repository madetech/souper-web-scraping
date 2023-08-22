docker build --progress=plain --no-cache
docker build --progress=plain --no-cache -t souper .
docker container run -dp 8000:8000 -t souper

# souper-web-scraping
Collecting information from 
[Service Standard Reports](https://www.gov.uk/service-standard-reports "Service Standard Reports")

Used in analysing the outcomes of Service Assessments and the reports produced.
Looking for patterns in data and stats that are behind them.

e.g, Can we determine if a larger proportion of the Digital Services presented by government DO NOT have appropriate service monitoring in place, in terms of meeting Service Standard number 14, i.e.: Monitoring the status of your service.

(Playbook document)

We didn't have time for a slideshow

Hello

What we've done since last presentation:
S - Second scraper
M - Hosting

This was the brief
  To create an application that can scrape information from the gov uk service reports for analysis for media drives and bids.
This is what we've done
  We have a reactive front-end showing data on each service with the option of looking at each report for each service
  This data is obtained in the background on a schedule so the front-end client user never has to wait for scraping data
This is what was difficult
  Lots of new tech
  Lack of staff and constant change overs leading to high-pressure on certain individuals and meaning we didn't meet out first
  deadline.
  Lots of onboarding v.short term
  However this meant we had a slick onboarding process
This is what we've learnt
  JA - React testing, Jest, Capybara
  SF - Souper (scraping) Python testing (Fixtures, Mocking, DB migration(Alembic))
  MB - Containerisation and copilot fastapi
This is where we can go in the future
  We have basic analysis outputs but we capture almost all the data therefore we can look to performing deeper analysis e.g:
  - Semantic analysis
  - Using LLMs

## Week 1/2
- Get basic data (reports and section)
- Input into DB
- Flask app to handle requests

## Week 2/2
- Display results
- Do further analysis