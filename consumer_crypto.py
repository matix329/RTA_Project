import pandas as pd

crypto_data_path = '/Users/matix329/Projekt_rta/crypto_data.csv'
crypto_data_df = pd.read_csv(crypto_data_path)

crypto_data_df['volatility'] = crypto_data_df['high_24h'] - crypto_data_df['low_24h']
crypto_data_df['market_cap_to_volume'] = crypto_data_df['market_cap'] / crypto_data_df['total_volume']
crypto_data_df['current_price_to_ath'] = crypto_data_df['current_price'] / crypto_data_df['ath']

new_crypto_data_path = '/Users/matix329/Projekt_rta/processed_crypto_data.csv'
crypto_data_df.to_csv(new_crypto_data_path, index=False)

print(f"Dane zostały zapisane do pliku {new_crypto_data_path}")