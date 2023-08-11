# souper-web-scraping
Collecting information from 
[Service Standard Reports](https://www.gov.uk/service-standard-reports "Service Standard Reports")

Used in analysing the outcomes of Service Assessments and the reports produced.
Looking for patterns in data and stats that are behind them.

e.g, Can we determine if a larger proportion of the Digital Services presented by government DO NOT have appropriate service monitoring in place, in terms of meeting Service Standard number 14, i.e.: Monitoring the status of your service.

## Rough Stages
### Stage 1
- Get basic data (reports and section)
- Input into DB
- Flask app to handle requests

### Stage 2
- Build front-end
- Display results
- Do further analysis

### Stage 3+
- Improve both

## How to Run
This is designed to have back-end analysis on a CRON (Schedule). The front-end should be able to generate reports on already accessible data through the front-end FastAPI talking to a DB.
* No Instructions yet so look at front-end/back-end READMEs
  * (Likely) get env variables for backend
  * (Likely) startup backend, follow README
  * (Likely) hit /scrape endpoint to get data
  * (Likely) start front-end, follow README
  * (Likely) wait for back-end to complete


