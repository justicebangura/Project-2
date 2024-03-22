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

    #lets write logic for strategy
    return "Signal-Buy or sell"


# check correlation of strategies the returns should be uncorelated to reduce overall portfolio risk - diversification