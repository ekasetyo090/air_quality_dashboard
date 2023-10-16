import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime as dt
sns.set(style='dark')

def create_df_tren(df):
    list_kolom = ['hari angka','hari','pukul']
    df_temp = df.drop(labels=list_kolom , axis=1)
    df_temp['tanggal'] = pd.to_datetime(df_temp['tanggal'], format="%Y-%m-%d %H:%M:%S")
    return df_temp

def create_df_day_name(df):
    df_temp = df.groupby(by="hari angka")['debu total'].mean().reset_index()
    df_temp['hari'] =  df_temp.index.map({0: 'Senin',1: 'Selasa',2: 'Rabu', 
                                          3: 'Kamis',4: 'Jumat',5: 'Sabtu',
                                          6: 'Minggu'})
    return df_temp

def create_df_day_hour(df, period):
    if period != 'All':
        df_temp = df.loc[df['hari'] == period].copy()
        df_temp = df_temp.sort_values(by='pukul', ascending=True).reset_index()
    else:
        df_temp = df.sort_values(by='pukul', ascending=True).reset_index()
        
    df_temp = df_temp.groupby(by='pukul')['debu total'].mean().reset_index()
    return df_temp



df_all = pd.read_csv('all_data.csv')

# Mengubah tipe data min_date dan max_date menjadi datetime.datetime
min_date = dt.datetime.strptime(df_all['tanggal'].min(), "%Y-%m-%d %H:%M:%S")

max_date = dt.datetime.strptime(df_all['tanggal'].max(), "%Y-%m-%d %H:%M:%S")

 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://res.cloudinary.com/dk0z4ums3/image/upload/v1693394503/attached_image/6-penyebab-polusi-udara-dan-cara-mengurangi-paparannya-0-alodokter.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    period = st.selectbox(
        label="Hari",
        options=('All','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu')
    )

main_df = df_all[(df_all["tanggal"] >= str(start_date)) & (df_all["tanggal"] <= str(end_date))]
    
df_tren = create_df_tren(main_df)
df_day_name = create_df_day_name(main_df)
df_day_hour = create_df_day_hour(main_df, period)
    
# plot number of daily orders (2021)
st.header('Polusi Debu Beijing Dashboard :mask:')
st.subheader(f'Total Konsentrasi Pada Rentang Waktu {str(start_date)} dan {str(end_date)}')

fig = plt.figure(figsize =(11, 5))
list_warna = ['#FF6347']
my_palette = sns.color_palette(list_warna)
sns.set_palette(my_palette)
sns.lineplot(x='tanggal', y='debu total', data=df_tren)
#plt.xticks(range(len(df_tren)), df_tren['tanggal'], rotation=45)
plt.xlabel('waktu')
plt.ylabel('Jumlah Partikel Debu')
plt.title(f'Konsetrasi Total (PM 2.5 & PM 10) {str(start_date)} dan {str(end_date)}')
st.pyplot(fig)
    

    
st.subheader(f'Rata-rata Polusi Di Hari Yang Berbeda ({str(start_date)} dan {str(end_date)})')   
list_warna = []
for i in df_day_name['debu total']:
    if i == df_day_name['debu total'].max():
        list_warna.append('#FF0000')
    else:
        list_warna.append('#FF6347')

my_palette = sns.color_palette(list_warna)
sns.set_palette(my_palette)    
fig = plt.figure(figsize =(11, 5))
sns.barplot(x='hari', y='debu total', data=df_day_name)
plt.xlabel(f'Hari')
plt.ylabel('Jumlah Partikel Debu')
plt.title('Hari Paling Berdebu')
st.pyplot(fig)

st.subheader(f'Rata-rata Polusi Berdasarkan Waktu Di Hari "{period}" Pada ({str(start_date)} dan {str(end_date)})')

list_warna = ['#FF0000']
my_palette = sns.color_palette(list_warna)
sns.set_palette(my_palette)    
fig = plt.figure(figsize =(11, 5))
sns.lineplot(x='pukul', y='debu total', data=df_day_hour)
plt.xlabel('Pukul')
plt.ylabel('Jumlah Partikel Debu')
plt.title('Hari Paling Berdebu')
st.pyplot(fig)


    