import streamlit as st
import pandas as pd
import os

conn = st.connection('mysql', type='sql')

df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)
conn.close()

st.title('Säädata Helsingistä')
st.dataframe(df)
