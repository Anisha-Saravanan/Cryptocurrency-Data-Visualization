# histogram_analysis.py
import pandas as pd
import plotly.express as px
from data_fetcher import fetch_multiple_coins

def returns_histogram(coins: list, months: int):
    days = months * 30
    coin_data = fetch_multiple_coins(coins, days)
    
    df = pd.DataFrame()
    for coin, prices in coin_data.items():
        temp = pd.DataFrame(prices, columns=['timestamp', coin])
        temp['timestamp'] = pd.to_datetime(temp['timestamp'], unit='ms')
        temp = temp.set_index('timestamp').resample('D').mean()
        df[coin] = temp[coin].pct_change()  # daily returns
    
    df = df.dropna().melt(var_name='Coin', value_name='Daily Return')
    
    fig = px.histogram(
        df,
        x='Daily Return',
        color='Coin',
        barmode='overlay',
        marginal='box',
        nbins=50,
        title=f"Histogram of Daily Returns ({months} months)"
    )
    return fig