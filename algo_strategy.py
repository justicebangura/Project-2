# Imports
import datetime
import pandas as pd
from finta import TA
import numpy as np
 

def simple_momentum(stock_df):
    # Initialize the new Signal column
    stock_df["Signal_SM"] = 0.0

<<<<<<< HEAD
    # When Actual Returns are greater than or equal to 0, generate signal to buy stock option long
    stock_df.loc[stock_df["Daily Returns"] >= 0, "Signal_SM"] = 1

    # When Actual Returns are less than 0, generate signal to sell stock option short
    stock_df.loc[stock_df["Daily Returns"] < 0, "Signal_SM"] = -1
    
    return stock_df


def dmac_strategy(stock_df):

    stock_df["Signal_DMAC"] = 0.0
    
    short_window = 50
    long_window = 100
    
    # Generate the trading signal 0 or 1,
    # where 1 is the short-window (SMA50) greater than the long-window (SMA100)
    # and 0 is when the condition is not met
    
    stock_df["Signal_DMAC"][short_window:] = np.where(
        stock_df["SMA50"][short_window:] > stock_df["SMA100"][short_window:], 1.0, 0.0)
    return stock_df



def finta_strategy(stock_df):
    # Initialize the 'Signal_FINTA' column with zeros
    stock_df["Signal_FINTA"] = 0.0
    
    short_window = 50
    long_window = 100

    # Generate trading signals: 1 for buy, 0 for hold
    stock_df["Signal_FINTA"][short_window:] = np.where(
        stock_df["TA Short"][short_window:] > stock_df["TA Long"][short_window:], 1.0, 0.0)

    return stock_df

def bollinger_bands_strategy(stock_df):

    stock_df['Signal_BB'] = 0.0

    # Generate buy signals
    buy_conditions = (stock_df['close'] < stock_df['Lower Band']) & (stock_df['close'].shift(1) >= stock_df['Lower Band'].shift(-1))
    stock_df.loc[buy_conditions, 'Signal_BB'] = 1

    # Generate sell signals
    sell_conditions = (stock_df['close'] > stock_df['Upper Band']) & (stock_df['close'].shift(1) <= stock_df['Upper Band'].shift(-1))
    stock_df.loc[sell_conditions, 'Signal_BB'] = -1

    return stock_df

def pairs_trading_signals(stock_df, entry_threshold=1.0, exit_threshold=0.5):
    # Calculate the spread between two assets (e.g., close prices)
    stock_df['Spread'] = stock_df['close'] - stock_df['open']
    
    # Initialize signals
    signals = []

    # Implement the pairs trading strategy
    for spread in stock_df['Spread']:
        if spread > entry_threshold:  # If spread is above entry threshold
            signals.append(1)  # Buy signal
        elif spread < -entry_threshold:  # If spread is below negative entry threshold
            signals.append(-1)  # Sell signal
        else:
            signals.append(0)  # Hold signal
            
    # Assign signals to DataFrame
    stock_df['Signal_PTS'] = signals

    return stock_df



=======
    #lets write logic for strategy
    return "Signal-Buy or sell"
>>>>>>> be8f67c829c2032a256d05ad09520c68e0a4e23c


# check correlation of strategies the returns should be uncorelated to reduce overall portfolio risk - diversification