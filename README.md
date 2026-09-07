# Cryptocurrency Data Visualization

A modular Python-based cryptocurrency analytics platform that retrieves live and historical market data using the **CoinGecko REST API**. The project performs technical analysis, volatility and correlation analysis, and regression-based cryptocurrency return prediction through an interactive **Streamlit and Plotly** dashboard.

## Features

* 📊 Cryptocurrency market data retrieval using CoinGecko API
* 📈 Technical indicators: **Moving Average, Bollinger Bands, RSI**
* 📉 Volatility and return analysis
* 🔗 Multi-asset correlation analysis with heatmaps
* 🤖 Linear Regression for next-period return prediction
* 🕯️ Interactive candlestick and volume visualizations
* 🖥️ Interactive Streamlit dashboard

## Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Plotly, Matplotlib**
* **Streamlit**
* **CoinGecko API / PyCoinGecko**

## Project Structure

```text
Cryptocurrency-Data-Visualization/
├── api_client.py
├── data_fetcher.py
├── moving_average.py
├── bollinger_bands.py
├── rsi.py
├── correlation_analysis.py
├── regression_analysis.py
├── candlestick_chart.py
├── volume_analysis.py
├── live_crypto.py
├── app.py
```


```bash
streamlit run app.py
```


