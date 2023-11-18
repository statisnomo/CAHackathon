import textwrap
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
# parameters = {'id': 1, 'convert': 'USD'}
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
parameters = {'symbol': 'BTC,ETH'}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'bde04074-f1e4-4a6f-888e-9783d15a400b',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


a = data['data']['BTC']
print(a)
c = a[0]
d = c['description']
d = textwrap.fill(d, width=150)
print('')
print(d)

max_line_width = 150
formatted_output = ""
for key, value in data.items():
    key_value_pair = f"{key}: {value}"
    # Split the key-value pair into multiline text with a maximum line width
    wrapped_text = textwrap.fill(key_value_pair, width=max_line_width)
    formatted_output += wrapped_text + '\n'

print(formatted_output)



#   a = data['data']    QUOTES STUFFFF
#   b = a['1']
#   print(b['id'])
#   print(b['name'])
#   print(b['symbol'])



import requests
import time

# Replace with your CoinGecko API endpoint for cryptocurrency data
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'


def get_crypto_price():
    response = requests.get(url)
    data = response.json()
    price = data['bitcoin']['usd']
    return price


while True:
    bitcoin_price = get_crypto_price()
    print(f"Bitcoin Price (USD): ${bitcoin_price}")
    time.sleep(3)  # Fetch and update price every minute
