<<<<<<< HEAD
import os

=======
<<<<<<< HEAD
# This file contains seperate functions for building and trainig machine learning  models 
=======
>>>>>>> fd229b5b6a879d0c05fb09c7439d0907641da447
def fetch_stock_data(start_date, end_date, tickers, timeframe = '1Day'):
    # Grabbing all necessary alpaca information
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
        ticker_df = ticker_df['close']
        dfs[ticker] = ticker_df
    new_df = pd.concat(dfs.values(), axis = 1, keys = tickers)
    # Resetting index to have only date information
    new_df.reset_index(inplace = True)
    new_df.timestamp = new_df.timestamp.dt.date
    new_df.set_index('timestamp', inplace = True)
    new_df.index = pd.to_datetime(new_df.index)
    return new_df
>>>>>>> 6662a79b93bb22baeecb4d2c7fef3bd48454c090
