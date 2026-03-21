import streamlit as st
from streamlit_autorefresh import st_autorefresh

from normalized_plot import show_normalized
from duration_plot import show_duration
from live_crypto import get_today_coin_plot
from correlation_analysis import correlation_heatmap
from histogram_analysis import returns_histogram
from moving_average import moving_average_plot
from regression_analysis import regression_profit_prediction

st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("📊 Crypto Dashboard - All Analyses")

# List of coins
coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']
default_coin = coins[0]  # e.g., bitcoin
ma_window = 7  # default moving average window

# -------------------------
# 1. Normalized Plot
# -------------------------
st.header("Normalized Crypto Trends 📈")
months_norm = st.number_input(
    "Months for Normalized Plot",
    min_value=1, max_value=60, value=12, key="norm_months"
)
days_norm = months_norm * 30
with st.spinner("Loading Normalized Plot..."):
    fig_norm = show_normalized(coins, days_norm)
st.plotly_chart(fig_norm, use_container_width=True)

# -------------------------
# 2. Duration Plot
# -------------------------
st.header(f"Duration Plot 📊")
coin_dur = st.selectbox("Select Coin for Duration Plot", coins, index=0)
months_dur = st.number_input(
    f"Months for Duration Plot {coin_dur}",
    min_value=1, max_value=60, value=12, key="dur_months"
)
with st.spinner("Loading Duration Plot..."):
    fig_dur = show_duration(coin_dur, months_dur)
st.plotly_chart(fig_dur, use_container_width=True)


# -------------------------
# 3. Live Line Plot
# -------------------------
st.header("Live Line Plot 🔴")

coin_live = st.selectbox("Select Coin for Live Plot", coins, index=0,key="coin_live")

st.write("Auto-refreshes every 5 seconds")

st_autorefresh(interval=5000, key="live_refresh")

with st.spinner("Loading Live Plot..."):
    fig_live = get_today_coin_plot(coin_live)

st.plotly_chart(fig_live, use_container_width=True)


# -------------------------
# 4. Correlation Heatmap
# -------------------------
st.header("Correlation Heatmap 🔥")

months_corr = st.number_input(
    "Months for Correlation Heatmap",
    min_value=1, max_value=60, value=12, key="corr_months_input"
)

with st.spinner("Computing correlation heatmap..."):
    fig_corr = correlation_heatmap(coins, months_corr)

st.plotly_chart(fig_corr, use_container_width=True)


# -------------------------
# 5. Returns Histogram
# -------------------------
st.header("Histogram of Daily Returns 📊")

months_hist = st.number_input(
    "Months for Histogram",
    min_value=1, max_value=60, value=12, key="hist_months_input"
)

with st.spinner("Computing histogram..."):
    fig_hist = returns_histogram(coins, months_hist)

st.plotly_chart(fig_hist, use_container_width=True)


# -------------------------
# 6. Moving Average
# -------------------------
st.header("Moving Average 🟢")

coin_ma = st.selectbox("Select Coin for Moving Average", coins, index=0)

months_ma = st.number_input(
    f"Months for Moving Average ({coin_ma})",
    min_value=1, max_value=60, value=12, key="ma_months_input"
)

window_ma = st.slider("Moving Average Window (days)", 2, 30, 7)

with st.spinner("Calculating moving average..."):
    fig_ma = moving_average_plot(coin_ma, months_ma, window_ma)

st.plotly_chart(fig_ma, use_container_width=True)


# -------------------------
# 7. Regression Analysis
# -------------------------
st.header("Regression Analysis 📈")

months_reg = st.number_input(
    "Months for Regression Analysis",
    min_value=1, max_value=60, value=12, key="reg_months_input"
)

with st.spinner("Computing regression predictions..."):
    df_pred = regression_profit_prediction(coins, months_reg)

st.dataframe(df_pred)


# -------------------------
# 8. Market Cap Pie Chart
# -------------------------
st.header("Crypto Market Cap Distribution 🥧")

with st.spinner("Loading market cap pie chart..."):
    fig_cat = crypto_category_pie(coins)

st.plotly_chart(fig_cat, use_container_width=True)