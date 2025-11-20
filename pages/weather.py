import streamlit as st
import mysql.connector
import pandas as pd
import os

mysql_user = os.getenv("MYSQL_USER");
mysql_password = os.getenv("MYSQL_PASSWORD");

conn = mysql.connector.connect(host='localhost', user=mysql_user, password=mysql_password, database='weather_db')
df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)
conn.close()

# Ensure timestamp is a datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort by timestamp ascending for plotting
df = df.sort_values("timestamp")

# Line chart for temperature
st.subheader("Temperature Over Time")
st.line_chart(df.set_index("timestamp")["temperature"])

st.title("Säädata Helsingistä")
st.dataframe(df)
