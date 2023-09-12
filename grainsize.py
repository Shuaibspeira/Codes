import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Histogram Generator")

uploaded_file = st.file_uploader("Hochladen der Excel-Datei  ")

if uploaded_file is not None:
    df=pd.read_excel(uploaded_file, engine = 'openpyxl')
    st.dataframe(df)
    
    st.subheader("Grain size distribution")
    sns.histplot(data=df,element="bars",multiple="dodge",bins=10,kde=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
