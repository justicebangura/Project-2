import os
import pandas as pd
import datetime as dt
import yfinance as yf
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv
from sklearn.cluster import KMeans


# Function for fetching stock_data in Alpaca
def fetch_stock_data(start_date, end_date, tickers, timeframe='1Day'):
    
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
    api = REST(alpaca_api_key, alpaca_secret_key, base_url='https://paper-api.alpaca.markets')
    
    # Set start and end dates
    start_date_iso = pd.Timestamp(start_date, tz='America/New_York').isoformat()
    end_date_iso = pd.Timestamp(end_date, tz='America/New_York').isoformat()
    
    # pull data from Api
    df_ticker = api.get_bars(tickers, TimeFrame.Day, start=start_date_iso, end=end_date_iso).df
    dfs = {}
    
    for ticker in tickers:
        ticker_df = df_ticker.loc[df_ticker.symbol == ticker].drop('symbol', axis=1)
        ticker_df = ticker_df[['open', 'close', 'high', 'volume']]
        dfs[ticker] = ticker_df
        
    data = pd.concat(dfs.values(), axis=1, keys=tickers)
    data.reset_index(inplace=True)
    data.timestamp = data.timestamp.dt.date
    data.set_index('timestamp', inplace=True)
    data.index = pd.to_datetime(data.index)
    
    return data

# Function for sellecting top 5 stocks from highest performing cluster
def get_clusters_from_sp500(sp500_url, split_factor=1, dividend=0):
    
    # Select tickers
    sp500 = pd.read_html(sp500_url)[0]
    sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-')
    tickers = sp500['Symbol'].unique().tolist()

    # Fetch stock data
    end_date = '2024-03-14'  # Adjust end date if needed
    start_date = pd.to_datetime(end_date) - pd.DateOffset(365*8)
    stock_data = yf.download(tickers=tickers, start=start_date, end=end_date)

    # Compute clusters
    closing_price = stock_data['Close']
    adjusted_close = closing_price / split_factor - dividend
    dollar_volume = adjusted_close * stock_data['Volume'] / 1e6
    
    monthly_data = pd.concat([dollar_volume.resample('M').mean(),
                          stock_data.resample('M').last().drop(columns=['Open', 'High', 'Low', 'Close'])],
                         axis=1).dropna()
    monthly_data['dollar_vol_rank'] = monthly_data['Volume'].rolling(window=5*12, min_periods=12).mean().rank(ascending=False)
    filtered_data = monthly_data[monthly_data['dollar_vol_rank'] <= 150]
    
    
    # Clustering using Kmeans 
    kmeans = KMeans(n_clusters=4, random_state=0)
    clusters = kmeans.fit_predict(filtered_data)
    filtered_data['cluster'] = clusters
    highest_rank_cluster = filtered_data.groupby('cluster')['dollar_vol_rank'].mean().idxmin()
    cluster_data = filtered_data[filtered_data['cluster'] == highest_rank_cluster]
    top_5 = cluster_data.nlargest(5, 'Volume')
    top_tickers = top_5.index.get_level_values('ticker').tolist()

    return top_tickers

