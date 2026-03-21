# regression_analysis.py
import pandas as pd
from data_fetcher import fetch_multiple_coins
from sklearn.linear_model import LinearRegression
import numpy as np

def regression_profit_prediction(coins: list, months: int):
    days = months * 30
    coin_data = fetch_multiple_coins(coins, days)
    
    returns = {}
    for coin, prices in coin_data.items():
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('timestamp').resample('D').mean()
        df['return'] = df['price'].pct_change()
        df = df.dropna()
        returns[coin] = df['return']
    
    df_returns = pd.DataFrame(returns).dropna()
    
    # Use linear regression: predict last day return using other coins
    X = df_returns.iloc[:-1]
    y = df_returns.shift(-1).iloc[:-1]
    
    predictions = {}
    for coin in coins:
        model = LinearRegression()
        model.fit(X.drop(columns=coin), y[coin])
        pred = model.predict(X.drop(columns=coin).iloc[-1:])[0]
        predictions[coin] = pred
    
    # Convert predictions to DataFrame
    df_pred = pd.DataFrame(list(predictions.items()), columns=['Coin', 'Predicted Return'])
    df_pred = df_pred.sort_values('Predicted Return', ascending=False)
    return df_pred