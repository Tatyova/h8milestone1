import datavisualization, hypo_test
import streamlit as st 

PAGES = {'Data Visualization': datavisualization,
         'Hypothesis Testing': hypo_test}

selected = st.sidebar.selectbox('Please Select Page', options=PAGES.keys())
page = PAGES[selected]

page.app()