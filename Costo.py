import numpy as np
import streamlit as st
import pandas as pd

st.write(''' Predicción del costo de actividades  ''')
st.image("imgproyecto.png", caption="predicción de costos.")

st.header('Datos de la actividad')

def user_input_features():
    Presupuesto = st.number_input('Presupuesto:', min_value=0.0, value=0.0, step=1.0)
    Tiempo invertido = st.number_input('Tiempo invertido (min):', min_value=0.0, value=0.0, step=1.0)
    Tipo = st.number_input('Tipo de actividad (1 a 6):', min_value=1, max_value=6, value=1, step=1)
    Momento = st.number_input('Momento (0 = mañana, 1 = tarde, 2 = noche):', min_value=0, max_value=3, value=0, step=1)
    No. de Personas = st.number_input('Número de personas:', min_value=1, value=1, step=1)

    user_input_data = {
        'Presupuesto': Presupuesto,
        'Tiempo invertido': Tiempo_min,
        'Tipo': Tipo,
        'Momento': Momento,
        'No. de personas': Personas,
    }

    features = pd.DataFrame(user_input_data, index=[0])
    return features

df = user_input_features()

# Cargar tu dataset real
datos = pd.read_csv('registrosdgg_limpio.csv')

# Variables para el modelo
X = datos[['Presupuesto', 'Tiempo invertido', 'Tipo', 'Momento', 'No. de personas']]
y = datos['Costo']

# Entrenamiento exactamente igual que tu código
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1613808
)

LR = LinearRegression()
LR.fit(X_train, y_train)

# Coeficientes
b = LR.coef_
b0 = LR.intercept_

# Predicción manual, igual que tu código original
prediccion = (
    b0
    + b[0] * df['Presupuesto']
    + b[1] * df['Tiempo invertido']
    + b[2] * df['Tipo']
    + b[3] * df['Momento']
    + b[4] * df['No. de ersonas']
)

st.subheader('Cálculo del costo estimado')
st.write('El costo estimado es: $', float(prediccion))
