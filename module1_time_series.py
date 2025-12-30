import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.seasonal import seasonal_decompose
Fix statsmodels import for cloud deployment

st.set_page_config(page_title="Module 1: Time Series", layout="wide")

st.title("Module 1: Introduction to Time Series")
st.subheader("Interactive Concept Dashboard")

st.markdown("""
A **time series** is a sequence of observations recorded over time at regular intervals.
Examples include monthly sales, yearly rainfall, and daily stock prices.
""")

np.random.seed(42)
dates = pd.date_range("2016-01", periods=72, freq="ME")
trend = np.linspace(100, 200, 72)
seasonal = 15 * np.sin(2 * np.pi * np.arange(72) / 12)
noise = np.random.normal(0, 6, 72)
ts = pd.Series(trend + seasonal + noise, index=dates)

st.header("Figure 1: Raw Time Series")

fig = go.Figure()
fig.add_trace(go.Scatter(x=ts.index, y=ts))
fig.update_layout(template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
**Interpretation:**  
The series shows an increasing trend with repeating seasonal patterns.
""")

decomp = seasonal_decompose(ts, model="additive", period=12)

st.header("Figure 2: Trend Component")
fig_t = go.Figure()
fig_t.add_trace(go.Scatter(x=ts.index, y=decomp.trend))
fig_t.update_layout(template="plotly_white")
st.plotly_chart(fig_t, use_container_width=True)

st.markdown("""
**Interpretation:**  
The trend represents long-term growth in the data.
""")

st.success("End of Module 1")

Add Module 1 Streamlit dashboard

