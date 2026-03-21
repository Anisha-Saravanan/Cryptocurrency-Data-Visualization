import ccxt
import plotly.graph_objects as go
import datetime
import time

exchange = ccxt.binance()

symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'ADA/USDT', 'SOL/USDT']

fig = go.Figure()

price_data = {symbol: [] for symbol in symbols}
time_data = []

print("Running live crypto tracker... Press Ctrl+C to stop")

while True:
    current_time = datetime.datetime.now()
    time_data.append(current_time)

    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        price_data[symbol].append(price)

    fig = go.Figure()

    for symbol in symbols:
        fig.add_trace(go.Scatter(
            x=time_data,
            y=price_data[symbol],
            mode='lines',
            name=symbol
        ))

    fig.update_layout(
        title="Live Crypto Prices (Today)",
        xaxis_title="Time",
        yaxis_title="Price (USDT)",
    )

    fig.show()

    time.sleep(5)  # update every 5 seconds