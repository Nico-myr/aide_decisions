import streamlit as st
from streamlit_echarts import st_echarts
from module_prev import graph_prev_BTC,graph_prev_ETH,graph_prev_BNB,df_prix_conseil

tab1, tab2, tab3 = st.tabs(["BTC", "ETH", "BNB"])

with tab1 :
    st.header("prévision du Bitcoin")
    st.dataframe(df_prix_conseil['BTC'])
    st.plotly_chart(graph_prev_BTC)
    
    

with tab2 :
    st.header("prévision de l'Etherum")
    st.dataframe(df_prix_conseil['ETH'])
    st.plotly_chart(graph_prev_ETH)
    

with tab3 :
    st.header("prévision du Binance coin")
    st.dataframe(df_prix_conseil['BNB'])
    st.plotly_chart(graph_prev_BNB)
    
