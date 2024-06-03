import json
import csv
from kafka import KafkaConsumer


def consume_stock_data():
    # Konfiguracja konsumenta Kafka
    consumer = KafkaConsumer(
        'stock',  # Nazwa tematu
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='stock-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # Otwórz plik CSV do zapisu
    with open('stock_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Zapisz nagłówki do pliku CSV
        writer.writerow(
            ['type', 'date', 'symbol', 'currentPrice', 'open', 'previousClose', 'dayLow', 'dayHigh', 'recommendation',
             'targetHighPrice', 'targetLowPrice', 'targetMeanPrice', 'targetMedianPrice', 'recommendationMean',
             'totalRevenue', 'revenuePerShare', 'totalDebt', 'debtToEquity', 'totalCash', 'totalCashPerShare', 'ebitda',
             'earningsGrowth', 'revenueGrowth'])

        print("Rozpoczynam pobieranie danych...")
        for message in consumer:
            stock_data = message.value

            # Zapisz dane do pliku CSV
            writer.writerow([
                stock_data.get('type', 'No Data'),
                stock_data.get('date', 'No Data'),
                stock_data.get('symbol', 'No Data'),
                stock_data.get('currentPrice', 'No Data'),
                stock_data.get('open', 'No Data'),
                stock_data.get('previousClose', 'No Data'),
                stock_data.get('dayLow', 'No Data'),
                stock_data.get('dayHigh', 'No Data'),
                stock_data.get('recommendation', 'No Data'),
                stock_data.get('targetHighPrice', 'No Data'),
                stock_data.get('targetLowPrice', 'No Data'),
                stock_data.get('targetMeanPrice', 'No Data'),
                stock_data.get('targetMedianPrice', 'No Data'),
                stock_data.get('recommendationMean', 'No Data'),
                stock_data.get('totalRevenue', 'No Data'),
                stock_data.get('revenuePerShare', 'No Data'),
                stock_data.get('totalDebt', 'No Data'),
                stock_data.get('debtToEquity', 'No Data'),
                stock_data.get('totalCash', 'No Data'),
                stock_data.get('totalCashPerShare', 'No Data'),
                stock_data.get('ebitda', 'No Data'),
                stock_data.get('earningsGrowth', 'No Data'),
                stock_data.get('revenueGrowth', 'No Data')
            ])
            print(f"Otrzymane dane: {stock_data}")


if __name__ == "__main__":
    try:
        consume_stock_data()
    except KeyboardInterrupt:
        print("Zakończono pobieranie danych.")
