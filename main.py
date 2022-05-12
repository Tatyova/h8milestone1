import pandas as pd
import numpy as np
import streamlit as st 

st.sidebar.subheader('Sidebar Menu')

pages = st.sidebar.selection('Select Page', options=['Data Visualization', 'Hypothesis Testing'])

if pages == 'Data Visualization':
    st.header('Data Visualization')
    
elif pages == 'Hypothesis Testing':
    st.header('Hypothesis Testing')
