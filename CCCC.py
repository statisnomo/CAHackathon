import textwrap
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import time
import pandas as pd
import matplotlib.pyplot as pl
from datetime import datetime as dt
datafile = pd.read_csv("Grade_12_full_data_csv_file.csv")

print('Welcome to this program about Cryptocurrency')
print('')


def info_crypto(ch1):
    url1 = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    parameters1 = {'symbol': ch1}
    headers1 = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'bde04074-f1e4-4a6f-888e-9783d15a400b',
    }

    session1 = Session()
    session1.headers.update(headers1)

    response1 = session1.get(url1, params=parameters1)
    data_main = json.loads(response1.text)
    print(data_main)
    a = data_main['data'][ch1][0]['description']
    d = textwrap.fill(a, width=150)
    print('')
    print(d)


def live_prices(ch2):
    url = "https://min-api.cryptocompare.com/data/price"
    params = {"fsym": ch2, "tsyms": "USD"}

    response = requests.get(url, params=params)
    data = response.json()
    price_in_usd = data["USD"]
    print("The live price of", ch2, "in USD is", price_in_usd)


def live_price_cmc(ch2):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {'symbol': ch2, "convert": "USD"}
    headers = {"X-CMC_PRO_API_KEY": 'bde04074-f1e4-4a6f-888e-9783d15a400b'}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    price = data["data"][ch2]['quote']['USD']['price']
    return price


def currency_price(ch2,cur):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {'symbol': ch2, "convert": cur}
    headers = {"X-CMC_PRO_API_KEY": 'bde04074-f1e4-4a6f-888e-9783d15a400b'}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    price = data["data"][ch2]['quote'][cur]['price']
    return price
def graph_hist_price(ch2):
    url = "https://min-api.cryptocompare.com/data/v2/histoday"
    params = {"fsym": ch2, "tsym": "USD", 'limit': 58, 'aggregate': 30}
    response = requests.get(url, params=params)
    data = response.json()

    a = data['Data']
    b = a['Data']
    c = len(b)
    lis = []
    date = []
    for i in range(0, c):
        lis.append(b[i]['high'])
        a = b[i]['time']
        date.append(dt.utcfromtimestamp(a).date())

    ut = data['Data']['TimeFrom']
    ut1 = data['Data']['TimeTo']
    dt1 = dt.utcfromtimestamp(ut)
    print("Start Time:", dt1)
    dt2 = dt.utcfromtimestamp(ut1)
    print("End Time:", dt2)
    d1 = dt1.date()
    d2 = dt2.date()

    ylabel = 'Price of ' + ch2 + '(in USD)'
    title = 'Price of ' + ch2 + ' from ' + str(d1) + ' to ' + str(d2)
    pl.figure(facecolor='c', edgecolor='b')
    pl.plot(date, lis, color='g', marker='d', markeredgecolor='m')
    pl.grid()
    pl.xlabel('Month/Year')
    pl.ylabel(ylabel)
    pl.xticks(rotation=45, ha='right')
    pl.title(title)
    pl.show()


