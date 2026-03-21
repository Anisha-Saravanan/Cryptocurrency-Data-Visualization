import streamlit as st
from normalized_plot import show_normalized
from duration_plot import show_duration

st.title("Crypto Dashboard 📊")

coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']

# Select visualization
option = st.radio(
    "Choose Visualization",
    ["Normalized Plot", "Duration Plot"]
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