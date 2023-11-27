import textwrap
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import turtle
import time
import pandas as pd
import matplotlib.pyplot as pl
from datetime import datetime as dt
datafile = pd.read_csv("Grade_12_full_data_csv_file.csv")
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
datafile['symbol'] = datafile['symbol'].str.upper()
print(datafile[['name', 'symbol']])

print("Welcome to the Cryptocurrency Analysis and Visualization Program!\n"
      "In the dynamic landscape of digital finance, understanding and tracking cryptocurrency trends is crucial for both enthusiasts and investors.\n"
      "This program aims to provide users with a comprehensive toolset to explore, analyze, and visualize various aspects of the cryptocurrency market.\n"
      "From live price updates to historical trends, this program offers valuable insights into the ever-evolving world of digital assets.")
print('This is a program that helps view and analyse trends in cryptocurrency with mesmerizing visual plots and statistics.')

print('')


def menu1(ch1):
    url1 = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    parameters1 = {'symbol': ch1}
    headers1 = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'bde04074-f1e4-4a6f-888e-9783d15a400b'}
    session1 = Session()
    session1.headers.update(headers1)
    try:
        response = session1.get(url1, params=parameters1)
        data_main = json.loads(response.text)
        print(data_main)
        fdata = data_main['data'][ch1][0]['description']
        fordata = textwrap.fill(fdata, width=150)
        print('')
        print(fordata)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("API ERROR:", e)


def menu2(ch5):
    url = "https://min-api.cryptocompare.com/data/v2/histoday"
    params = {"fsym": ch5, "tsym": "USD", 'limit': 58, 'aggregate': 30}
    response = requests.get(url, params=params)
    data = response.json()

    a1 = data['Data']
    b1 = a1['Data']
    c1 = len(b1)
    lis = []
    date = []
    for j in range(0, c1):
        lis.append(b1[j]['high'])
        a1 = b1[j]['time']
        date.append(dt.utcfromtimestamp(a1).date())

    ut = data['Data']['TimeFrom']
    ut1 = data['Data']['TimeTo']
    dt1 = dt.utcfromtimestamp(ut)
    print("Start Time:", dt1)
    dt2 = dt.utcfromtimestamp(ut1)
    print("End Time:", dt2)
    d1 = dt1.date()
    d2 = dt2.date()
    print('This is the list of items getting graphed:\n', lis)
    ylabel = 'Price of ' + ch5 + '(in USD)'
    title = 'Price of ' + ch5 + ' from ' + str(d1) + ' to ' + str(d2)
    pl.figure(facecolor='c', edgecolor='b')
    pl.plot(date, lis, color='g', marker='.', markeredgecolor='m')
    pl.grid()
    pl.xlabel('Year')
    pl.ylabel(ylabel)
    pl.xticks(rotation=45, ha='right')
    pl.title(title)
    max_price = max(lis)
    current_price = lis[-1]
    middle_point = len(date) // 2
    pl.axhline(max_price, linestyle='--', color='r', label='Max Price')
    pl.axhline(current_price, linestyle='--', color='b', label='Current Price')
    pl.annotate(f'Max Price: {max_price:.2f} USD', xy=(date[middle_point], max_price),
                xytext=(date[middle_point], max_price + (max_price/100)), color='r', ha='center', va='bottom', fontsize=10)

    pl.annotate(f'Current Price: {current_price:.2f} USD', xy=(date[middle_point], current_price),
                xytext=(date[-1], current_price + (current_price/10)), color='b', ha='center', va='center', fontsize=10)

    pl.legend()
    pl.show()


