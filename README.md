# Crypto Pipeline with Airflow

![Airflow](https://img.shields.io/badge/Apache%20Airflow-cryptocurrency-blue.svg)

## Description
This project is a fully automated cryptocurrency data pipeline using Apache Airflow. It scrapes data from CoinMarketCap, processes the top 10 cryptocurrencies, and stores the data in an SQLite database.

### Features:
- Automated hourly cryptocurrency data scraping from CoinMarketCap.
- Data transformation to filter and clean the top 10 cryptos.
- Data storage using SQLite, ready for analysis or reporting.

### Technologies Used:
- **Apache Airflow**: For automation and scheduling.
- **SQLite**: Lightweight database for storing crypto data.
- **Python**: For scraping, transforming, and storing data.

## How to Use

### Requirements:
- Python 3.x
- Apache Airflow
- CoinMarketCap API Key

### Setup:
1. Clone this repository:
   ```bash
   git clone https://github.com/mahdi-eth/crypto-pipeline-airflow.git
   ```
2. Install dependencies
3. 
4. Create a `config.json` file in the project root and add your CoinMarketCap API key:
   ```json
   {
     "X-CMC_PRO_API_KEY": "your_api_key_here"
   }
   ```

5. Initialize Airflow:
   ```bash
   airflow db init
   ```

6. Start the Airflow scheduler and webserver:
   ```bash
   docker-compose up -d
   ```

7. Access Airflow UI: Open [http://localhost:8080](http://localhost:8080) to view and trigger the DAG.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
