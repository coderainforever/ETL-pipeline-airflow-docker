# ETL-pipeline-airflow-docker-container
ETL Pipeline using Airflow Dag (Extract JSON data and ingest to SQLite Database)

## Step 1: Running Airflow in Docker

Have Docker installed. 

Create a new project folder and open terminal in that folder and run

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'

to deploy Airflow on Docker Compose and created dags, logs and plugins folders 

Then run the command: 

docker-compose up airflow-init

and then 

docker-compose up

and then access the web server at localhost:8080 via Docker GUI

It can also be accessed using the command on terminal after checking the running containers using docker ps and choosing the container id

docker exec <container-id> airflow version

## Step 2: Running DAG

Open the project folder in VSCode and activate the virtual environment and run pip install -r requirements.txt in terminal. Then create two new python files in the dags directory - one containing the code for the tasks and the other one the DAG. 

In the main python file, create 3 different functions corresponding to three different tasks in the pipeline. 

* Task 1 - Extract: We will use a public open dataset on the counts of COVID-19 related hospitalization, cases, and deaths in New York City as our external data source. The dataset is pulled as a JSON file using python requests and saved in csv format. 

* Task 2 - Transform: Then the data is transformed by formatting dates and removing a few columns by loading as a dataframe using pandas. The transformed data is also saved in CSV format.

* Task 3 - Load: Then the data is again pulled into a dataframe and ingested to an SQlite database. 

The tasks are added to the DAG using PythonOperator. 

## Step 3: Validation 

Check the .csv and .db files to make sure the data is actually properly extracted, transformed and loaded. 

Verify the Database using DBeaver or other tools

Source files have been uploaded in the repository: https://github.com/vinazol/ETL-pipeline-airflow-docker
