import logging
from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
from scrape_coinmarketcap import scrape_crypto_data
from transform_crypto import filter_top_cryptos, transform_data
from store_crypto import create_table, store_crypto_data

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG('crypto_pipeline',
         default_args=default_args,
         schedule='@hourly',  # Schedule every hour
         catchup=False) as dag:

    @task
    def scrape_task():
        logging.info("Starting to scrape cryptocurrency data...")
        crypto_data = scrape_crypto_data()
        if crypto_data is None:
            raise ValueError("Failed to fetch cryptocurrency data.")
        return crypto_data
    
    @task
    def transform_task(crypto_data):
        logging.info("Transforming cryptocurrency data...")
        top_cryptos = filter_top_cryptos(crypto_data, top_n=10)
        return transform_data(top_cryptos)

    @task
    def store_task(transformed_data):
        logging.info("Storing cryptocurrency data in the database...")
        create_table()
        store_crypto_data(transformed_data)

    # Set the task dependencies using the TaskFlow API
    crypto_data = scrape_task()
    transformed_data = transform_task(crypto_data)
    store_task(transformed_data)
