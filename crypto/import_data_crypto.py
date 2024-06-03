import json
import csv
from kafka import KafkaConsumer

def consume_crypto_data():
    # Konfiguracja konsumenta Kafka
    consumer = KafkaConsumer(
        'crypto',  # Nazwa tematu
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='crypto-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # Otwórz plik CSV do zapisu
    with open('crypto_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Zapisz nagłówki do pliku CSV
        writer.writerow(
            ['type', 'date', 'name', 'current_price', 'high_24h', 'low_24h', 'price_change_24h',
             'price_change_percentage_24h', 'market_cap', 'total_volume', 'ath', 'atl']
        )

        print("Rozpoczynam pobieranie danych...")
        for message in consumer:
            crypto_data = message.value

            # Zapisz dane do pliku CSV
            writer.writerow([
                crypto_data.get('type', 'No Data'),
                crypto_data.get('date', 'No Data'),
                crypto_data.get('name', 'No Data'),
                crypto_data.get('current_price', 'No Data'),
                crypto_data.get('high_24h', 'No Data'),
                crypto_data.get('low_24h', 'No Data'),
                crypto_data.get('price_change_24h', 'No Data'),
                crypto_data.get('price_change_percentage_24h', 'No Data'),
                crypto_data.get('market_cap', 'No Data'),
                crypto_data.get('total_volume', 'No Data'),
                crypto_data.get('ath', 'No Data'),
                crypto_data.get('atl', 'No Data')
            ])
            print(f"Otrzymane dane: {crypto_data}")

if __name__ == "__main__":
    try:
        consume_crypto_data()
    except KeyboardInterrupt:
        print("Zakończono pobieranie danych.")
