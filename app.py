import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de anuncios de coches en EE.UU.')

# Casilla para histograma
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro de los coches')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para diagrama de dispersión
if st.checkbox('Mostrar gráfico de dispersión odómetro vs precio'):
    st.write('Diagrama de dispersión entre odómetro y precio')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)