#main streamlit code gui

import numpy as np
import pandas as pd
import streamlit as st 
import plotly.express as px 

#loading data
@st.cache_data
def load_data():
    path='data/kc_house_data.csv'
    df=pd.read_csv(path)
    return df

#call the load func
with st.spinner("loading data...."):
    df=load_data()

#title
st.title("House Price Analysis") 
    
#display dataset
if st.checkbox("Show Dataset",True):
    st.subheader("Dataset")  
    st.dataframe(df)  