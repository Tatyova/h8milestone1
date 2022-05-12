from matplotlib.ft2font import VERTICAL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 
from scipy import stats
from PIL import Image

def app():
    st.title('Hypothesis Testing')
    st.write('Saya asumsikan Average COGS Supermarket tahun lalu sebesar 3000 rata rata per hari, apakah hal tersebut menandakan COGS meningkat secara signifikan? saya akan melakukan *single sample one sided test* dengan tingkat signifikansi 0.05 H0: μ <= 3000 H1: μ > 3000')
    st.image(img, caption='Reject H0')
    st.write("P-value: 0.001993358289211853")
    st.write("Karena p-Value lebih kecil dari 0.05 maka kita tolak H0 sehingga dapat kita simpulkan adanya peningkatan signifikan Rata Rata COGS per hari dari tahun sebelumnya")
    
st.title('Hypothesis Testing')

img = Image.open(r'C:\Users\LENOVO\OneDrive\Desktop\h8dsft_Milestone1_Timothy\hypothesis.png')

st.write('Saya asumsikan Average COGS Supermarket tahun lalu sebesar 3000 rata rata per hari, apakah hal tersebut menandakan COGS meningkat secara signifikan? saya akan melakukan *single sample one sided test* dengan tingkat signifikansi 0.05 H0: μ <= 3000 H1: μ > 3000')

st.image(img, caption='Reject H0')

st.write("P-value: 0.001993358289211853")

st.write("Karena p-Value lebih kecil dari 0.05 maka kita tolak H0 sehingga dapat kita simpulkan adanya peningkatan signifikan Rata Rata COGS per hari dari tahun sebelumnya")