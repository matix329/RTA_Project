## Instrukcja uruchomienia

### Krok 1: 
Uruchom aplikację Dockera.

### Krok 2: Uruchomienie kontenerów

W terminalu (na macOS) lub w wierszu poleceń (na Windows), przejdź do katalogu, w którym znajduje się plik `docker-compose.yml`, a następnie uruchom poniższe polecenie:

```sh
docker-compose up -d
```

**Uwaga**: Czasem mogą wystąpić problemy z kontenerem **_Kafka-UI_**. W takim przypadku konieczne może być kilkukrotne uruchomienie i zamknięcie kontenera, aby Kafka zaczęła działać poprawnie.

### Krok 3: Sprawdzenie działania Kafka UI

Po uruchomieniu kontenerów, Kafka UI będzie dostępne pod adresem: [http://localhost:8180](http://localhost:8180).

Możesz także uzyskać dostęp do Kafka UI poprzez link w aplikacji Docker.

### Krok 4: Sprawdzenie w Kafka UI

Wejdź na Dashboard w Kafka UI i sprawdź, czy masz wgląd w klastery. Nas interesuje klaster o nazwie "local".

Jeżeli jest dostępny, przejdź do zakładki "topics" i sprawdź, czy są tam dwa topiki: `crypto` i `stock`. To właśnie te topiki nas interesują, ponieważ tam będą logi z naszych operacji.

### Krok 5: Uruchomienie streamów

W terminalu przejdź do katalogu, w którym znajdują się pliki `stream_stock.py` oraz `stream_crypto.py`, a następnie uruchom je jeden obok drugiego za pomocą komendy:
```sh
python3 stream_stock.py
```

### Krok 6: Uruchomienie importu

W nowym oknie terminala uruchom pliki `import_data_stock.py` oraz `import_data_crypto.py`.

```sh
python3 import_data_stock.py
```

**UWAGA**: Aby przerwać działanie tych procesów, użyj kombinacji klawiszy `Ctrl + C` (niezależnie od tego, czy używasz macOS, czy Windows).
