import streamlit as st
from pycoingecko import CoinGeckoAPI
import plotly.graph_objects as go
import datetime
@st.cache_data(ttl=3600)
def show_duration(coin, months):
    cg = CoinGeckoAPI()

    # Convert months → days
    days = months * 30

    data = cg.get_coin_market_chart_by_id(
        id=coin,
        vs_currency='usd',
        days=days
    )

    prices = data['prices']

    dates = [datetime.datetime.fromtimestamp(p[0]/1000) for p in prices]
    values = [p[1] for p in prices]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=values,
        mode='lines',
        name=coin
    ))

    fig.update_layout(
        title=f"{coin} Price for Last {months} Months",
        xaxis_title="Date",
        yaxis_title="Price (USD)"
    )

    return fig