import pandas as pd


def process_stock_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['symbol', 'date'])

    df['price_change'] = df.groupby('symbol')['currentPrice'].pct_change() * 100

    average_prices = df.groupby('symbol')['currentPrice'].mean().reset_index()
    average_prices.columns = ['symbol', 'average_price']
    df = pd.merge(df, average_prices, on='symbol')

    df['price_to_average_ratio'] = df['currentPrice'] / df['average_price']

    df['rolling_mean'] = df.groupby('symbol')['currentPrice'].transform(lambda x: x.rolling(window=7).mean())
    df['rolling_std'] = df.groupby('symbol')['currentPrice'].transform(lambda x: x.rolling(window=7).std())

    df['cumulative_return'] = df.groupby('symbol')['currentPrice'].apply(lambda x: x / x.iloc[0] - 1).reset_index(
        level=0, drop=True)

    df.to_csv(output_file, index=False)
    print(f"Przetworzone dane zapisane do pliku {output_file}")


if __name__ == "__main__":
    input_file = '/Users/matix329/Projekt_rta/stock_data.csv'
    output_file = '/Users/matix329/Projekt_rta/processed_stock_data.csv'
    process_stock_data(input_file, output_file)
