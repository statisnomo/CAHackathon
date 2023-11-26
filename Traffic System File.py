import pandas as pd
import matplotlib.pyplot as pl
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import textwrap
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import turtle
import time

from datetime import datetime as dt

pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
'''
serno = list(range(1, 51))
state = ['Agra', 'Ahmedabad', 'Allahabad(Prayagraj)', 'Amritsar', 'Asansol Durgapur', 'Aurangabad', 'Bengaluru',
         'Bhopal', 'Chandigarh', 'Coimbatore', 'Chennai', 'Delhi', 'Dhanbad', 'Faridabad', 'Ghaziabad', 'Gwalior',
         'Hyderabad',
         'Indore', 'Jabalpur', 'Jaipur', 'Jamshedpur', 'Jodhpur', 'Kannur', 'Kanpur', 'Khozikode', 'Kochi',
         'Kolkata', 'Kollam',
         'Kota', 'Lucknow', 'Ludhiana', 'Madurai', 'Mallapuram', 'Meerut', 'Mumbai', 'Nagpur', 'Nashik', 'Patna',
         'Pune',
         'Raipur', 'Rajkot', 'Srinagar', 'Surat', 'Thiruvanthapuram', 'Thrissur', 'Tiruchirapalli',
         'Vadodra', 'Varanasi', 'Vijaywada city', 'Vizaq']
stagJ = [31, 82, 123, 0, 4, 0, 347, 0, 72, 139, 367, 497, 9, 6, 27, 0, 227, 16, 0, 179,
         20, 2, 0, 57, 184, 278, 39, 0, 0, 60, 12, 0, 0, 0, 28, 16, 0, 0, 27, 44, 0, 0, 28,
         99, 228, 229, 7, 44, 77, 98]
roabJ = [23, 12, 53, 0, 3, 0, 33, 0, 31, 35, 45, 105, 2, 2, 11, 0, 27, 0, 32, 32, 9, 1, 0, 13, 13, 12, 9, 0, 0, 7,
         25, 0, 0, 0, 33, 9, 0, 0, 3, 21, 0, 0, 23, 78, 58, 78, 0, 0, 198, 13]
oth = [17, 41, 21, 0, 2, 0, 232, 0, 4, 97, 255, 12, 23, 1, 10, 0, 43, 0, 61, 13, 23, 7, 0, 21, 134, 129, 32, 0, 0,
       4, 13, 0, 0, 0, 66, 28, 0, 0, 8, 53, 119, 4, 60, 41, 119, 0, 87, 67, 23, 34]
tna = [30, 78, 1, 7, 3, 694, 0, 96, 146, 464, 440, 55, 14, 59, 5, 746, 9, 87, 90, 1, 1, 1, 17, 299, 204, 127, 0, 0,
       307, 105, 9, 0, 0, 107, 100, 0, 0, 16, 201, 812, 37, 440, 45, 76, 237, 276, 464, 68, 299, 127]
perinj = [3, 16, 66, 0, 1, 3, 398, 0, 20, 14, 709, 111, 55, 6, 23, 3, 52, 16, 5, 93, 5, 1, 13, 84, 255, 23, 5, 0, 6,
          6, 0, 6, 3, 13, 3, 4, 0, 0, 55, 5, 1, 13, 24, 44, 56, 78, 86, 45, 67, 19]
SIGNAL = {'Serial No': serno, 'States/UTs': state, 'Staggered Junction': stagJ,
          'Round about Junction': roabJ, 'Others': oth, 'Total number of Accidents': tna, 'Persons Injured': perinj}
SUG = pd.DataFrame(SIGNAL)
TLS = [31, 82, 123, 0, 4, 0, 347, 0, 72, 139, 367, 497, 9, 6, 27, 0, 227, 16, 0, 179, 20, 2,
       0, 57, 184, 278, 39, 60, 12, 0, 0, 0, 28, 16, 0, 0, 27, 44, 0, 0, 28, 99, 228, 229, 7, 109, 44, 77, 98,
       189]
PC = [3, 12, 53, 0, 3, 0, 33, 0, 31, 35, 45, 105, 2, 2, 11, 0, 27, 0, 32, 32, 9, 1, 0, 13, 13,
      12, 9, 0, 0, 7, 25, 0, 0, 0, 33, 9, 0, 0, 3, 21, 0, 0, 23, 78, 58, 78, 0, 0, 198, 13]
SS = [7, 41, 21, 30, 71, 29, 12, 7, 13, 20, 21, 5, 13, 3, 16, 0, 7, 0, 7, 0, 7, 24, 31, 27, 10, 5, 15,
      3, 0, 7, 0, 7, 31, 23, 17, 7, 24, 31, 27, 10, 5, 15, 3, 0, 7, 0, 7, 8, 20, 0]
PI = [24, 29, 20, 3, 71, 29, 12, 7, 13, 20, 21, 5, 13, 3, 16, 0, 7, 0, 7, 0, 7, 24, 31, 27, 10, 5,
      15, 3, 0, 7, 0, 7, 24, 31, 27, 10, 5, 15, 3, 0, 7, 0, 7, 24, 31, 27, 10, 5, 8, 27]
data = {'S.No': serno, 'States/UTs': state, 'Traffic Light Signal': TLS, 'Police Controlled': PC, 'Stop Sign': SS,
        'Persons Injured': PI}
df = pd.DataFrame(data)
print('Hello user, welcome to our program')
print('This program primarily aims on eliminating the increased wait times at junctions and allow the easy flow of traffic')
print('You will now be asked to view statistics in order to get a grasp.')
print()
print('1 View the Accidents Classified according to Type of Junction \n'
      '2 View the Accidents Classified according to the type of control')
AC = int(input('Enter the option number: '))
if AC == 1:
    print(SUG)
    print('The graphs will now be shown')
    pl.plot(tna[0:10], state[0:10])
    pl.plot(stagJ[0:10], state[0:10])
    pl.plot(roabJ[0:10], state[0:10])
    pl.plot(perinj[0:10], state[0:10])
    pl.plot(oth[0:10], state[0:10])
    pl.grid()
    pl.xlabel('Accidents')
    pl.ylabel('Cities,Towns')
    pl.legend(['Total No of Accidents', 'Staggered Junction', 'Roundabout Junction', 'Persons Injured', 'Others'], loc='upper right')
    pl.show()
elif AC == 2:
    print(df)
    print('The graphs will now be shown')
    pl.plot(TLS[0:10], state[0:10])
    pl.plot(PC[0:10], state[0:10])
    pl.plot(SS[0:10], state[0:10])
    pl.plot(PI[0:10], state[0:10])
    pl.grid()
    pl.xlabel('Accidents')
    pl.ylabel('Cities,Towns')
    pl.legend(['Traffic Light Signal', 'Police Controlled', 'Stop Sign', 'Persons Injured'], loc='upper right')
    pl.show()'''


