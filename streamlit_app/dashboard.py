import streamlit as st
import pandas as pd
import requests

st.title("Pharmaceutical Sales Forecast Dashboard")

try:
    response = requests.get("http://localhost:8000/forecast")
    forecast = response.json()
    df = pd.DataFrame(forecast)
    st.line_chart(df.set_index("ds")["yhat1"])
    st.dataframe(df)
except Exception as e:
    st.warning(f"Could not load forecast data: {e}")