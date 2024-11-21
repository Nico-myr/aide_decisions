import streamlit as st
from module_indicateur import graph_BB_BTC,graph_BB_ETH,graph_BB_BNB,graph_rsi_BTC,graph_rsi_ETH,graph_rsi_BNB,graph_EMA_BTC,graph_EMA_ETH,graph_EMA_BNB

tab1, tab2, tab3 = st.tabs(["BTC", "ETH", "BNB"])

with tab1 :
    st.header("indicateurs du Bitcoin")
    st.plotly_chart(graph_BB_BTC)
    st.plotly_chart(graph_rsi_BTC)
    st.plotly_chart(graph_EMA_BTC)

with tab2 :
    st.header("indicateurs de l'Etherum")
    st.plotly_chart(graph_BB_ETH)
    st.plotly_chart(graph_rsi_ETH)
    st.plotly_chart(graph_EMA_ETH)
with tab3 :
    st.header("indicateurs du Binance coin")
    st.plotly_chart(graph_BB_BNB)
    st.plotly_chart(graph_rsi_BNB)
    st.plotly_chart(graph_EMA_BNB)