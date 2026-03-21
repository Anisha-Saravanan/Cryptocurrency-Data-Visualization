from pycoingecko import CoinGeckoAPI
import streamlit as st
import plotly.graph_objects as go
import datetime

cg = CoinGeckoAPI()
@st.cache_data(ttl=300)
def get_coin_data(coin, days):
    cg = CoinGeckoAPI()
    return cg.get_coin_market_chart_by_id(
        id=coin,
        vs_currency='usd',
        days=days
    )
def get_today_coin_plot(coin):
    data = get_coin_data(coin,1)

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
        title=f"{coin.upper()} Price Today (12 AM → Now)",
        xaxis_title="Time",
        yaxis_title="Price (USD)",
        hovermode="x unified"
    )

    return fig