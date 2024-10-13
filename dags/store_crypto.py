import os
import sqlite3

# Get the directory of the current script or specify a known directory
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'crypto_data.db')

def create_table():
    conn = sqlite3.connect(db_path)  # Use the absolute path here
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cryptocurrencies (
            id INTEGER PRIMARY KEY,
            name TEXT,
            symbol TEXT,
            rank INTEGER,
            slug TEXT,
            is_active INTEGER,
            first_historical_data TEXT,
            last_historical_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_crypto_data(transformed_data):
    conn = sqlite3.connect(db_path)  # Use the absolute path here
    cursor = conn.cursor()

    for crypto in transformed_data:
        cursor.execute('''
            INSERT OR REPLACE INTO cryptocurrencies
            (id, name, symbol, rank, slug, is_active, first_historical_data, last_historical_data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (crypto['id'], crypto['name'], crypto['symbol'], crypto['rank'], crypto['slug'],
              crypto['is_active'], crypto['first_historical_data'], crypto['last_historical_data']))

    conn.commit()
    conn.close()
