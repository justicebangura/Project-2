# This python file contains feautures calculations 

import pandas_ta as ta
import pandas as pd
import numpy as np
from finta import TA


def calculate_pct_change(stock_df):
    stock_df['Daily Returns'] = stock_df['close'].pct_change()
    return stock_df

def cumulative_returns(stock_df):
    stock_df['Cumulative Returns'] = (1 + stock_df['Daily Returns']).cumprod()
    return stock_df

def sma_ema_long_short(stock_df):
    short_window = 50
    long_window = 100
    
    stock_df['SMA50'] = stock_df['close'].rolling(window=short_window).mean()
    stock_df['SMA100'] = stock_df['close'].rolling(window=long_window).mean()
    
    return stock_df

# Simple Moving Average (SMA)
def simple_moving_averge(stock_df):
    stock_df['SMA20'] = stock_df['close'].rolling(window=20).mean()
    
    return stock_df

# Standard Deviation (SD)
def standard_deviation(stock_df):
    stock_df['STD'] = stock_df['close'].rolling(window=20).std()
    
    return stock_df

# Upper Bollinger Band (UB) and Lower Bollinger Band (LB)
def calculate_bollinger_bands(stock_df):
    
    # Compute Bollinger Bands
    stock_df['Upper Band'] = stock_df['SMA20'] + 2 * stock_df['STD']
    stock_df['Lower Band'] = stock_df['SMA20'] - 2 * stock_df['STD']
    
    return stock_df

def finta_technical_indicators(stock_df):

    # Set the short window and long windows
    short_window = 15
    long_window = 50

    # Add the SMA technical indicators for the short and long windows
    stock_df["TA Short"] = TA.SMA(stock_df, short_window)
    stock_df["TA Long"] = TA.SMA(stock_df, long_window)
    
    return stock_df