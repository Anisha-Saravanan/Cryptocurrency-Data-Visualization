# dashboard_chk.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from normalized_plot import show_normalized
from duration_plot import show_duration
from live_crypto import get_today_coin_plot

st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("📊 Crypto Dashboard")

# List of coins
coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']

# -------------------------
# 1. NORMALIZED PLOT
# -------------------------
st.header("Normalized Plot 📈")

months_norm = st.number_input(
    "Normalized Plot: Enter number of months",
    min_value=1,
    max_value=60,
    value=12,
    key="norm_months"
)
days_norm = months_norm * 30  # convert months → days

with st.spinner("Fetching normalized data..."):
    fig_norm = show_normalized(coins, days_norm)
st.plotly_chart(fig_norm, use_container_width=True)

# -------------------------
# 2. DURATION PLOT
# -------------------------
st.header("Duration Plot 📊")

coin_dur = st.selectbox("Select Coin for Duration Plot", coins)
months_dur = st.number_input(
    f"Duration Plot ({coin_dur.title()}): Enter number of months",
    min_value=1,
    max_value=60,
    value=12,
    key="dur_months"
)
days_dur = months_dur * 30

with st.spinner(f"Fetching {coin_dur.title()} duration data..."):
    fig_dur = show_duration(coin_dur, months_dur)
st.plotly_chart(fig_dur, use_container_width=True)

# -------------------------
# 3. LIVE LINE PLOT
# -------------------------
st.header("Live Line Plot 🔴")

coin_live = st.selectbox("Select Coin for Live Plot", coins, index=0)
st.write("Showing today's price (12:00 AM → now)")

# Auto-refresh every 5 seconds
st_autorefresh(interval=5000, key="live_refresh")

# Display live plot
fig_live = get_today_coin_plot(coin_live)
st.plotly_chart(fig_live, use_container_width=True)