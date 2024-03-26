import os
import pandas as pd
import datetime as dt
import yfinance as yf
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv


def fetch_stock_data(tickers, alpaca_api_key, api_secret_key, base_url):
    # Create the Alpaca API object
    api = tradeapi.REST(alpaca_api_key, api_secret_key, base_url, api_version="v2")

    # Specify the start and end dates directly
    start_date = pd.Timestamp("2019-03-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2024-03-01", tz="America/New_York").isoformat()

    # Set timeframe to "1Day" for Alpaca API
    timeframe = "1Hour"

    # Get closing prices for the tickers for the specified timeframe and dates
    dataframe = api.get_bars(tickers, timeframe, start=start_date, end=end_date).df

    # Reorganize the DataFrame
    stock_data = dataframe[['symbol', 'open', 'high', 'low', 'close', 'volume']]

    return stock_data


# Function for sellecting top dollar volume (liquidity) stocks
def get_top_tickers(sp500_url):
    
    # Select tickers
    sp500 = pd.read_html(sp500_url)[0]
    sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-')

    # Get unique ticker symbols
    tickers = sp500['Symbol'].unique().tolist()

    # Fetch stock data from Yahoo Finance
    end_date = pd.Timestamp.now().date()
    start_date = end_date - pd.DateOffset(days=2268)
    stock_data = yf.download(tickers=tickers, start=start_date, end=end_date)

    # Drop stocks with less than 1 trading year
    stock_data = stock_data.dropna(thresh=252, axis=0)

    # Calculate dollar volume
    dollar_volume = stock_data['Adj Close'] * stock_data['Volume'] / 1e6

    # Resample the dollar volume
    monthly_dollar_volume = dollar_volume.resample('M').mean()

    # Compute percentile rank
    monthly_dollar_vol_rank = monthly_dollar_volume.rank(pct=True)

    # Convert DataFrame to Series using stack
    stacked_data = monthly_dollar_vol_rank.stack()

    # Sort stacked data by value in descending order
    sorted_stacked_data = stacked_data.sort_values(ascending=False)

    # Select the top 5 values
    top_values = sorted_stacked_data.head(5)

    # Extract the index of the top 5 values
    top_tickers = top_values.index.tolist()

    return top_tickers
