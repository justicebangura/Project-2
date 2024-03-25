# This python file contains feautures to be added to the Dataframe 

import pandas_ta as ta
import pandas as pd
import numpy as np
from finta import TA

# calculate percentage change
def calculate_pct_change(stock_df):
    stock_df['Daily Returns'] = stock_df['close'].pct_change()
    return stock_df

# stock cumulative returns
def cumulative_returns(stock_df):
    stock_df['Cumulative Returns'] = (1 + stock_df['Daily Returns']).cumprod()
    return stock_df

# Slow and fast moving averages
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

# finta strategy
def finta_technical_indicators(stock_df):

    # Set the short window and long windows
    short_window = 15
    long_window = 50

    # Add the SMA technical indicators for the short and long windows
    stock_df["TA Short"] = TA.SMA(stock_df, short_window)
    stock_df["TA Long"] = TA.SMA(stock_df, long_window)
    
    return stock_df

# This section is for plotting strategy returns 
def calculate_strategy_returns(stock_df):
    
    stock_df['Majority Vote Returns'] = stock_df['Daily Returns'] * stock_df['Signal'].shift()
    
    return stock_df

# calculate simple momentum returns
def calculate_simple_momentum_returns(stock_df):
    
    stock_df['Simple Momentum Returns'] = stock_df['Daily Returns'] * stock_df['Signal_SM'].shift()
    
    return stock_df

# calculate dmac returns
def calculate_dmac_returns(stock_df):
    
    stock_df['DMAC Returns'] = stock_df['Daily Returns'] * stock_df['Signal_DMAC'].shift()
    
    return stock_df

# calculate finta returns
def calculate_finta_returns(stock_df):
    
    stock_df['Finta Returns'] = stock_df['Daily Returns'] * stock_df['Signal_FINTA'].shift()
    
    return stock_df

# calculate bollinger bands returns
def calculate_bollinger_bands_returns(stock_df):
    
    stock_df['Bollinger Bands Returns'] = stock_df['Daily Returns'] * stock_df['Signal_BB'].shift()
    
    return stock_df

# calculate pairs trading returns
def calculate_pairs_trading_returns(stock_df):
    
    stock_df['Pairs_Trading_Returns'] = stock_df['Daily Returns'] * stock_df['Signal_PTS'].shift()
    
    return stock_df