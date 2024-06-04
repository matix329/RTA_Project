import json
import csv
import pandas as pd
from kafka import KafkaConsumer
from datetime import datetime

# Funkcja przetwarzająca dane kryptowalut
def process_crypto_data(data, output_file):
    try:
        print(f"Przetwarzanie {len(data)} rekordów...")
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by=['name', 'date'])

        # Obliczenia specyficzne dla danych kryptowalut
        df['volatility'] = df['high_24h'] - df['low_24h']
        df['market_cap_to_volume'] = df['market_cap'] / df['total_volume']
        df['current_price_to_ath'] = df['current_price'] / df['ath']

        df.to_csv(output_file, index=False)
        print(f"Przetworzone dane zapisane do pliku {output_file}")
    except Exception as e:
        print(f"Błąd podczas przetwarzania danych: {e}")

# Funkcja konsumująca dane z Kafka i zapisująca do CSV
def consume_crypto_data():
    try:
        consumer = KafkaConsumer(
            'crypto',  # Nazwa tematu
            bootstrap_servers=['localhost:29092'],  # Użyj portu 29092, jeśli uruchamiasz z hosta
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='crypto-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    except Exception as e:
        print(f"Błąd przy tworzeniu konsumenta Kafka: {e}")
        return

    data = []

    print("Rozpoczęcie konsumpcji danych z Kafka...")

    for message in consumer:
        try:
            crypto_data = message.value
            data.append(crypto_data)
            print(f"Otrzymane dane: {crypto_data}")

            # Przetwarzaj dane po każdym nowym rekordzie
            process_crypto_data(data, '/Users/matix329/Projekt_rta/processed_crypto_data.csv')
        except Exception as e:
            print(f"Błąd podczas odbierania lub przetwarzania wiadomości: {e}")

if __name__ == "__main__":
    try:
        consume_crypto_data()
    except KeyboardInterrupt:
        print("Zakończono pobieranie danych.")
    except Exception as e:
        print(f"Błąd główny: {e}")
