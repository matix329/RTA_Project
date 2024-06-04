# RTA_Project
-------
### Stock
Skrypt `import_data_stock.py` przetwarza dane giełdowe i generuje przetworzone dane, które są zapisywane w nowym pliku CSV (`processed_stock_data.csv`). Skrypt dodaje kilka nowych kolumn, które ułatwiają analizę danych akcji na przestrzeni czasu.

### **Nowe Kolumny**

**price_change:**
Procentowa zmiana ceny zamknięcia w stosunku do poprzedniego dnia dla każdego symbolu.

**average_price:**
Umożliwia porównanie bieżącej ceny zamknięcia z średnią ceną zamknięcia.

**price_to_average_ratio:**
Stosunek bieżącej ceny zamknięcia do średniej ceny zamknięcia dla każdego symbolu.

**rolling_mean:**
7-dniowa średnia ruchoma ceny zamknięcia.

**rolling_std:**
7-dniowe odchylenie standardowe ceny zamknięcia.

**cumulative_return:**
Kumulatywny zwrot od początku danych do bieżącego dnia.

------
### Consumer_crypto
Skrypt `import_data_stock.py` wczytuje dane kryptowalutowe i dodaje nowe kolumny do analizy i zapisuje zmodyfikowane dane do nowego pliku `processed_crypto_data.csv`.

## Nowe kolumny

**volatility**:
Różnica między najwyższą a najniższą ceną w ciągu 24 godzin.

**market_cap_to_volume**:
Stosunek kapitalizacji rynkowej do wolumenu obrotu.

**current_price_to_ath**:
Stosunek aktualnej ceny do najwyższej ceny wszech czasów (ATH).