def quantities(ch2):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {'symbol': ch2, 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'bde04074-f1e4-4a6f-888e-9783d15a400b'}

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        b = data['data'][ch2][0]
        print('Id:', b['id'])
        print('Name:', b['name'])
        print('Symbol:', b['symbol'])
        c = b['quote']['USD']
        print('Price:', c['price'])
        print('24 hour volume:', c['volume_24h'])
        print('Percent change in 1 hour:', c['percent_change_1h'])
        print('Percent change in 7 days:', c['percent_change_7d'])
        print('Percent change in 90 days:', c['percent_change_90d'])
        print('Market cap:', c['market_cap'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


while True:
    print('Enter 1 to view a basic introduction to CRYPTOCURRENCY\n'
          'Enter 2 to view details about different cryptocurrencies\n'
          'Enter 3 to view graphs about recent trends in cryptocurrency\n'
          'Enter 4 to view live prices of various cryptocurrencies\n'
          'Enter 5 to view prices of cryptos in different currencies\n'
          'Enter 6 to view different stats of a cryptocurrency:')
    ch = input()
    if ch == '1':
        print("CRYPTOCURRENCY!!!!!!!!!!!!!!!")
        print('''Title: Cryptocurrency: A Revolution in Digital Finance

Introduction:

Cryptocurrency is a groundbreaking concept that has transformed the landscape of traditional finance. Emerging in the wake of the 2008 financial crisis, it aimed to address issues of centralization, security, and accessibility. This essay explores the fundamental aspects of cryptocurrency, its underlying technology, and its impact on the global economy.

Body:

Definition and Origin:
Cryptocurrency is a form of digital or virtual currency that uses cryptography for security. Unlike traditional currencies issued by governments and central banks, cryptocurrencies operate on decentralized networks based on blockchain technology. The first and most well-known cryptocurrency, Bitcoin, was introduced in 2009 by an anonymous entity known as Satoshi Nakamoto. Bitcoin laid the foundation for numerous other cryptocurrencies collectively known as altcoins.

Blockchain Technology:
At the core of most cryptocurrencies is blockchain, a distributed ledger that records all transactions across a network of computers. Each block contains a list of transactions and a reference to the previous block, creating a secure and transparent chain. The decentralized nature of blockchain eliminates the need for intermediaries, providing a more efficient and secure way to conduct transactions. This technology has applications beyond cryptocurrencies, such as supply chain management, voting systems, and smart contracts.

Cryptocurrency Types and Functions:
Cryptocurrencies serve various purposes beyond being a medium of exchange. Some, like Bitcoin, primarily function as a store of value and a hedge against inflation. Others, like Ethereum, enable the creation of decentralized applications (DApps) through smart contracts. Stablecoins are designed to minimize price volatility by pegging their value to a fiat currency or other assets. Understanding the diversity of cryptocurrencies is crucial for grasping their broader impact on the financial ecosystem.

Impact on Global Finance:
Cryptocurrencies have disrupted traditional financial systems, offering new opportunities and challenges. The decentralized nature of cryptocurrencies allows for financial inclusion, enabling people without access to traditional banking services to participate in the global economy. However, regulatory challenges, concerns about illicit activities, and market volatility have prompted governments and financial institutions to adopt various approaches, ranging from acceptance to skepticism.

Conclusion:

In conclusion, cryptocurrency represents a transformative force in the world of finance. Its underlying blockchain technology has implications far beyond currency, influencing industries and sectors globally. As cryptocurrencies continue to evolve, finding a balance between innovation and regulation will be crucial for their sustained growth and integration into mainstream finance.''')
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break

    elif ch == '2':
        print("Informations")
        info_crypto(input("Enter the symbol of the Crypto whose info is to be displayed:"))
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '3':
        print("GRAPHHSSS(tbd)")
        print('Enter 1 to view graphs of prices in the last 5 years of a cryptocurrency\n'
              'Enter 2 to view graphs of various other parameters of different cryptocurrencies')
        ch3 = input()
        if ch3 == '1':
            graph_hist_price(input("Enter the symbol of the Crypto whose graph over the years is to be displayed:"))
        elif ch3 == '2':
            pl.figure(facecolor='c', edgecolor='b')
            pl.plot(datafile['symbol'][1:10], datafile['market_cap'][1:10]/10**11, color='g', marker='d', markeredgecolor='m')
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
            pl.plot(datafile['symbol'][0:10], datafile['total_volume'][0:10], color='g', marker='d',
                    markeredgecolor='m')
            pl.show()
        else:
            print("INVALID INPUT ERROR")
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break

    elif ch == '4':
        print('LIVEE PRICES!!!')
        live_prices(input("Enter the symbol of the Crypto whose live price is to be displayed:"))

        var = input("Enter symbol of crypto(in CAPS):")
        print("The live price of", var, "in USD is", live_price_cmc(var))
        print("")
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '5':
        print("Different currency prices")
        ch1 = input("Enter symbol of crypto:")
        no = input('How many currencies do you want to convert to? : ')
        lis2, lis1 = [], []
        if no.isdigit():
            print('Enter currency symbol (eg:INR)')
            for i in range(0, int(no)):
                lis2.append(input(str(i+1) + ": "))
        else:
            print("INVALID INPUT ERROR")
        for i in range(0, len(lis2)):
            val = currency_price(ch1, lis2[i])
            print('Price of', ch1, 'in', lis2[i], ': ', val)
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '6':
        print('Different quantities of a crypto')
        quantities(input("Enter symbol of crypto(In CAPS): "))
        print('')
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    else:
        print('INVALID INPUT ERROR')
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
print("L you're OUT")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(datafile[['id', 'name', 'current_price']])
