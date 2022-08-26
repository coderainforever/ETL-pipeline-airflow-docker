from datetime import date, datetime
import requests
import pandas as pd
import json
import requests
from sqlalchemy import create_engine

# Extract:  Extracting JSON data from public API of New York City website and saving to a .csv file

def _extract():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    result_load = requests.get(url)
    df = pd.DataFrame(json.loads(result_load.content))
    df.to_csv("data/covid_db_original_{}.csv".format(date.today().strftime("%Y%m%d")))
_extract()

# Transform: Transforming the data using pandas and saving to a new .csv file

def _transform():
    df1 = pd.read_csv("data/covid_db_original_{}.csv".format(date.today().strftime("%Y%m%d")))
    df1['date'] = df1['date_of_interest'].str.extract('(....-..-..)', expand=True)
    df1.drop(df1.columns.difference(['date','case_count','hospitalized_count','death_count']), axis=1, inplace=True)
    df1 = df1.set_index("date")
    df1.to_csv("data/covid_db_transformed_{}.csv".format(date.today().strftime("%Y%m%d")))
_transform()

# Load: Ingesting the transformed data into an SQLite Database

def _load():
    
    df2 = pd.read_csv("data/covid_db_transformed_{}.csv".format(date.today().strftime("%Y%m%d")))
    DATABASE_LOCATION = "sqlite:///covid_db_cleaned.sqlite"
    engine = create_engine(DATABASE_LOCATION, echo=True)
    sqlite_connection = engine.connect()
    sqlite_table = "covid_data"
    df2.to_sql(sqlite_table, sqlite_connection, if_exists='append')
    sqlite_connection.close()

_load()