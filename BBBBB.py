import pandas as pd
import matplotlib.pyplot as pl
datafile = pd.read_csv("Grade_12_full_data_csv_file.csv")
import textwrap
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
'''
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = {'symbol': 'BTC', 'convert': 'USD'}
#url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
#parameters = {'symbol': 'BTC,ETH'}

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
#a = data['data']
#b = a['BTC']
#print(b)
#c = b[0]
#d = c['description']
#d = textwrap.fill(d, width=150)
#print('')
#print(d)

b = data['data']['BTC']
b = b[0]
print('Id:', b['id'])
print('Name:', b['name'])
print('Symbol:', b['symbol'])
c = b['quote']['USD']
print('Price:', c['price'])
print('24 hour volume:', c['volume_24h'])
print('Percent change in 7 days:', c['percent_change_7d'])
print('Percent change in 90 days:', c['price'])
print('Price', c['price'])
print('Market cap:', c['market_cap'])

def currency_price(ch2,cur):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {'symbol': ch2, "convert": cur}
    headers = {"X-CMC_PRO_API_KEY": 'bde04074-f1e4-4a6f-888e-9783d15a400b'}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    price = data["data"][ch2]['quote']
    return price
print("Different currency prices")
ch1 = input("Enter symbol of crypto:")
ch4 = list(input("Enter various currencies(symbol eg:INR) to be converted to(separated by commas: "))

for i in range(0, len(ch4)):
    print(currency_price(ch1, ch4[i]))
'''
a = datafile['market_cap'][1:10]
b = a/10**10

pl.figure(facecolor='c', edgecolor='b')
pl.plot(datafile['symbol'][1:10], b, color='g', marker='d', markeredgecolor='m')
pl.ylim(10 ** 10, 2.5 * 10 ** 11)
pl.grid()
pl.xlabel('Cryptocurrencies')
pl.ylabel('Market Cap')
pl.xticks(rotation=45, ha='right')
pl.title('Market Cap for various cryptocurrencies')
pl.show()
pl.plot(datafile['symbol'][0:10], datafile['ath_change_percentage'][0:10], color='g', marker='d',
        markeredgecolor='m')
pl.show()
pl.plot(datafile['symbol'][0:10], datafile['market_cap_change_percentage_24h'][0:10], color='g', marker='d',
        markeredgecolor='m')
pl.show()
pl.plot(datafile['symbol'][0:10], datafile['total_volume'][0:10]/10**10, color='g', marker='d',
        markeredgecolor='m')
pl.show()