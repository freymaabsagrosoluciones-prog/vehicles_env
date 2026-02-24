import pandas as pd 
import streamlit as st
import plotly.express as px 

st.set_page_config(page_title = "mandos",layout="wide")
st.title("analisis de datos")

@st.cache_data
def load_data():
    df=(pd.read_csv("vehicles_us.csv"))
    return df

df = load_data()
"""""boton histograma"""""

st.header("historial general")

if st.button("construir histograma"):
    st.write("creando histograma de precios")

fig = px.histogram(df, x="price", title= "distribucion precios vehiculos")
st.plotly_chart(fig)


"""mostrar datos"""
df=load_data()
st.subheader("vista previa conjunto de datos")
st.write(df.head())
"""informacion general """
st.subheader("clasificacion de vehiculos")
st.write(f"numero de filas{df.shape[0]}")
st.write(f"numero de columnas {df.shape[1]}") 

"""barra lateral """
st.sidebar.header("filtros")
if "model_year" in df.columns:
    years=sorted(df["model_year"].dropna().unique())
    selected_year = st.sidebar.selectbox("selecciona un año",years)
    filtered_df = df[df["model_year"]==selected_year]
else:
    filtered_df = df

"""""histograma filtrado """""
st.subheader ("histograma de precio")
if "price" in filtered_df.columns:
    fig_hist=px.histogram(filtered_df, x="price", nbins=50, title="distribucion de precio")
    st.plotly_chart(fig_hist,use_container_width=True)


"""grafico de dispersion"""

st.subheader("relacion entre odometo y precio")

if "odometer" in filtered_df.columns and "price" in filtered_df.columns:
    fig= px.scatter (filtered_df, x="odometer", y="price", title="odometro vs price",)

st.plotly_chart(fig)









