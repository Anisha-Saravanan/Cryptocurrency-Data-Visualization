import streamlit as st
from live_crypto import get_today_coin_plot
import time
from streamlit_autorefresh import st_autorefresh
from normalized_plot import show_normalized
from duration_plot import show_duration
st.title("Crypto Dashboard 📊")

coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']

# Select visualization
option = st.radio(
    "Choose Visualization",
    ["Normalized Plot", "Duration Plot","Live Line Plot"]
)

# -------------------------
# NORMALIZED
# -------------------------
if option == "Normalized Plot":

    months = st.number_input(
        "Enter number of months",
        min_value=1,
        max_value=60,
        value=6,
        key="norm_months"
    )

    days = months * 30

    with st.spinner("Loading normalized plot..."):
        fig = show_normalized(coins, days)
        st.plotly_chart(fig, use_container_width=True)


# -------------------------
# DURATION PLOT
# -------------------------
elif option == "Duration Plot":

    coin = st.selectbox("Select Coin", coins)

    months = st.number_input(
        "Enter number of months",
        min_value=1,
        max_value=60,
        value=6,
        key="dur_months"
    )

    with st.spinner("Loading duration plot..."):
        fig = show_duration(coin, months)
        st.plotly_chart(fig, use_container_width=True)

elif option == "Live Line Plot":

    st.write("Showing today's data (12:00 AM → Now)")

    coin = st.selectbox("Select Coin", coins)

    placeholder = st.empty()

    import time

    run = st.checkbox("Start Live View")

    if run:
        st_autorefresh(interval=10000, key="live_refresh")  # 10 seconds

        fig = get_today_coin_plot(coin)

        placeholder.plotly_chart(
        fig,
        use_container_width=True
        )