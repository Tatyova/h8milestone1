from itertools import count
from matplotlib.ft2font import VERTICAL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st 
from scipy import stats

def app():
    st.title('Myanmar Supermarket Behaviour Summary')
    st.write('Dataframe')
    st.subheader('Jumlah Produk yang dibeli per Gender')
    st.radio('Pilih Kategori', options= ss['Product line'].unique(), key=count)
    st.pyplot(fig)
    st.subheader('Tingkat Kepuasan Supermarket per Kota')
    st.selectbox('Pilih Kota', options= ss['City'].unique(), key=count)
    st.pyplot(fig2)
    st.subheader('Metode Pembayaran yang paling disenangi customer')
    st.radio('Metode Pembayaran:', options=sshr['Payment'].unique(), key=count)
    st.pyplot(fig3)
    st.subheader('Rating per Cabang Supermarket')
    st.selectbox('Pilih Cabang Supermarket', options= df['Branch'].unique(), key=count)
    st.pyplot(fig4)
    
    
st.title('Myanmar Supermarket Behaviour Summary')
st.write('Dataframe')
df = pd.read_csv('supermarket_sales - Sheet1.csv')
ss = df.copy()
del ss["Invoice ID"]
del ss["Tax 5%"]
del ss["Branch"]
del ss["Total"]
del ss["gross margin percentage"]
del ss["gross income"]

ssw = ss.drop(ss.index[ss['Gender'] == 'Male'])
del ssw['Unit price']
del ssw['cogs']
del ssw['Rating']

sshr = ss.drop(ss.index[ss['Rating'] < 8])
sshr

ss['Z-Score'] = stats.zscore(ss['cogs'])

ss['Date'] = pd.to_datetime(ss['Date'], errors='coerce')
daily_cogs = ss[['Date','cogs']].groupby('Date').sum()


selected = st.radio('Pilih Kategori', options= ss['Product line'].unique())

fig,ax = plt.subplots()
sns.histplot(df[df['Product line']==selected]['Gender'])

selected2 = st.selectbox('Pilih Kota', options= ss['City'].unique())

ss['Rating']= ss.Rating.astype(object)

fig2,ax = plt.subplots()
sns.scatterplot(ss[ss['City']==selected2]['Date'],
                ss[ss['City']==selected2]['Rating'])
plt.xticks(rotation=45)


selected3 = st.radio('Metode Pembayaran:', options=sshr['Payment'].unique())

fig3,ax = plt.subplots()
sns.histplot(sshr[sshr['Payment']==selected3]['Customer type'])

selected4 = st.selectbox('Pilih Cabang Supermarket', options= df['Branch'].unique())


fig4,ax = plt.subplots()
sns.scatterplot(df[df['Branch']==selected4]['Date'],
                df[df['Branch']==selected4]['Rating'])
plt.xticks(fontsize=4, rotation=90)