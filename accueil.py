import streamlit as st

st.header(":blue[Aide à la décisions : Bitcoin, Ethereum et Binance coin]",divider=True)
st.write("Avant de commencer dans les paramètres activer le theme sombre et le Wide mode ")


st.subheader(":blue[Long terme]")
st.markdown("""
    <h2 style="font-size: 20px; color: white;text-align: center;">
        1) Graphique des OHLC des cours du Bitcoin, de l'Ethereum et du Binance Coin en mensuel et hebdomadaire
    </h2>
    <h2 style="font-size: 20px; color: white;text-align: center; ">
        2) Histogramme des volumes d'échanges en dizaines de milliers de dollars en mensuel et hebdomadaire
    </h2>
    """, unsafe_allow_html=True)

st.subheader(":blue[Indicateurs]")

st.markdown("""
    <h2 style="font-size: 20px; color: white; text-align: center;">
        1) Graphique OHLC avec les bandes de Bollinger
    </h2>
    <h2 style="font-size: 20px; color: white; text-align: center;">
        2) Graphique Relative Strength Index
    </h2>
    <h2 style="font-size: 20px; color: white; text-align: center;">
        3) Moyenne mobile exponentielle (Up et Down)
    </h2>
    """, unsafe_allow_html=True)
st.subheader(":blue[Prévisions]")
st.markdown("""
    <h2 style="font-size: 20px; color: white;text-align: center;">
        1) Tableau de positions conseillé
    </h2>
    <h2 style="font-size: 20px; color: white;text-align: center; ">
        2) Graphique prévisions des crypto monnaies à l'aide du lissage exponentiel simple
    </h2>
    """, unsafe_allow_html=True)