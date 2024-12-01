
import pandas as pd

# Importation données 
from data import x_BTC, x_ETH, x_BNB

# Fonction SKTIME
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error
from sktime.utils.plotting import plot_series

# Visualisation
import plotly.graph_objects as go


# Prévision BTC

# Préparation échantillon de  test et horizon test
BTC_train, BTC_test = temporal_train_test_split(x_BTC,test_size= 10)
fh_test = ForecastingHorizon(BTC_test.index, is_relative=False)

# Horizon prévision 
fh_dates = pd.date_range(start=x_BTC.index[-1], periods=10, freq='30min')
fh_pred = ForecastingHorizon(fh_dates, is_relative=False)

# Utilisation du modèle 
model= ExponentialSmoothing(trend="add", seasonal=None)
model_test_BTC= model.fit(BTC_train)
model_pred_BTC=model.fit(x_BTC) 

# Prévision et test 
BTC_perf=model_test_BTC.predict(fh_test)
BTC_pred = model_pred_BTC.predict(fh_pred)

# MAPE (test de qualité)
mape_BTC = mean_absolute_percentage_error(BTC_test, BTC_pred)*100

# Création des dataframes
df_BTC_train= pd.DataFrame(BTC_train)
df_BTC_pred=pd.DataFrame(BTC_pred)
BTC_fusion=pd.DataFrame(pd.concat([BTC_train, BTC_test], axis=0))



# Prévision eth

# Préparation échantillon de  test et horizon test
ETH_train, ETH_test = temporal_train_test_split(x_ETH,test_size= 10)
fh_test = ForecastingHorizon(ETH_test.index, is_relative=False)

# Horizon prévision 
fh_dates = pd.date_range(start=x_ETH.index[-1], periods=10, freq='30min')
fh_pred = ForecastingHorizon(fh_dates, is_relative=False)

# Utilisation du modèle 
model= ExponentialSmoothing(trend="add", seasonal=None)
model_test_ETH= model.fit(ETH_train)
model_pred_ETH=model.fit(x_ETH) 

# Prévision et test 

ETH_perf=model_test_ETH.predict(fh_test)
ETH_pred = model_pred_ETH.predict(fh_pred)

# MAPE (test de qualité)
mape_ETH = mean_absolute_percentage_error(ETH_test, ETH_pred)*100

# Création des dataframes
df_ETH_train= pd.DataFrame(ETH_train)
df_ETH_pred = pd.DataFrame(ETH_pred)
ETH_fusion=pd.DataFrame(pd.concat([ETH_train, ETH_test], axis=0))



# Prévision BNB

# Préparation échantillon de  test et horizon test
BNB_train, BNB_test = temporal_train_test_split(x_BNB,test_size= 10)
fh_test = ForecastingHorizon(BNB_test.index, is_relative=False)

# Horizon prévision 
fh_dates = pd.date_range(start=x_BNB.index[-1], periods=10, freq='30min')
fh_pred = ForecastingHorizon(fh_dates, is_relative=False)

# Utilisation du modèle 
model= ExponentialSmoothing(trend="add", seasonal=None)
model_test_BNB= model.fit(BNB_train)
model_pred_BNB=model.fit(x_BNB) 

# Prévision et test 
BNB_perf=model_test_BNB.predict(fh_test)
BNB_pred = model_pred_BNB.predict(fh_pred)

# MAPE (test de qualité)
mape_BNB = mean_absolute_percentage_error(BNB_test, BNB_pred)*100

# Création des dataframes
df_BNB_train= pd.DataFrame(BNB_train)
df_BNB_pred = pd.DataFrame(BNB_pred)
BNB_fusion=pd.DataFrame(pd.concat([BNB_train, BNB_test], axis=0))





# Fonction graphique prévision
def graph_prev_2(index_fusion, valeur_y_fusion, index_pred, valeur_pred):
    # convertir 
    index_fusion = pd.Series(index_fusion).values
    valeur_y_fusion = pd.Series(valeur_y_fusion).values
    index_pred = pd.Series(index_pred).values
    valeur_pred = pd.Series(valeur_pred).values
    
   
    df_fusion = pd.DataFrame({'Date': index_fusion, 'Valeur': valeur_y_fusion, 'Type': 'cours'})
    df_pred = pd.DataFrame({'Date': index_pred, 'Valeur': valeur_pred, 'Type': 'prévision'})
    
    
    frames = []
    max_length_fusion = len(df_fusion)
    max_length_pred = len(df_pred)

    
    fig = go.Figure()

    # ligne cours et prévision
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Cours', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Prévision', line=dict(color='red')))

    # ordre d'apparition des lines
    for i in range(1, max_length_fusion + max_length_pred + 1):
        frame_data = []

        
        if i <= max_length_fusion:
            frame_data.append(go.Scatter(x=df_fusion['Date'][:i], y=df_fusion['Valeur'][:i], mode='lines', line=dict(color='blue')))
            frame_data.append(go.Scatter(x=[], y=[], mode='lines', line=dict(color='red')))  # Prévision vide avant la fin du cours
        
        else:
            frame_data.append(go.Scatter(x=df_fusion['Date'], y=df_fusion['Valeur'], mode='lines', line=dict(color='blue')))
            j = i - max_length_fusion  # index pour les données de prévision
            frame_data.append(go.Scatter(x=df_pred['Date'][:j], y=df_pred['Valeur'][:j], mode='lines', line=dict(color='red')))

        
        frames.append(go.Frame(data=frame_data, name=str(i)))

     
    fig.frames = frames

    fig.update_layout(
        xaxis_title="Temps",
        yaxis_title="prix (usd)",
        title="Prévisions ",
        hovermode="x unified",
        template="plotly_dark",
        updatemenus=[{
            "type": "buttons",
            "showactive": False,
            "buttons": [{
                "label": "Play",
                "method": "animate",
                "args": [None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True}]
            }]
        }]
    )
    return fig
    
 # Application fonction graphique
graph_prev_BTC=graph_prev_2(BTC_fusion.index, BTC_fusion['Open'], df_BTC_pred.index, df_BTC_pred['Open'])
graph_prev_ETH=graph_prev_2(ETH_fusion.index,ETH_fusion['Open'],df_ETH_pred.index,df_ETH_pred['Open'])
graph_prev_BNB=graph_prev_2(BNB_fusion.index,BNB_fusion['Open'],df_BNB_pred.index,df_BNB_pred['Open'])



# Tableau conseil position

def prix(prevision):
    prix_entrée = round(min(prevision), 2)
    prix_cible = round(max(prevision), 2)
    prix_stop = round(prix_entrée * 0.99, 2)

    return prix_entrée, prix_cible, prix_stop

prix_conseil_BTC= prix(BTC_pred)
prix_conseil_ETH=prix(ETH_pred)
prix_conseil_BNB=prix(BNB_pred)

df_prix_conseil = pd.DataFrame({
    "BTC":{
        "prix_entrée":prix_conseil_BTC[0],
        "prix_cible" : prix_conseil_BTC[1],
        "prix_sortie" : prix_conseil_BTC[2],

    },
    "ETH":{
        "prix_entrée":prix_conseil_ETH[0],
        "prix_cible" : prix_conseil_ETH[1],
        "prix_sortie" : prix_conseil_ETH[2],       
    } ,
    "BNB":{
        "prix_entrée":prix_conseil_BNB[0],
        "prix_cible" : prix_conseil_BNB[1],
        "prix_sortie" : prix_conseil_BNB[2],       
    } 
})
