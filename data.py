# importation packages
import requests
import pandas as pd
import numpy as np
import yfinance as yf
import pandas as pd



# Données OHLC (Open, Hight, Low, Close ), lien différents pour chaque symbols

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

#Préparation de données

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



#API YFINANCE pour historiquess prix et volume commençant le 1 janvier 2023

def get_ohlc_data_yfinance(symbol, interval, start_date="2023-01-01"):
    
    data = yf.download(tickers=symbol, interval=interval, start=start_date)
     
    return data

intervals = ["1mo", "1wk"]

data_BTC = {interval: get_ohlc_data_yfinance(symbol='BTC-USD', interval=interval) for interval in intervals}
data_ETH = {interval: get_ohlc_data_yfinance(symbol='ETH-USD', interval=interval) for interval in intervals}
data_BNB = {interval: get_ohlc_data_yfinance(symbol='BNB-USD', interval=interval) for interval in intervals}

#préparation des données pour l'historiques des prix et du volume

#BTC
df_btc_lt_W=pd.DataFrame(data_BTC['1wk'])
df_btc_lt_M=pd.DataFrame(data_BTC['1mo'])
#ETH
df_eth_lt_W=pd.DataFrame(data_ETH['1wk'])
df_eth_lt_M=pd.DataFrame(data_ETH['1mo'])
#BNB
df_bnb_lt_W=pd.DataFrame(data_BNB['1wk'])
df_bnb_lt_M=pd.DataFrame(data_BNB['1mo'])