datafile = pd.read_csv("Grade_12_full_data_csv_file.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
datafile['symbol'] = datafile['symbol'].str.upper()
print(datafile[['name', 'symbol']])

print('Welcome to this program about Cryptocurrency')
print('This is a program that helps view and analyse trends in cryptocurrency with mesmerizing visual plots and statistics.')
print("Comment: Write a bigger intro")
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
        a = data_main['data'][ch1][0]['description']
        d = textwrap.fill(a, width=150)
        print('')
        print(d)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("API ERROR:", e)


def menu2(ch5):
    url = "https://min-api.cryptocompare.com/data/v2/histoday"
    params = {"fsym": ch5, "tsym": "USD", 'limit': 58, 'aggregate': 30}
    response = requests.get(url, params=params)
    data = response.json()

    a = data['Data']
    b = a['Data']
    c = len(b)
    lis = []
    date = []
    for j in range(0, c):
        lis.append(b[j]['high'])
        a = b[j]['time']
        date.append(dt.utcfromtimestamp(a).date())

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
        b = data['data'][ch6][0]
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
        print("API ERROR:", e)


def run():
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
                    lis2.append(input(str(i + 1) + ": "))
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
                                    print("Updated total volume of", var4, 'is', df.loc[df.index[0], 'total_volume'],
                                          'USD')
                                elif b == '4':
                                    c = input("Enter correct market cap change percentage of " + var4 + ": ")
                                    df.loc[df.index[0], 'market_cap_change_percentage_24h'] = c
                                    datafile.loc[df.index[0], 'market_cap_change_percentage_24h'] = c
                                    print("Updated market cap change percentage of", var4, 'is',
                                          df.loc[df.index[0], 'market_cap_change_percentage_24h'])
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
    print("L you're OUT")
    datafile.to_csv("Grade_12_full_data_csv_file.csv")


def change_color():
    color = colorchooser.askcolor()
    hexcolor = color[1]
    root.config(bg=hexcolor)


# Initialize a Tkinter window
root = tk.Tk()
root.title("CryptoCurrency")
root.geometry("1200x1200")


# Function to display statistics
def display_statistics():
    option = combo.get()
    if option == "View":
        text.delete('1.0', tk.END)
        text.insert(tk.END, datafile.to_string())
    elif option == "View Accidents by Control Type":
        text.delete('1.0', tk.END)
        text.insert(tk.END, datafile.to_string())


# Function to display graphs
def display_graphs():
    pl.figure(figsize=(10, 6))
    option = combo.get()
    if option == "View Accidents by Junction Type":
        for col in datafile.columns[5:7]:
            pl.barh(datafile['current_price'][2:12], datafile[col][2:12], label=col)
    else:
        for col in datafile.columns[5   :7]:
            pl.barh(datafile['current_price'][2:12], datafile[col][2:12], label=col)

    # Customize plot appearance here

    pl.xlabel('Accidents')
    pl.ylabel('Cities/Towns')
    pl.legend(loc='upper right')
    pl.title("Accidents Statistics")
    pl.tight_layout()
    pl.show()


# Create a label
label = ttk.Label(root, text="Choose an option:")
label.pack(pady=10)

# Create a combo box for user selection
options = ['1. Basic introduction to CRYPTOCURRENCY', '2. Details about different cryptocurrencies'
           '3. View graphs about recent trends in cryptocurrency', '4. View live prices of various cryptocurrencies',
           '5. View prices of cryptos in different currencies', '6. View different stats of a cryptocurrency',
           '7. View database items and edit/modify']
combo = ttk.Combobox(root, values=options)
combo.pack()

# Create a button to display statistics
statistics_button = ttk.Button(root, text="Run", command=display_statistics())
statistics_button.pack(pady=10)

# Create a button to display graphs
graphs_button = ttk.Button(root, text="Display Graphs", command=display_graphs())
graphs_button.pack()

cc_button = ttk.Button(root, text="change background color ", command=change_color())
cc_button.pack()
# Create a text box to display statistics
text = tk.Text(root, height=20, width=130)
text.pack()

root.mainloop()

