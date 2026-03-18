import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
st.header('Dashboard de Análise de Veículos')
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros') # escrever uma mensagem
    fig = px.histogram(car_data, x="odometer") # criar um histograma
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo

build_histogram = st.checkbox('Criar um histograma') # criar uma caixa de seleção

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para preço vs quilometragem')
    
    fig = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig, use_container_width=True)      