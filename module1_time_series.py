import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Module 1: Time Series", layout="wide")

# ---------------- TITLE ----------------
st.title("Module 1: Introduction to Time Series")
st.subheader("Interactive Concept Dashboard")

st.markdown("""
A **time series** is a sequence of observations recorded over time at regular intervals.
Examples include monthly sales, rainfall, temperature, and stock prices.
""")

st.divider()

# ---------------- DATA ----------------
np.random.seed(42)
dates = pd.date_range("2016-01", periods=72, freq="ME")

trend = np.linspace(100, 200, 72)
seasonal = 15 * np.sin(2 * np.pi * np.arange(72) / 12)
noise = np.random.normal(0, 6, 72)

series = trend + seasonal + noise
ts = pd.Series(series, index=dates)

# ---------------- RAW SERIES ----------------
st.header("Figure 1: Raw Time Series")

fig_raw = go.Figure()
fig_raw.add_trace(go.Scatter(x=ts.index, y=ts, name="Observed Series"))
fig_raw.update_layout(template="plotly_white")

st.plotly_chart(fig_raw, use_container_width=True)

st.markdown("""
**Interpretation:**  
The time series shows an overall upward trend with repeating seasonal fluctuations
and random variations.
""")

st.divider()

# ---------------- TREND (MOVING AVERAGE) ----------------
st.header("Figure 2: Trend Component")

trend_est = ts.rolling(window=12, center=True).mean()

fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=ts.index, y=trend_est, name="Trend"))
fig_trend.update_layout(template="plotly_white")

st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("""
**Interpretation:**  
The trend represents the long-term movement of the series,
ignoring short-term fluctuations.
""")

st.divider()

# ---------------- SEASONAL ----------------
st.header("Figure 3: Seasonal Component")

detrended = ts - trend_est
seasonal_est = detrended.groupby(detrended.index.month).mean()
seasonal_full = detrended.index.month.map(seasonal_est)

fig_seasonal = go.Figure()
fig_seasonal.add_trace(go.Scatter(x=ts.index, y=seasonal_full, name="Seasonal"))
fig_seasonal.update_layout(template="plotly_white")

st.plotly_chart(fig_seasonal, use_container_width=True)

st.markdown("""
**Interpretation:**  
The seasonal component shows a repeating annual pattern
that occurs at fixed intervals.
""")

st.divider()

# ---------------- IRREGULAR ----------------
st.header("Figure 4: Irregular Component")

irregular = ts - trend_est - seasonal_full

fig_irreg = go.Figure()
fig_irreg.add_trace(go.Scatter(x=ts.index, y=irregular, name="Irregular"))
fig_irreg.update_layout(template="plotly_white")

st.plotly_chart(fig_irreg, use_container_width=True)

st.markdown("""
**Interpretation:**  
The irregular component captures random fluctuations
that cannot be explained by trend or seasonality.
""")

st.divider()

# ---------------- MODEL ----------------
st.header("Additive Model")

st.markdown("""
The series follows the **Additive Model**:

### **Y = T + S + I**

This model is suitable when seasonal fluctuations remain
approximately constant over time.
""")

st.success("End of Module 1 ✔")
