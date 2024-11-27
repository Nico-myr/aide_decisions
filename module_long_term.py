
import pandas as pd
import numpy as np
import  plotly.express  as  px
import plotly.graph_objects as go

from data import df_btc_lt_W,df_btc_lt_M,df_eth_lt_W,df_eth_lt_M,df_bnb_lt_W,df_bnb_lt_M#, classement

#classement 

#df_classement= pd.DataFrame(classement,columns=["name","price_change_percentage_24h"])
#df_classement.rename(columns={"name": "symbol", "price_change_percentage_24h": "variations (%) "}, inplace=True)
#df_classement["variations (%) "] = df_classement["variations (%) "].round(2)


# historique des prix 


def graph_OHLC(df, interval, symbol):

    fig = go.Figure()
    
    #bougies OHLC
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'][symbol],
        high=df['High'][symbol],
        low=df['Low'][symbol],
        close=df['Close'][symbol],
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

hist_BTC_sem=graph_OHLC(df_btc_lt_W,"hebdomadaire", 'BTC-USD')
hist_BTC_m=graph_OHLC(df_btc_lt_M," mensuel ", 'BTC-USD')

#ETH

hist_ETH_sem=graph_OHLC(df_eth_lt_W,"hebdomadaire", 'ETH-USD')
hist_ETH_m=graph_OHLC(df_eth_lt_M," mensuel ", 'ETH-USD')

#BNB

hist_BNB_sem=graph_OHLC(df_bnb_lt_W,"hebdomadaire", 'BNB-USD')
hist_BNB_m=graph_OHLC(df_bnb_lt_M," mensuel ", 'BNB-USD')


# historique des volumes 

def graph_hist_vol(df, interval, symbol, dtick_val=0):
    
    #convertion d'unité
    df['Volume'] = pd.to_numeric(df['Volume'][symbol], errors='coerce')
    df['Volume_conv'] = (df['Volume'][symbol] / 1000).round()
    
   
    fig = go.Figure()

    # Ajouter un histogramme pour le volume
    fig.add_trace(go.Bar(
        x=df.index,  # Vérifiez que 'Date' existe dans df
        y=df['Volume_conv'],  # Utilisez la nouvelle colonne
        name='Volume',
        marker=dict(color='rgb(128, 0, 128)')
        
    ))
    
    
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        title="Historique " +interval+ "des volumes " +symbol,
        xaxis_title="Dates",
        yaxis_title="Volume (en milliard )",
        yaxis=dict(
            tickmode="linear",
            dtick=dtick_val
        )
    )
    
    return fig
    
    
    

#BTC

vol_BTC_M=graph_hist_vol(df_btc_lt_M, ' mensuel ', 'BTC-USD',100000000)
vol_BTC_W=graph_hist_vol(df_btc_lt_W, ' hebdomadaire ', 'BTC-USD',65000000)

#ETH


vol_ETH_M=graph_hist_vol(df_eth_lt_M, ' mensuel ', 'ETH-USD',100000000)
vol_ETH_W=graph_hist_vol(df_eth_lt_W, ' hebdomadaire ', 'ETH-USD',65000000)

#BNB


vol_BNB_M=graph_hist_vol(df_bnb_lt_M, ' mensuel ', 'BNB-USD',5000000)
vol_BNB_W=graph_hist_vol(df_bnb_lt_W, ' hebdomadaire ', 'BNB-USD',3500000)




