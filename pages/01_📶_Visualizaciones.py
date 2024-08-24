import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown(':chart_with_upwards_trend:')
st.markdown(':bar_chart:')

if st.checkbox('Mostrar textbox'):
    st.write('Hola streamlit')
#definimos solo las columnas que nos interesan
fields=['country','points','price','variety']
df=pd.read_csv('data/wine_reviews.csv',encoding='utf-8',usecols=fields)
df.dropna(inplace=True)

#st.dataframe(df)
#Mostrar un dataframe si hacemos clic en el checkbox
if st.checkbox('Mostrar df'):
    st.dataframe(df)
    
#Ver el encabezado o los ultimos registros del df
if st.checkbox('Vista de datos Head o Tail'):
    if st.button('Mostrar Head'):
        st.write(df.head())
    if st.button('Mostrar Tail'):
        st.write(df.tail())
    
dim=st.radio('Dimensión a mostrar:',('Filas','Columnas'),horizontal=True)
if dim=='Filas':
    st.write('Cantidad de filas:',df.shape[0])
else:
    st.write('Cantidad de columnas:',df.shape[1])
    
#colocar parametros para las graficas
#precio_limite=250
precio_limite=st.slider('Definir precio máximo',0,4000,250)


fig=plt.figure(figsize=(6,4))
sns.scatterplot(x='price',y='points',data=df[df['price']<precio_limite])
st.pyplot(fig)

countries_list=df['country'].unique().tolist()
countries=st.multiselect('Seleccione un/unos/pais/paises a analizar')
df_countries=df[df['country'].isin(countries)]
    
fig=plt.figure(figsize=(6,4))
sns.scatterplot(x='price',y='points',hue='country' ,data=df_countries)
st.pyplot(fig)

col1,col2=st.columns(2)
with col1:
    df_countries=df[df['country']=='Argentina']
    fig=plt.figure()
    sns.scatterplot(x='price',y='points',hue='country' ,data=df_countries)
    plt.title('Puntajes según precio para Argentina')
    st.pyplot(fig)
with col2:
    df_countries=df[df['country']=='Chile']
    fig=plt.figure()
    sns.scatterplot(x='price',y='points',hue='country' ,data=df_countries)
    plt.title('Puntajes según precio para Chile')
    st.pyplot(fig)
 










