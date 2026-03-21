import streamlit as st
from normalized_plot import show_normalized
from duration_plot import show_duration
from live_crypto import get_today_coin_plot
from streamlit_autorefresh import st_autorefresh

st.title("Crypto Dashboard 📊")

coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']

# -------------------------
# 1. NORMALIZED PLOT
# -------------------------
st.header("Normalized Plot 📈")

months_norm = st.number_input(
    "Normalized Plot: Enter number of months",
    min_value=1,
    max_value=60,
    value=12,  # default 12 months
    key="norm_months"
)
days_norm = months_norm * 30

with st.spinner("Loading normalized plot..."):
    fig_norm = show_normalized(coins, days_norm)
    st.plotly_chart(fig_norm, use_container_width=True)

# -------------------------
# 2. DURATION PLOT
# -------------------------
st.header("Duration Plot 📊")

coin_dur = st.selectbox("Duration Plot: Select Coin", coins, index=0)  # default bitcoin

months_dur = st.number_input(
    f"Duration Plot ({coin_dur}): Enter number of months",
    min_value=1,
    max_value=60,
    value=12,  # default 12 months
    key="dur_months"
)

with st.spinner(f"Loading {coin_dur} duration plot..."):
    fig_dur = show_duration(coin_dur, months_dur)
    st.plotly_chart(fig_dur, use_container_width=True)

# -------------------------
# 3. LIVE LINE PLOT
# -------------------------
st.header("Live Line Plot 🔴")

coin_live = st.selectbox("Live Plot: Select Coin", coins, index=0)  # default bitcoin

st.write("Showing today's data (12:00 AM → Now)")

# auto-refresh every 5 sec
st_autorefresh(interval=5000, key="live_refresh")

fig_live = get_today_coin_plot(coin_live)
st.plotly_chart(fig_live, use_container_width=True)