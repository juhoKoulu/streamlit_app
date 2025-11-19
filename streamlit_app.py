import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_resource
def mySql():
	# Initialize connection.
	conn = st.connection('mysql', type='sql')
	# Perform query.
	df = conn.query('SELECT `Daily Max 8-hour CO Concentration` from co_table LIMIT 100;', ttl=600)
	return df

# Streamlit
def main():
	st.title("Plot data from MySql")
	st.write("Daily Max 8-hour CO Concentration")
	data = mySql()
	#plot data
	df2 = pd.DataFrame(data, columns=["Daily Max 8-hour CO Concentration"])
	dmcocon = px.line(df2, x=df2.index, y="Daily Max 8-hour CO Concentration")
	st.plotly_chart(dmcocon , use_container_width=True)

if __name__ == "__main__":
	main()
