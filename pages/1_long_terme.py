import streamlit as st 
from module_long_term import  hist_BTC_m, hist_BTC_sem, hist_ETH_m, hist_ETH_sem, hist_BNB_m, hist_BNB_sem,vol_BTC_M,vol_BTC_W,vol_ETH_M,vol_ETH_W,vol_BNB_M,vol_BNB_W#, df_classement


col2, col3 = st.columns(2)
   

with col2:
    st.header("Cours à long terme")
    cours_BTC, cours_ETH, cours_BNB = st.tabs(["BTC", "ETH", "BNB"])
    
    with cours_BTC :
        st.plotly_chart(hist_BTC_m)
        st.plotly_chart(hist_BTC_sem)
        
        
        

    with cours_ETH:
        st.plotly_chart(hist_ETH_m)
        st.plotly_chart(hist_ETH_sem)
        
        
        

    with cours_BNB:
        st.plotly_chart(hist_BNB_m)
        st.plotly_chart(hist_BNB_sem)
        
        

with col3 :
    st.header("Volume à long terme")
    vol_BTC, vol_ETH, vol_BNB = st.tabs(["BTC", "ETH", "BNB"])
    
    with vol_BTC:
        st.plotly_chart(vol_BTC_M)
        st.plotly_chart(vol_BTC_W)
       
        
                
    with vol_ETH:
        st.plotly_chart(vol_ETH_M)
        st.plotly_chart(vol_ETH_W)
        
        
                
    with vol_BNB:
        st.plotly_chart(vol_BNB_M)
        st.plotly_chart(vol_BNB_W)
        
        
        