def menu3(ch8):
    if ch8 == '1':
        pl.figure(facecolor='gold', edgecolor='k')
        pl.plot(datafile['symbol'][2:20], datafile['current_price'][2:20], color='maroon', marker='o',
                markeredgecolor='b')
        pl.grid()
        pl.xlabel('Cryptocurrencies')
        pl.ylabel('Price (in USD)')
        pl.xticks(rotation=45, ha='right')
        pl.title('Prices for various cryptocurrencies')
        pl.show()
    elif ch8 == '2':
        pl.figure(facecolor='lightcoral', edgecolor='k')
        pl.plot(datafile['symbol'][1:20], datafile['market_cap'][1:20] / 10 ** 11, color='maroon', marker='o',
                markeredgecolor='b')
        pl.grid()
        pl.xlabel('Cryptocurrencies')
        pl.ylabel('Market Cap (in USD)(*10^10)')
        pl.xticks(rotation=45, ha='right')
        pl.title('Market Cap for various cryptocurrencies')
        pl.show()
    elif ch8 == '3':
        pl.figure(facecolor='cyan', edgecolor='k')
        pl.bar(datafile['symbol'][0:10], datafile['total_volume'][0:10] / 10 ** 10, color='khaki')
        pl.plot(datafile['symbol'][0:10], datafile['total_volume'][0:10] / 10 ** 10, color='g', marker='o',
                markeredgecolor='m')
        pl.grid()
        pl.xlabel('Cryptocurrencies')
        pl.ylabel('Total Volume(in USD)(*10^10)')
        pl.xticks(rotation=45, ha='right')
        pl.title('Total Volume for various cryptocurrencies')
        pl.show()
    elif ch8 == '4':
        pl.figure(facecolor='thistle', edgecolor='k')
        pl.bar(datafile['symbol'][0:10], datafile['market_cap_change_percentage_24h'][0:10], color='royalblue')
        pl.plot(datafile['symbol'][0:10], datafile['market_cap_change_percentage_24h'][0:10], color='g', marker='d',
                markeredgecolor='m')
        pl.grid()
        pl.xlabel('Cryptocurrencies')
        pl.ylabel('Market Cap')
        pl.xticks(rotation=45, ha='right')
        pl.title('Market Cap change percentage for various cryptocurrencies')
        pl.show()
    elif ch8 == '5':
        pl.figure(facecolor='silver', edgecolor='k')
        pl.plot(datafile['symbol'][3:17], datafile['ath'][3:17], color='g', marker='o', markeredgecolor='m')
        pl.grid()
        pl.xlabel('Cryptocurrencies')
        pl.ylabel('All time high price (in USD)')
        pl.xticks(rotation=45, ha='right')
        pl.title('All time high prices for various cryptocurrencies')
        pl.show()
    elif ch8 == '6':
        pl.figure(facecolor='khaki', edgecolor='k')
        pl.plot(datafile['symbol'][2:11], datafile['atl'][2:11], color='g', marker='o', markeredgecolor='m')
        pl.grid()
        pl.xlabel('Cryptocurrencies')
        pl.ylabel('All time low price (in USD)')
        pl.xticks(rotation=45, ha='right')
        pl.title('All time low prices for various cryptocurrencies')
        pl.show()


def menu4(ch2):
    url = "https://min-api.cryptocompare.com/data/price"
    params = {"fsym": ch2, "tsyms": "USD"}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        price_in_usd = data["USD"]
        print("The live price of", ch2, "in USD is", price_in_usd)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("API ERROR:", e)


def menu5(ch3):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {'symbol': ch3, "convert": "USD"}

    try:
        headers = {"X-CMC_PRO_API_KEY": 'bde04074-f1e4-4a6f-888e-9783d15a400b'}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        price = data["data"][ch3]['quote']['USD']['price']
        return price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("API ERROR:", e)


def menu6(ch4, cur):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {'symbol': ch4, "convert": cur}

    try:
        headers = {"X-CMC_PRO_API_KEY": 'bde04074-f1e4-4a6f-888e-9783d15a400b'}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        price = data["data"][ch4]['quote'][cur]['price']
        return price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("API ERROR:", e)


