import pandas as pd
import numpy as np
from binance.client import Client
from binance.exceptions import BinanceAPIException

client = Client('api_key', 'secret_key')
api_key = ''
secret_key = ''

def tickers():
    tickers = pd.DataFrame(client.get_ticker())
    # isolates the symbol and volume
    tickers = tickers.loc[:, ['symbol', 'volume']]
    # floats volume
    tickers['volume'] = tickers.loc[:, ['volume']].astype(float)
    tickers = tickers.loc[tickers['volume'] >= 150000, 'symbol']
    return tickers

tickers = tickers()

def test_iterdf(tickers):
    try:
        print('Running 1m')
        _5m = [pd.DataFrame(client.get_historical_klines(i, client.KLINE_INTERVAL_1HOUR, "10 September, 2018")) for i in tickers]

    except BinanceAPIException as e:
        print(e.status_code)
        print(e.message)

    return _5m

klines = test_iterdf(tickers)
k_len = len(klines)

def tick_check():
    mask = np.ones(len(klines), dtype=bool)

    for i in range(len(klines)):
        if klines[i].empty == True:
            mask[[i]] = False
    return mask
mask = tick_check()

def clean_data():    

    print('running clean_data')
    try:
        list = []
        for i in range(len(klines)):
            if klines[i].empty == True:
                list.append('1')
                del klines[i]
    except:
        print('working on it')
    for i in list:
        if i == '1':
            clean_data()
    symbol = []
    for i in range(len(tickers)):
        if mask[i] == True:
            symbol.append(tickers.iloc[i])

    return symbol


clean_data()
tickers = clean_data()


def change_klines_to_np():
    for i in range(len(klines)):
        klines[i] = klines[i].values

    return print('klines is numpy')


change_klines_to_np()

        
Columns = ["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", 
           "Quote asset volume", "Number of trades", "Taker buy base asset volume", 
           "Taker buy quote asset volume", "Can be ignored"]

#add in try/except for length mismatch error
def get_labeled_data(klines, columns=Columns):
    for j, df in enumerate(klines):
        df.columns = columns
        klines[j] = df.drop("Can be ignored", axis = 1) # Drop column
    return klines
get_labeled_data(klines, columns=Columns)
    
for i in range(len(t)):
    if t[i] == l[0]:
        l.pop(i)
        t[i] = np.nan
        t[i].dropna()

