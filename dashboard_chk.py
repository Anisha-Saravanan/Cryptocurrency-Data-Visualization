import streamlit as st
from streamlit_autorefresh import st_autorefresh

from normalized_plot import show_normalized
from duration_plot import show_duration
from live_crypto import get_today_coin_plot
from correlation_analysis import correlation_heatmap
from histogram_analysis import returns_histogram
from moving_average import moving_average_plot
from regression_analysis import regression_profit_prediction
from rsi import rsi_plot
from bollinger_bands import bollinger_plot
from volume_analysis import volume_plot
from candlestick_chart import candlestick_plot

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
# 11. Candlestick Chart
# -------------------------
st.header("Candlestick Chart 🕯️")

coin_candle = st.selectbox(
    "Select Coin for Candlestick",
    coins,
    index=0,
    key="coin_candle"
)

months_candle = st.number_input(
    f"Months for Candlestick ({coin_candle})",
    min_value=1, max_value=60, value=12,
    key="candle_months_input"
)

with st.spinner("Generating Candlestick Chart..."):
    fig_candle = candlestick_plot(coin_candle, months_candle)

st.plotly_chart(fig_candle, use_container_width=True)

# -------------------------
# 5. Returns Histogram
# -------------------------
st.header("Histogram of Daily Returns 📊")

months_hist = st.number_input(
    "Months for Histogram",
    min_value=1, max_value=60, value=12, key="hist_months_input"
)

with st.spinner("Computing histogram..."):
    fig_hist, fig_scatter, stats_df = returns_histogram(coins, months_hist)

st.plotly_chart(fig_hist, use_container_width=True)
st.plotly_chart(fig_scatter, use_container_width=True)
st.dataframe(stats_df)


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
    df, fig1, fig2, fig3 = regression_profit_prediction(coins, months_reg)

st.dataframe(df)
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)

# -------------------------
# 8. RSI Analysis
# -------------------------
st.header("RSI Indicator 📉")

coin_rsi = st.selectbox("Select Coin for RSI", coins, index=0, key="coin_rsi")

months_rsi = st.number_input(
    f"Months for RSI ({coin_rsi})",
    min_value=1, max_value=60, value=12, key="rsi_months_input"
)

with st.spinner("Calculating RSI..."):
    fig_rsi = rsi_plot(coin_rsi, months_rsi)

st.plotly_chart(fig_rsi, use_container_width=True)

# -------------------------
# 9. Bollinger Bands
# -------------------------
st.header("Bollinger Bands 🔥")

coin_bb = st.selectbox("Select Coin for Bollinger Bands", coins, index=0, key="coin_bb")

months_bb = st.number_input(
    f"Months for Bollinger Bands ({coin_bb})",
    min_value=1, max_value=60, value=12, key="bb_months_input"
)

window_bb = st.slider(
    "Bollinger Window (days)", 5, 50, 20, key="bb_window"
)

with st.spinner("Calculating Bollinger Bands..."):
    fig_bb = bollinger_plot(coin_bb, months_bb, window_bb)

st.plotly_chart(fig_bb, use_container_width=True)

# -------------------------
# 10. Volume Analysis
# -------------------------
st.header("Volume Analysis 📊")

coin_vol = st.selectbox("Select Coin for Volume", coins, index=0, key="coin_vol")

months_vol = st.number_input(
    f"Months for Volume ({coin_vol})",
    min_value=1, max_value=60, value=12, key="vol_months_input"
)

with st.spinner("Loading Volume Data..."):
    fig_vol = volume_plot(coin_vol, months_vol)

st.plotly_chart(fig_vol, use_container_width=True)


