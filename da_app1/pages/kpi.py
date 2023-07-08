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
st.subheader("Key Performance Indicator")

#get the list of all columbs
cols=df.columns.tolist()
selected_cols=st.multiselect('Select Columns',cols)
st.write('You Selected: ',len(selected_cols),'columns')

#access datafeame column
#df['price']

#st.metric(label="Average Price",
          #value=round(df['price'].mean()),
          #delta=round(df['price'].std()))
          
          
for col in selected_cols:
    try:
        st.metric(label=f"Mean {col}",
          value=round(df['price'].mean()),
          delta=round(df['price'].std()))
        st.line_chart(df[col],use_container_width=True)
    except:
        st.error(f'Cannot display {col} numeric data')    


        