'''import requests


def get_btc_price_cryptocompare():
    url = "https://min-api.cryptocompare.com/data/price"
    params = {
        "fsym": "BTC",     # From symbol (BTC)
        "tsyms": "USD"     # To symbol (USD)
    }
    response = requests.get(url, params=params)
    data = response.json()
    price_in_usd = data["USD"]
    return price_in_usd


btc_price = get_btc_price_cryptocompare()
print(f"The live price of BTC in USD is ${btc_price}")


def get_btc_price_coinmarketcap(apikey):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {
        "id": "1",              # Bitcoin's ID on CoinMarketCap
        "convert": "USD"        # Convert to USD
    }
    headers = {
        "X-CMC_PRO_API_KEY": apikey
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    price_in_usd = data["data"]["1"]["quote"]["USD"]["price"]
    return price_in_usd


# Replace "YOUR_API_KEY" with your actual CoinMarketCap API key
api_key = "bde04074-f1e4-4a6f-888e-9783d15a400b"
btc_price = get_btc_price_coinmarketcap(api_key)
print(f"The live price of BTC in USD is ${btc_price}")
'''
import pandas as pd
import mplfinance as mpf

# Sample data (replace this with your OHLCV data)
data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'open': [100, 110, 95, 105, 102],
    'high': [120, 115, 100, 110, 105],
    'low': [90, 100, 92, 98, 100],
    'close': [110, 105, 97, 102, 101],
    'volume': [100000, 120000, 80000, 90000, 95000]
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Create a candlestick chart
mpf.plot(df, type='candle', mav=(5, 10), volume=True, show_nontrading=True)
