import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from api_client import cg

@st.cache_data(ttl=3600, show_spinner=False)
def fetch_coin_prices(coin: str, days: int) -> list:
    """Fetch price data for a single coin. Cached independently."""
    data = cg.get_coin_market_chart_by_id(id=coin, vs_currency='usd', days=days)
    return data['prices']

def fetch_multiple_coins(coins: list, days: int) -> dict:
    """Fetch multiple coins in parallel."""
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(lambda c: (c, fetch_coin_prices(c, days)), coins)
    return dict(results)
