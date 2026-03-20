'''import ccxt
import matplotlib.pyplot as plt
from collections import deque
import time

exchange = ccxt.binance()

symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']

data = {symbol: deque(maxlen=50) for symbol in symbols}
base_price = {}

plt.ion()

while True:
    plt.clf()
    
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        
        # Store first value as base
        if symbol not in base_price:
            base_price[symbol] = price
        
        # Normalize (start from 1)
        normalized_price = price / base_price[symbol]
        
        data[symbol].append(normalized_price)
        
        plt.plot(list(data[symbol]), label=symbol)
    
    plt.title("Live Crypto Comparison (Normalized)")
    plt.xlabel("Time")
    plt.ylabel("Relative Change (Base = 1)")
    plt.legend()
    
    plt.pause(0.5)
    time.sleep(2)'''

'''import ccxt
import plotly.graph_objects as go
import time

exchange = ccxt.binance()

symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']

base_price = {}
data = {symbol: [] for symbol in symbols}

fig = go.Figure()

while True:
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        
        if symbol not in base_price:
            base_price[symbol] = price
        
        normalized = ((price - base_price[symbol]) / base_price[symbol]) * 100
        data[symbol].append(normalized)
    
    fig = go.Figure()
    
    for symbol in symbols:
        fig.add_trace(go.Scatter(
            y=data[symbol],
            mode='lines',
            name=symbol
        ))
    
    fig.update_layout(
        title="Live Crypto Performance (%)",
        xaxis_title="Time",
        yaxis_title="Percentage Change",
        template="plotly_dark"   # 🔥 makes it look professional
    )
    
    fig.show()
    time.sleep(5)'''

'''import ccxt
import matplotlib.pyplot as plt
from collections import deque
import time

exchange = ccxt.binance()

symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']

data = {symbol: deque(maxlen=100) for symbol in symbols}

plt.ion()

while True:
    plt.clf()
    
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        
        data[symbol].append(price)
        
        plt.plot(list(data[symbol]), label=symbol)
    
    plt.title("Live Crypto Prices")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    print("hi")
    plt.pause(0.5)
    time.sleep(2)'''

import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import time

exchange = ccxt.binance()

symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']

# Create DataFrame
df = pd.DataFrame()

plt.ion()

while True:
    row = {}

    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        row[symbol] = ticker['last']
    
    # Add timestamp
    row['time'] = pd.Timestamp.now()
    
    df = pd.concat([df, pd.DataFrame([row])])
    
    # Keep last 100 points
    df = df.tail(100)

    plt.clf()

    for symbol in symbols:
        plt.plot(df['time'], df[symbol], label=symbol)

    plt.title("Crypto Prices - Live")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.pause(0.5)

    time.sleep(2)
