
EODHD_API_KEY = "66ba439b448894.67845987"

# commodities APIs
# bonds APIs

# stocks APIs
#   - stocks fundamentals end of day historical data
url = f'https://eodhd.com/api/fundamentals/{SYMBOL_NAME}.{EXCHANGE_ID}?api_token=demo&fmt=json'
data = requests.get(url).json()

# ETFs APIs
# news APIs
# equities APIs
# mutual funds APIs
# indices APIs
url = f'https://eodhd.com/api/fundamentals/GSPC.INDX?api_token={YOUR_API_TOKEN}&fmt=json'
data = requests.get(url).json()
# list of exchanges
url = f'https://eodhd.com/api/exchanges-list/?api_token={YOUR_API_TOKEN}&fmt=json'
data = requests.get(url).json()
# bulk fundamentals APIs
url = f'https://eodhd.com/api/bulk-fundamentals/NASDAQ?api_token={EODHD_API_KEY}&fmt=json'
data = requests.get(url).json()

# government bonds
url = f'https://eodhd.com/api/eod/UK10Y.GBOND?api_token={YOUR_API_TOKEN}&fmt=json'
data = requests.get(url).json()
# EURIBOR
url = f'https://eodhd.com/api/eod/EURIBOR3M.MONEY?api_token={YOUR_API_TOKEN}&fmt=json'
# LIBOR
url = f'https://eodhd.com/api/eod/LIBOREUR2M.MONEY?api_token={YOUR_API_TOKEN}&fmt=json'
# ECB exchange rates
url = f'https://eodhd.com/api/eod/ECBEURUSD.MONEY?api_token={YOUR_API_TOKEN}&fmt=json'

# economic events API
url = f'https://eodhd.com/api/economic-events?api_token=demo&fmt=json'
data = requests.get(url).json()


# commodities websockets
# bonds websockets
# stocks websockets
US market trade data: wss://ws.eodhistoricaldata.com/ws/us?api_token=XXX
US market quote data: wss://ws.eodhistoricaldata.com/ws/us-quote?api_token=XXX

# ETFs websockets
# news websockets
