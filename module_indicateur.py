#importation package 
import  plotly.express  as  px
import plotly.graph_objects as go

import pandas as pd
import numpy as np

from data import open_BTC,open_ETH,open_BNB,df_OHLC_BTC,df_OHLC_BNB,df_OHLC_ETH

#Graphique bougie et BB




def calcul_BB(prix, valeurs_passees=10, ecart=5):
    #tableau 1 dim pour calcul
    prix = np.asarray(prix).flatten()
    prix = pd.Series(prix)

    rolling_mean = prix.rolling(valeurs_passees, min_periods=1).mean()
    rolling_std = prix.rolling(valeurs_passees, min_periods=1).std()
    
    # Calcul des bandes de Bollinger
    bande_supp = rolling_mean + ecart * rolling_std
    bande_inf = rolling_mean - ecart * rolling_std
    
    return bande_supp.values, bande_inf.values


# Exemple d'appel à la fonction avec open_BTC
B_supp_BTC, B_inf_BTC = calcul_BB(open_BTC)
B_supp_ETH, B_inf_ETH = calcul_BB(open_ETH)
B_supp_BNB, B_inf_BNB = calcul_BB(open_BNB)







def graph_BB(df, bande_supp, bande_inf, nom):

    

    fig = go.Figure()
    
    #bougies OHLC
    fig.add_trace(go.Candlestick(
        x=df['Timestamp'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Prix",
        increasing_line_color='green',
        decreasing_line_color= 'red',

        
    ))
    
    # BB supp
    fig.add_trace(go.Scatter(
        x=df['Timestamp'],  
        y=bande_supp,  
        mode='lines',
        name='bande supérieur Bollinger',
        line=dict(color='red')
    ))
    
    #BB inf
    fig.add_trace(go.Scatter(
        x=df['Timestamp'],  
        y=bande_inf,    
        mode='lines',
        name='bande inférieure  Bollinger ',
        line=dict(color='green')
    ))
    fig.update_layout(template="seaborn",
                      xaxis_title="Périodes",
                      yaxis_title="prix en dollars ",
                      title="graphique Bandes Bollinger  "+nom)
    
    
    return fig

graph_BB_BTC=graph_BB(df_OHLC_BTC,B_supp_BTC, B_inf_BTC,nom = "du Bitcoin")
graph_BB_ETH=graph_BB(df_OHLC_ETH,B_supp_ETH, B_inf_ETH,nom = "d'Ethereum")
graph_BB_BNB=graph_BB(df_OHLC_BNB,B_supp_BNB, B_inf_BNB, nom= "du Binance Coin")




#RSI

def RSI_indica (prix, period=14):
    delta = prix.diff()
    up = delta.where(delta > 0, 0)  
    down = -delta.where(delta < 0, 0)

    # moyenne exponentielle  des gains et perte
    ema_up = up.ewm(alpha=1/period, min_periods=period).mean()
    ema_down = down.abs().ewm(alpha=1/period, min_periods=period).mean()
    rs = ema_up / ema_down
    rsi = 100 - 100 / (1 + rs)
    
    return rsi.iloc[period:], ema_up.iloc[period:], ema_down.iloc[period:]

BTC_rsi, BTC_ema_up, BTC_ema_down = RSI_indica(open_BTC['Open'])
ETH_rsi, ETH_ema_up, ETH_ema_down = RSI_indica(open_ETH['Open'])
BNB_rsi, BNB_ema_up, BNB_ema_down = RSI_indica(open_BNB['Open'])

def graph_RSI (rsi, ema_up, ema_down):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rsi.index, y=rsi, mode='lines', name='RSI', line=dict(color='blue')))
    fig.update_layout(
        title="RSI (Relative Strength Index)",
        xaxis_title="Périodes",
        yaxis_title="Valeurs en %",
        template="seaborn",  
        showlegend=True
    )

    
    return fig

graph_rsi_BTC =graph_RSI(BTC_rsi,BTC_ema_up,BTC_ema_down)
graph_rsi_ETH =graph_RSI(ETH_rsi,ETH_ema_up,ETH_ema_down)
graph_rsi_BNB =graph_RSI(BNB_rsi,BNB_ema_up,BNB_ema_down)

# EMA 
def graph_EMA(ema_up,ema_down):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ema_up.index, y=ema_up, mode='lines', name='EMA Up', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=ema_down.index, y=ema_down, mode='lines', name='EMA Down', line=dict(color='red')))
    fig.update_layout(
    title="EMA (Moyenne mobile exponentielle)",
    xaxis_title="Périodes",
    yaxis_title="Valeurs",
    template="seaborn",        
    showlegend=True
    )

    
    return fig

graph_EMA_BTC=graph_EMA(BTC_ema_up,BTC_ema_down)
graph_EMA_ETH=graph_EMA(ETH_ema_up,ETH_ema_down)
graph_EMA_BNB=graph_EMA(BNB_ema_up,BNB_ema_down)

