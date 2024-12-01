import pandas as pd
import plotly.graph_objects as go

from data import df_btc_lt_W,df_btc_lt_M,df_eth_lt_W,df_eth_lt_M,df_bnb_lt_W,df_bnb_lt_M


# Fonction graphique historique des prix 


def graph_OHLC(df, interval, symbol):

    fig = go.Figure()
    
    # type OHLC
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
    

#Application fonction historique des prix pour une période hebdomadaire et mensuel 

# BTC

hist_BTC_sem=graph_OHLC(df_btc_lt_W,"hebdomadaire", 'BTC-USD')
hist_BTC_m=graph_OHLC(df_btc_lt_M," mensuel ", 'BTC-USD')

# ETH

hist_ETH_sem=graph_OHLC(df_eth_lt_W,"hebdomadaire", 'ETH-USD')
hist_ETH_m=graph_OHLC(df_eth_lt_M," mensuel ", 'ETH-USD')

# BNB

hist_BNB_sem=graph_OHLC(df_bnb_lt_W,"hebdomadaire", 'BNB-USD')
hist_BNB_m=graph_OHLC(df_bnb_lt_M," mensuel ", 'BNB-USD')


# fonction graphique historique des volumes 

def graph_hist_vol(df, interval, symbol, dtick_val=0):
    
    #convertion d'unité (probleme d'affichage lier à streamlit )
    df['Volume'] = pd.to_numeric(df['Volume'][symbol], errors='coerce') #éviter erreur type de données
    df['Volume_conv'] = (df['Volume'][symbol] / 1000).round() # optimisation calcul (problème lier à la performance )
    
   
    fig = go.Figure()

    
    fig.add_trace(go.Bar(
        x=df.index,  
        y=df['Volume_conv'],  
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
            dtick=dtick_val # adaptation de l'échelle y 
        )
    )
    
    return fig
    
    
#Application fonction historique des volumes pour une période  hebdomadaire et mensuel 

#BTC
vol_BTC_M=graph_hist_vol(df_btc_lt_M, ' mensuel ', 'BTC-USD',100000000)
vol_BTC_W=graph_hist_vol(df_btc_lt_W, ' hebdomadaire ', 'BTC-USD',65000000)

#ETH
vol_ETH_M=graph_hist_vol(df_eth_lt_M, ' mensuel ', 'ETH-USD',100000000)
vol_ETH_W=graph_hist_vol(df_eth_lt_W, ' hebdomadaire ', 'ETH-USD',65000000)

#BNB
vol_BNB_M=graph_hist_vol(df_bnb_lt_M, ' mensuel ', 'BNB-USD',5000000)
vol_BNB_W=graph_hist_vol(df_bnb_lt_W, ' hebdomadaire ', 'BNB-USD',3500000)








