def filter_top_cryptos(crypto_data, top_n=10):
    # Sort the cryptocurrencies by rank and return the top N
    return sorted(crypto_data, key=lambda x: x['rank'])[:top_n]

def transform_data(crypto_data):
    # Example transformation: extract useful fields
    transformed_data = []
    for crypto in crypto_data:
        transformed_data.append({
            'id': crypto['id'],
            'name': crypto['name'],
            'symbol': crypto['symbol'],
            'rank': crypto['rank'],
            'slug': crypto['slug'],
            'is_active': crypto['is_active'],
            'first_historical_data': crypto['first_historical_data'],
            'last_historical_data': crypto['last_historical_data']
        })
    return transformed_data
