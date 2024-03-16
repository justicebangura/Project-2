import os
import pandas as pd
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv


# Function for fetching  stock data via Alpaca API
def fetch_stock_data(start_date, end_date, tickers, timeframe = '1Day'):
    # Grabbing all necessary Alpaca information
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
    api = REST(alpaca_api_key, alpaca_secret_key, base_url = 'https://paper-api.alpaca.markets')
    start_date_iso = pd.Timestamp(start_date, tz = 'America/New_York').isoformat()
    end_date_iso = pd.Timestamp(end_date, tz = 'America/New_York').isoformat()
    # Creating dataframe
    df_ticker = api.get_bars(tickers, TimeFrame.Day, start = start_date_iso, end = end_date_iso).df
    # Selecting only close price data for each stock, and concatenating them into one dataframe
    dfs = {}
    for ticker in tickers:
        ticker_df = df_ticker.loc[df_ticker.symbol == ticker].drop('symbol', axis = 1)
        ticker_df = ticker_df[['open','close','high','volume']]
        dfs[ticker] = ticker_df
    stock_data = pd.concat(dfs.values(), axis = 1, keys = tickers)
    # Resetting index to have only date information
    stock_data.reset_index(inplace = True)
    stock_data.timestamp = stock_data.timestamp.dt.date
    stock_data.set_index('timestamp', inplace = True)
    stock_data.index = pd.to_datetime(stock_data.index)
    return stock_data