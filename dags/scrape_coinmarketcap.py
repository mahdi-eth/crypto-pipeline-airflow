import json
import os
from requests import Session, ConnectionError, Timeout, TooManyRedirects

# Function to load config from a file
def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the config.json file
    config_path = os.path.join(script_dir, 'config.json')
    
    # Load the config.json file
    with open(config_path) as config_file:
        return json.load(config_file)

# Function to scrape cryptocurrency data
def scrape_crypto_data():
    config = load_config()
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config["X-CMC_PRO_API_KEY"],
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
        # Return the list of cryptocurrencies
        return data["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Error while fetching data: {e}")
        return None
