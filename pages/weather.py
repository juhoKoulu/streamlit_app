import streamlit as st
import os

conn = st.connection('mysql', type='sql')
df = conn.query('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', ttl=0)

st.title('Säädata Helsingistä')
st.dataframe(df)
