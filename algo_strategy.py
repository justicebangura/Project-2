# Imports
import datetime
import pandas as pd
 


def simple_momentum(Stock_data):
    
    # Filter the date index and close columns
    signals_df = stock_df.loc[:, ["average"]]

    # Calculate percentage change in implied volatility 
    # (Implied Volatility is a proxy for option price returns) 
    signals_df["Actual Returns"] = ( signals_df["average"].pct_change())
    signals_df["Actual Returns"].head()
    
    # Initialize the new Signal column
    signals_df["Signal"] = 0.0

   # When Actual Returns are greater than or equal to 0, generate signal to buy stock option long
    signals_df.loc[(signals_df["Actual Returns"] >= 0), "Signal"] = 1

   # When Actual Returns are less than 0, generate signal to sell stock option short
    signals_df.loc[(signals_df["Actual Returns"] < 0), "Signal"] = -1
    
    return simple_momentum_df


def dmac_strategy(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"


def finta_strategy(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"


# check correlation of strategies the returns should be uncorelated to reduce overall portfolio risk - diversification