import json
import csv
import pandas as pd
from kafka import KafkaConsumer
from datetime import datetime

# Funkcja przetwarzająca dane giełdowe
def process_stock_data(data, output_file):
    try:
        print(f"Przetwarzanie {len(data)} rekordów...")
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by=['symbol', 'date'])

        df['price_change'] = df.groupby('symbol')['currentPrice'].pct_change() * 100

        average_prices = df.groupby('symbol')['currentPrice'].mean().reset_index()
        average_prices.columns = ['symbol', 'average_price']
        df = pd.merge(df, average_prices, on='symbol')

        df['price_to_average_ratio'] = df['currentPrice'] / df['average_price']

        df['rolling_mean'] = df.groupby('symbol')['currentPrice'].transform(lambda x: x.rolling(window=7).mean())
        df['rolling_std'] = df.groupby('symbol')['currentPrice'].transform(lambda x: x.rolling(window=7).std())

        df['cumulative_return'] = df.groupby('symbol')['currentPrice'].apply(lambda x: x / x.iloc[0] - 1).reset_index(level=0, drop=True)

        df.to_csv(output_file, index=False)
        print(f"Przetworzone dane zapisane do pliku {output_file}")
    except Exception as e:
        print(f"Błąd podczas przetwarzania danych: {e}")

# Funkcja konsumująca dane z Kafka i zapisująca do CSV
def consume_stock_data():
    try:
        consumer = KafkaConsumer(
            'stock',  # Nazwa tematu
            bootstrap_servers=['localhost:29092'],  # Użyj portu 29092, jeśli uruchamiasz z hosta
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='stock-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    except Exception as e:
        print(f"Błąd przy tworzeniu konsumenta Kafka: {e}")
        return

    data = []

    print("Rozpoczęcie konsumpcji danych z Kafka...")

    for message in consumer:
        try:
            stock_data = message.value
            data.append(stock_data)
            print(f"Otrzymane dane: {stock_data}")

            # Przetwarzaj dane po każdym nowym rekordzie
            process_stock_data(data, '#Wklej link')
        except Exception as e:
            print(f"Błąd podczas odbierania lub przetwarzania wiadomości: {e}")

if __name__ == "__main__":
    try:
        consume_stock_data()
    except KeyboardInterrupt:
        print("Zakończono pobieranie danych.")
    except Exception as e:
        print(f"Błąd główny: {e}")
