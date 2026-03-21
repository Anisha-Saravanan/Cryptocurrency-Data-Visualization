# geographic_analysis.py
import pandas as pd
import plotly.express as px
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def crypto_category_pie(coins: list):
    coin_list = cg.get_coins_markets(vs_currency='usd', ids=coins)
    
    df = pd.DataFrame(coin_list)
    # Example: use 'market_cap_rank' as categories
    df['Category'] = pd.cut(df['market_cap_rank'], bins=[0,10,50,100,500,1000,10000],
                            labels=['Top10','Top50','Top100','Top500','Top1000','Others'])
    
    fig = px.pie(
        df,
        names='Category',
        values='market_cap',
        title='Crypto Distribution by Market Cap Category'
    )
    return fig