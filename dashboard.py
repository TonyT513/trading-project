import streamlit as st
import psycopg2
import pandas as pd

# Connect to your Postgres database
conn = psycopg2.connect(dbname="trading_logs", user="tonythompson")

# Query trades table
df = pd.read_sql("SELECT * FROM trades ORDER BY timestamp DESC", conn)

# Streamlit UI
st.title("Trade Log Dashboard")
st.dataframe(df)
