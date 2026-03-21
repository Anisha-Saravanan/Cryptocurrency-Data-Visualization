# dashboard_chk.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from normalized_plot import show_normalized
from duration_plot import get_today_coin_plot
from correlation_analysis import correlation_heatmap
from histogram_analysis import returns_histogram
from moving_average import moving_average_plot
from regression_analysis import regression_profit_prediction
from geographic_analysis import crypto_category_pie

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
st.header(f"Duration Plot — {default_coin.title()} 📊")
months_dur = st.number_input(
    f"Months for Duration Plot ({default_coin.title()})",
    min_value=1, max_value=60, value=12, key="dur_months"
)
with st.spinner("Loading Duration Plot..."):
    fig_dur = show_duration(default_coin, months_dur)
st.plotly_chart(fig_dur, use_container_width=True)

# -------------------------
# 3. Live Line Plot
# -------------------------
st.header(f"Live Plot — {default_coin.title()} 🔴")
st.write("Auto-refreshes every 5 seconds")
st_autorefresh(interval=5000, key="live_refresh")
fig_live = get_today_coin_plot(default_coin)
st.plotly_chart(fig_live, use_container_width=True)

# -------------------------
# 4. Correlation Heatmap
# -------------------------
st.header("Correlation Heatmap of Daily Returns 🔥")
months_corr = st.number_input(
    "Months for Correlation Heatmap",
    min_value=1, max_value=60, value=12, key="corr_months"
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
    min_value=1, max_value=60, value=12, key="hist_months"
)
with st.spinner("Computing histogram..."):
    fig_hist = returns_histogram(coins, months_hist)
st.plotly_chart(fig_hist, use_container_width=True)

# -------------------------
# 6. Moving Average
# -------------------------
st.header(f"{default_coin.title()} Moving Average ({ma_window}-Day) 🟢")
months_ma = st.number_input(
    f"Months for Moving Average ({default_coin.title()})",
    min_value=1, max_value=60, value=12, key="ma_months"
)
window_ma = st.slider("Moving Average Window (days)", 2, 30, 7)
with st.spinner("Calculating moving average..."):
    fig_ma = moving_average_plot(default_coin, months_ma, window_ma)
st.plotly_chart(fig_ma, use_container_width=True)

# -------------------------
# 7. Regression Analysis
# -------------------------
st.header("Next-Day Return Prediction (Regression Analysis) 📈")
months_reg = st.number_input(
    "Months for Regression Analysis",
    min_value=1, max_value=60, value=12, key="reg_months"
)
with st.spinner("Computing regression predictions..."):
    df_pred = regression_profit_prediction(coins, months_reg)
st.dataframe(df_pred)

# -------------------------
# 8. Market Cap / Category Pie
# -------------------------
st.header("Crypto Market Cap Distribution 🥧")
months_cat = st.number_input(
    "Months for Market Cap Analysis (ignored, default 12)", 
    min_value=1, max_value=60, value=12, key="cat_months"
)
with st.spinner("Loading market cap pie chart..."):
    fig_cat = crypto_category_pie(coins)
st.plotly_chart(fig_cat, use_container_width=True)