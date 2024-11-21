
import pandas as pd
import numpy as np
import  plotly.express  as  px
import plotly.graph_objects as go

from data import data_monthly, data_weekly#, classement

#classement 

#df_classement= pd.DataFrame(classement,columns=["name","price_change_percentage_24h"])
#df_classement.rename(columns={"name": "symbol", "price_change_percentage_24h": "variations (%) "}, inplace=True)
#df_classement["variations (%) "] = df_classement["variations (%) "].round(2)


# historique des prix 


def graph_OHLC(df, interval, symbol):

    fig = go.Figure()
    
    #bougies OHLC
    fig.add_trace(go.Candlestick(
        x=df['timestamp'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name="OHLC",
        increasing_line_color='green',
        decreasing_line_color= 'red',

        
    ))
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        title="Historique " + interval + " des prix" + symbol ,
        xaxis_title="Dates",
        yaxis_title="Prix en USDT"
        )
    return fig
    

#historique BTC

hist_BTC_sem=graph_OHLC(data_weekly['BTCUSDT'],"hebdomadaire", " du BTC")
hist_BTC_m=graph_OHLC(data_monthly['BTCUSDT']," mensuel ", " du BTC")

#ETH

hist_ETH_sem=graph_OHLC(data_weekly['ETHUSDT'],"hebdomadaire", " de l'ETH")
hist_ETH_m=graph_OHLC(data_monthly['ETHUSDT']," mensuel ", " de l'ETH")

#BNB

hist_BNB_sem=graph_OHLC(data_weekly['BNBUSDT'],"hebdomadaire", " du BNB")
hist_BNB_m=graph_OHLC(data_monthly['BNBUSDT']," mensuel ", " du BNB")


# historique des volumes 

def graph_hist_vol(df, interval, symbol,dtick_val):

    df['volume']=pd.to_numeric(df['volume'], errors='coerce')
    df['volume_conv']=(df['volume']/10000).round() # nouvelle col pour éviter les probleme de perfs
    fig = go.Figure()

    # Ajouter un histogramme pour le volume
    fig.add_trace(go.Bar(
        x=df['timestamp'], 
        y=df['volume_conv'],
        name='Volume',
        marker=dict(color='rgb(0, 0, 255, 255)')
    ))
    
    # Mise en forme du graphique
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        title=f"Historique " + interval + "des volumes " + symbol,
        xaxis_title="Dates",
        yaxis_title="Volume (en dizaine de milliers)",
        yaxis=dict(
            tickmode="linear",         
            dtick=dtick_val)
    )
    return fig
    
    
    

#BTC

vol_BTC_M=graph_hist_vol(data_monthly['BTCUSDT'], 'mensuel ', 'BTC',50)
vol_BTC_W=graph_hist_vol(data_weekly['BTCUSDT'], 'hebdomadaire', 'BTC',10)

#ETH


vol_ETH_M=graph_hist_vol(data_monthly['ETHUSDT'], 'mensuel ', 'ETH',250)
vol_ETH_W=graph_hist_vol(data_weekly['ETHUSDT'], 'hebdomadaire ', 'ETH',100)

#BNB


vol_BNB_M=graph_hist_vol(data_monthly['BNBUSDT'], 'mensuel ', 'BNB',1000)
vol_BNB_W=graph_hist_vol(data_weekly['BNBUSDT'], 'hebdomadaire ', 'BNB',100)



