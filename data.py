# importation packages
import requests
import pandas as pd
import numpy as np
from binance.client import Client



# Données OHLC

#OHLC BTC
url_BTC = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=1"
headers = {"accept": "application/json"}
response_BTC = requests.get(url_BTC, headers=headers)
BTC_json= response_BTC.json()

#OHCL ETH

url_ETH = "https://api.coingecko.com/api/v3/coins/ethereum/ohlc?vs_currency=usd&days=1"
headers = {"accept": "application/json"}
response_ETH = requests.get(url_ETH, headers=headers)
ETH_json=response_ETH.json()

#OHCL BNB 
url_BNB = "https://api.coingecko.com/api/v3/coins/binancecoin/ohlc?vs_currency=usd&days=1"
headers = {"accept": "application/json"}
response_BNB = requests.get(url_BNB, headers=headers)
BNB_json=response_BNB.json()

#nettoyage

#BTC
df_OHLC_BTC= pd.DataFrame(BTC_json, columns=["Timestamp", "Open", "High", "Low", "Close"])
df_OHLC_BTC['Timestamp'] = pd.to_datetime(df_OHLC_BTC['Timestamp'], unit='ms')
open_BTC = df_OHLC_BTC.drop(['High','Low','Close'], axis=1)
open_BTC.set_index("Timestamp", inplace=True)
x_BTC=pd.Series(open_BTC['Open'])

#ETH
df_OHLC_ETH= pd.DataFrame(ETH_json, columns=["Timestamp", "Open", "High", "Low", "Close"])
df_OHLC_ETH['Timestamp'] = pd.to_datetime(df_OHLC_ETH['Timestamp'], unit='ms')
open_ETH = df_OHLC_ETH.drop(['High','Low','Close'], axis=1)
open_ETH.set_index("Timestamp", inplace=True)
x_ETH=pd.Series(open_ETH['Open'])


#BNB
df_OHLC_BNB= pd.DataFrame(BNB_json, columns=["Timestamp", "Open", "High", "Low", "Close"])
df_OHLC_BNB['Timestamp'] = pd.to_datetime(df_OHLC_BNB['Timestamp'], unit='ms')
open_BNB = df_OHLC_BNB.drop(['High','Low','Close'], axis=1)
open_BNB.set_index("Timestamp", inplace=True)
x_BNB=pd.Series(open_BNB['Open'])

# API BInance OHLC avec volume historique 1 an 

#probleme lier au serveur changement url 

url = "https://api4.binance.com"
client = Client(url) #connection API public Binance 


symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
start_date = "1 year ago UTC"  # Période de 1 an

# Fonction pour obtenir des données OHLC
def get_ohlc_data(symbol, interval):
    klines = client.get_historical_klines(symbol, interval, start_date)
    # Transformation des données en DataFrame
    data = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 
        'close_time', 'quote_asset_volume', 'number_of_trades', 
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms') 

    return data[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    
    

data_monthly = {symbol: get_ohlc_data(symbol, Client.KLINE_INTERVAL_1MONTH) for symbol in symbols}
data_weekly = {symbol: get_ohlc_data(symbol, Client.KLINE_INTERVAL_1WEEK) for symbol in symbols}
data_daily= {symbol: get_ohlc_data(symbol, Client.KLINE_INTERVAL_3DAY ) for symbol in symbols}

#classement market cap 

#url = "https://api.coingecko.com/api/v3/coins/markets"
#params = {
    #"vs_currency": "usd",  
    #"per_page": 10,  # nbr de cryptos par page classé par rank market cap
    #"page": 1,  # nbr de page  
#}

#response = requests.get(url, params=params)
#response.raise_for_status()
#classement = response.json()



def get_ohlc_data_yfinance(symbol, interval, start_date="2023-01-01"):
    
    data = yf.download(tickers=symbol, interval=interval, start=start_date)
     
    return data

intervals = ["1mo", "1wk"]

data_BTC = {interval: get_ohlc_data_yfinance(symbol='BTC-USD', interval=interval) for interval in intervals}
data_ETH = {interval: get_ohlc_data_yfinance(symbol='ETH-USD', interval=interval) for interval in intervals}
data_BNB = {interval: get_ohlc_data_yfinance(symbol='BNB-USD', interval=interval) for interval in intervals}

df_btc_lt_W=pd.DataFrame(data_BTC['1wk'])
df_btc_lt_M=pd.DataFrame(data_BTC['1mo'])

df_eth_lt_W=pd.DataFrame(data_ETH['1wk'])
df_eth_lt_M=pd.DataFrame(data_ETH['1mo'])

df_bnb_lt_W=pd.DataFrame(data_BNB['1wk'])
df_bnb_lt_M=pd.DataFrame(data_BNB['1mo'])