def menu7(ch6):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {'symbol': ch6, 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'bde04074-f1e4-4a6f-888e-9783d15a400b'}

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        b1 = data['data'][ch6][0]
        print('Id:', b1['id'])
        print('Name:', b1['name'])
        print('Symbol:', b1['symbol'])
        c1 = b1['quote']['USD']
        print('Price:', c1['price'])
        print('24 hour volume:', c1['volume_24h'])
        print('Percent change in 1 hour:', c1['percent_change_1h'])
        print('Percent change in 7 days:', c1['percent_change_7d'])
        print('Percent change in 90 days:', c1['percent_change_90d'])
        print('Market cap:', c1['market_cap'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("API ERROR:", e)


while True:
    print("Select an option by entering the corresponding option.")
    print('1. Basic introduction to CRYPTOCURRENCY\n'
          '2. Details about different cryptocurrencies\n'
          '3. View graphs about recent trends in cryptocurrency\n'
          '4. View live prices of various cryptocurrencies\n'
          '5. View prices of cryptos in different currencies\n'
          '6. View different stats of a cryptocurrency\n'
          '7. View database items and edit/modify')
    ch = input(":")
    if ch == '1':
        print("CRYPTOCURRENCY!!!!!!!!!!!!!!!")
        print('''Cryptocurrency: A Revolution in Digital Finance

Cryptocurrency is a groundbreaking concept that has transformed the landscape of traditional finance.
Emerging in the wake of the 2008 financial crisis, it aimed to address issues of centralization, security, and accessibility.
This essay explores the fundamental aspects of cryptocurrency, its underlying technology, and its impact on the global economy.
Cryptocurrency is a form of digital or virtual currency that uses cryptography for security.
Unlike traditional currencies issued by governments and central banks, cryptocurrencies operate on decentralized networks based on blockchain technology.
The first and most well-known cryptocurrency, Bitcoin, was introduced in 2009 by an anonymous entity known as Satoshi Nakamoto.
Bitcoin laid the foundation for numerous other cryptocurrencies collectively known as altcoins.

Blockchain Technology: At the core of most cryptocurrencies is blockchain, a distributed ledger that records all transactions across a network of computers.
Each block contains a list of transactions and a reference to the previous block, creating a secure and transparent chain.
The decentralized nature of blockchain eliminates the need for intermediaries, providing a more efficient and secure way to conduct transactions.
This technology has applications beyond cryptocurrencies, such as supply chain management, voting systems, and smart contracts.

Cryptocurrencies serve various purposes beyond being a medium of exchange.
Some, like Bitcoin, primarily function as a store of value and a hedge against inflation.
Others, like Ethereum, enable the creation of decentralized applications (DApps) through smart contracts.
Stablecoins are designed to minimize price volatility by pegging their value to a fiat currency or other assets.
Understanding the diversity of cryptocurrencies is crucial for grasping their broader impact on the financial ecosystem.

Cryptocurrencies have disrupted traditional financial systems, offering new opportunities and challenges.
The decentralized nature of cryptocurrencies allows for financial inclusion, enabling people without access to traditional banking services to participate in the global economy.
However, regulatory challenges, concerns about illicit activities, and market volatility have prompted governments and 
financial institutions to adopt various approaches, ranging from acceptance to skepticism.

In conclusion, cryptocurrency represents a transformative force in the world of finance.
Its underlying blockchain technology has implications far beyond currency, influencing industries and sectors globally.
As cryptocurrencies continue to evolve, finding a balance between innovation and regulation will be crucial for their sustained growth and integration into mainstream finance.''')
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break

    elif ch == '2':
        print("Informations")
        menu1(input("Enter the symbol of the Crypto whose info is to be displayed:"))
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '3':
        print("GRAPHHSSS(tbd)")
        print('Enter 1 to view graphs of prices in the last 5 years of a cryptocurrency\n'
              'Enter 2 to view graphs of various other parameters of different cryptocurrencies')
        var2 = input(':')
        if var2 == '1':
            menu2(input("Enter the symbol of the Crypto whose graph over the years is to be displayed:"))
        elif var2 == '2':
            while True:
                print("To view graphs of any of these parameter enter corresponding number:\n"
                      "1. Current Price\n"
                      "2. Market Cap\n"
                      "3. Total Volume\n"
                      "4. Market Cap Change Percentage \n"
                      "5. All time high prices\n"
                      "6. All time low prices")
                var3 = input(":")
                menu3(var3)
                cont = input('Enter 1 to go back to graph menu:')
                if cont != '1':
                    break

        else:
            print("INVALID INPUT ERROR")
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break

    elif ch == '4':
        print('LIVEE PRICES!!!')
        var = input("Enter symbol of crypto(in CAPS):")
        menu4(var)
        print("The live price of", var, "in USD is", menu5(var))
        print("")
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '5':
        print("Different currency prices")
        var1 = input("Enter symbol of crypto:")
        no = input('How many currencies do you want to convert to? : ')
        lis2, lis1 = [], []
        if no.isdigit():
            print('Enter currency symbol (eg:INR)')
            for i in range(0, int(no)):
                lis2.append(input(str(i+1) + ": "))
        else:
            print("INVALID INPUT ERROR")
        for i in range(0, len(lis2)):
            val = menu6(var1, lis2[i])
            print('Price of', var1, 'in', lis2[i], ': ', val)
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '6':
        print('Different quantities of a crypto')
        menu7(input("Enter symbol of crypto(In CAPS): "))
        print('')
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    elif ch == '7':
        print("EDITING DATABASE")

        while True:
            var4 = input("Enter symbol of Crypto from given list(in CAPS):")
            df = datafile[datafile['symbol'] == var4]
            if not df.empty:
                print("Details for", var4, ":")
                print('Cryptocurrency name: ', df.loc[df.index[0], 'name'])
                print('Symbol: ', df.loc[df.index[0], 'symbol'])
                print('Current price: ', df.loc[df.index[0], 'current_price'])
                print('Market Cap: ', df.loc[df.index[0], 'market_cap'])
                print('Total Volume: ', df.loc[df.index[0], 'total_volume'])
                print('Market Cap Change Percentage: ', df.loc[df.index[0], 'market_cap_change_percentage_24h'])
                print('All Time High: ', df.loc[df.index[0], 'ath'])
                print('All Time Low: ', df.loc[df.index[0], 'atl'])
                print("\nIs the given data accurate?\nEnter 1 if inaccurate")
                a = input(":")
                if a == '1':
                    print('\nIf you feel the data items are wrong, feel free to update them')
                    d = input('Enter 1 to update the data:')
                    while True:
                        if d == '1':
                            print('Which data is wrong?\n'
                                  '1. Current Price\n'
                                  '2. Market Cap\n'
                                  '3. Total Volume\n'
                                  '4. Market Cap Change Percentage\n'
                                  '5. All TIme High\n'
                                  '6. All Time Low')
                            b = input(':')
                            if b == '1':
                                c = input("Enter correct price of " + var4 + ": ")
                                df.loc[df.index[0], 'current_price'] = c
                                datafile.loc[df.index[0], 'current_price'] = c
                                print("Updated price of", var4, 'is', df.loc[df.index[0], 'current_price'], 'USD')
                            elif b == '2':
                                c = input("Enter correct market cap of " + var4 + ": ")
                                df.loc[df.index[0], 'market_cap'] = c
                                datafile.loc[df.index[0], 'market_cap'] = c
                                print("Updated market cap of", var4, 'is', df.loc[df.index[0], 'market_cap'], 'USD')
                            elif b == '3':
                                c = input("Enter correct total volume of " + var4 + ": ")
                                df.loc[df.index[0], 'total_volume'] = c
                                datafile.loc[df.index[0], 'total_volume'] = c
                                print("Updated total volume of", var4, 'is', df.loc[df.index[0], 'total_volume'], 'USD')
                            elif b == '4':
                                c = input("Enter correct market cap change percentage of " + var4 + ": ")
                                df.loc[df.index[0], 'market_cap_change_percentage_24h'] = c
                                datafile.loc[df.index[0], 'market_cap_change_percentage_24h'] = c
                                print("Updated market cap change percentage of", var4, 'is', df.loc[df.index[0], 'market_cap_change_percentage_24h'])
                            elif b == '5':
                                c = input("Enter correct all time high of " + var4 + ": ")
                                df.loc[df.index[0], 'ath'] = c
                                datafile.loc[df.index[0], 'ath'] = c
                                print("Updated all time high of", var4, 'is', df.loc[df.index[0], 'ath'], 'USD')
                            elif b == '6':
                                c = input("Enter correct all time low of " + var4 + ": ")
                                df.loc[df.index[0], 'atl'] = c
                                datafile.loc[df.index[0], 'atl'] = c
                                print("Updated all time low of", var4, 'is', df.loc[df.index[0], 'atl'], 'USD')

                            cont = input("Enter 1 to update more data items(else press enter):")
                            if cont != '1':
                                break
                        else:
                            print("Thank you!")
                            print("We will check and update the data ASAP")
                            break
                    cont = input("Enter 1 to go back to database values(else press enter):")
                    if cont != '1':
                        break
                else:
                    print("Thank you!")
                    cont = input("Enter 1 to go back to database values(else press enter):")
                    if cont != '1':
                        break
            else:
                print("INVALID SYMBOL ERROR")
                print("No information found for", var4)
                print("Enter valid symbol")
                cont = input("Enter 1 to go back to database values(else press enter):")
                if cont != '1':
                    break
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
    else:
        print('INVALID INPUT ERROR')
        cont = input("Enter 1 to go back to menu:")
        if cont != '1':
            break
print('')
print('Thank you for your time!\nHope you liked this program!')
print('')
datafile.to_csv("Grade_12_full_data_csv_file.csv", index=False)

print(datafile)
