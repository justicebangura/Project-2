# This python file contains feauture calculations 

import pandas_ta as ta
import pandas as pd



def calculate_pct_change(stock_df):
    stock_df['Daily Returns'] = stock_df['close'].pct_change()
    return stock_df

def cumulative_returns(stock_df):
    stock_df['Cumulative Returns'] = (1 + stock_df['Daily Returns']).cumprod()
    return stock_df

def daily_returns_lagged(stock_df):
    stock_df['Daily Returns Lagged'] = stock_df['Daily Returns'].shift(-1)
    return stock_df

def sma_ema_long_short(stock_df):
    short_window = 5
    long_window = 100
    
    stock_df['SMA Fast'] = stock_df['close'].rolling(window=short_window).mean()
    stock_df['SMA Slow'] = stock_df['close'].rolling(window=long_window).mean()
    stock_df["EMA Fast"] = stock_df["close"].ewm(span=short_window).mean()
    stock_df["EMA Fast"] = stock_df["close"].ewm(span=long_window).mean()
    
    return stock_df

# Calculating Don Chaian 
def don_chaian(stock_df):
    stock_df[['DCL', 'DCM', 'DCU']] = stock_df.ta.donchian(lower_length = 40, upper_length = 50)
    
    return stock_df

# Simple Moving Average (SMA)
def simple_moving_averge(stock_df):
    stock_df['SMA'] = stock_df['close'].rolling(window=20).mean()
    
    return stock_df

# Standard Deviation (SD)
def standard_deviation(stock_df):
    stock_df['STD'] = stock_df['close'].rolling(window=20).std()
    
    return stock_df

# Upper Bollinger Band (UB) and Lower Bollinger Band (LB)
def calculate_bollinger_bands(stock_df):
    
    # Compute Bollinger Bands
    stock_df['Upper Bollinger Band'] = stock_df['SMA'] + 2 * stock_df['STD']
    stock_df['Lower Bollinger Band'] = stock_df['SMA'] - 2 * stock_df['STD']
    
    return stock_df


def weighted_moving_average(stock_df):
    
    period = 5
    
    # Calculate the exponentially weighted moving average
    wma_values = stock_df['close'].ewm(alpha=1.0 / period, adjust=False).mean()
    
    # Assign the calculated WMA values to the DataFrame directly
    stock_df['WMA'] = wma_values
    
    return stock_df

def atr(stock_df, n=14):
    
    high = stock_df['high']
    low = stock_df['low']
    close = stock_df['close']
    
    # Calculate True Range
    tr = pd.DataFrame()
    tr['tr0'] = high - low
    tr['tr1'] = (high - close.shift()).abs()
    tr['tr2'] = (low - close.shift()).abs()
    tr = tr.max(axis=1)
    
    # Calculate ATR using exponential moving average
    stock_df['ATR'] = tr.ewm(span=n, adjust=False).mean()
    
    return stock_df

# Comnodity Channel Index
def commodity_channel_index(stock_df):
    p = 20
    ma = (stock_df['close'])/p
    mean_dev = (stock_df['close']-ma) / p
    price = (stock_df['high'] + stock_df['low'] + stock_df['close'])/3

    stock_df['CCI'] = (price - ma)/(0.015*mean_dev)*price
    
    return stock_df

def df_to_windowed_df(stock_df, first_date_str, last_date_str, n=3):
    first_date = pd.to_datetime(first_date_str)
    last_date = pd.to_datetime(last_date_str)
    target_date = first_date
    dates = []
    X, Y = [], []
    last_time = False
    while True:
        df_subset = stock_df.loc[:target_date].tail(n + 1)
        if len(df_subset) != n + 1:
            print(f'Error: Window of size {n} is too large for date {target_date}')
            return
        values = df_subset['close'].to_numpy()  # Adjusted to access close price
        x, y = values[:-1], values[-1]
        dates.append(target_date)
        X.append(x)
        Y.append(y)
        next_week = stock_df.loc[target_date:target_date + pd.Timedelta(days=7)]
        next_datetime_str = str(next_week.head(2).tail(1).index.values[0])
        next_date_str = next_datetime_str.split('T')[0]
        year_month_day = next_date_str.split('-')
        year, month, day = map(int, year_month_day)
        next_date = datetime.datetime(day=day, month=month, year=year)
        if last_time:
            break
        target_date = next_date
        if target_date == last_date:
            last_time = True
    X = np.array(X)
    for i in range(0, n):
        stock_df[f'Target-{n - i}'] = X[:, i]
    stock_df['Target'] = Y
    stock_df['Target Date'] = dates
    return stock_df





