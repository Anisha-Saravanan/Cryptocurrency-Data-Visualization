import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import time

# Connect to Binance
exchange = ccxt.binance()

symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']

# Empty DataFrame
df = pd.DataFrame()

# Store base prices for normalization
base_price = {}

plt.ion()  # interactive mode

while True:
    row = {}

    # Fetch live prices
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        row[symbol] = price

        # Save first value as base
        if symbol not in base_price:
            base_price[symbol] = price

    # Add timestamp
    row['time'] = pd.Timestamp.now()

    # Append new row
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

    # Keep last 50 points (for smooth graph)
    df = df.tail(50)

    # Clear plot
    plt.clf()

    # Plot each coin (normalized % change)
    for symbol in symbols:
        normalized = ((df[symbol] - base_price[symbol]) / base_price[symbol]) * 100
        plt.plot(df['time'], normalized, label=symbol)

    # Styling (like your image)
    plt.title("Live Crypto Performance (%)")
    plt.xlabel("Time")
    plt.ylabel("Percentage Change (%)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.pause(0.5)

    # Wait before next update
    time.sleep(1)