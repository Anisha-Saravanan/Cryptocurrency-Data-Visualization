import ccxt
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
    time.sleep(2)