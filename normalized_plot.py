import streamlit as st
from pycoingecko import CoinGeckoAPI
import plotly.graph_objects as go
import datetime
@st.cache_data(ttl=3600)  
def show_normalized(coins, days):
    cg = CoinGeckoAPI()
    fig = go.Figure()

    for coin in coins:
        data = cg.get_coin_market_chart_by_id(
            id=coin,
            vs_currency='usd',
            days=days
        )

        prices = data['prices']

        dates = [datetime.datetime.fromtimestamp(p[0]/1000) for p in prices]
        values = [p[1] for p in prices]

        normalized = [(v / values[0]) * 100 for v in values]

        fig.add_trace(go.Scatter(
            x=dates,
            y=normalized,
            mode='lines',
            name=coin
        ))

    fig.update_layout(
        title="Normalized Crypto Trends",
        xaxis_title="Date",
        yaxis_title="Growth (Base = 100)"
    )

    return fig