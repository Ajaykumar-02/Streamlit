import streamlit as st
import pandas as pd

st.title("Chai sales Dashboard")

file = st.file_uploader("Upload your Csv file ",type = ['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
        

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by cities",cities)
    filtterd_data = df[df["City"] == selected_city ]
    st.dataframe(filtterd_data)
