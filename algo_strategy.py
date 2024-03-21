# Imports

# check correlation of strategies the returns should be uncorelated to reduce overall portfolio risk - diversification

def strategy_one(Stock_data):
    #lets write logic for strategy
    return "Signal- Buy or sell"


def strategy_two(Stock_data):
    ## Read the aapl.csv file into a Pandas DataFrame
# Set the date column as the DateTimeIndex
a# Read the aapl.csv file into a Pandas DataFrame
# Set the date column as the DateTimeIndex
# Import the required libraries
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
NVDA_df = pd.read_csv(
    Path("../Resources/NVDA.csv"),
   
    parse_dates=True,
    infer_datetime_format=True
)
)
# Review the DataFrame
NVDA_df.head()
# Filter the date index and close columns
signals_df = NVDA_df.loc[:,["close"]]

# Review the DataFrame
signals_df.head()
short_window = 50
long_window = 100
# Generate the short and long window simple moving averages (50 and 100 days, respectively)
signals_df["SMA50"] = signals_df["Close"].rolling(window=short_window).mean()
signals_df["SMA100"] = signals_df["Close"].rolling(window=long_window).mean()

# Review the DataFrame
display(signals_df.head())
display(signals_df.tail())
# Create a column to hold the trading signal
signals_df["Signal"] = 0.0
# Generate the trading signal 0 or 1,
# where 1 is the short-window (SMA50) greater than the long-window (SMA100)
# and 0 is when the condition is not met
signals_df["Signal"][short_window:] = np.where(
    signals_df["SMA50"][short_window:] > signals_df["SMA100"][short_window:], 1.0, 0.0
)

# Review the DataFrame
signals_df.tail(10)
# Slice the DataFrame to confirm the Signal
signals_df.loc["2015-02-09":"2015-02-17"]
# Calculate the points in time when the Signal value changes
# Identify trade entry (1) and exit (-1) points
signals_df["Entry/Exit"] = signals_df["Signal"].diff()

# Review the DataFrame
signals_df.loc["2015-02-09":"2015-02-17"]
# Visualize exit position relative to close price
exit = signals_df[signals_df["Entry/Exit"] == -1.0]["close"].hvplot.scatter(
    color="yellow",
    marker="v",
    size=200,
    legend=False,
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
exit
# Visualize entry position relative to close price
entry = signals_df[signals_df["Entry/Exit"] == 1.0]["Close"].hvplot.scatter(
    color="purple",
    marker="^",
    size=200,
    legend=False,
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
entry
# Visualize close price for the investment
security_close = signals_df[["Close"]].hvplot(
    line_color="lightgray",
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
security_close
# Visualize moving averages
moving_avgs = signals_df[["SMA50", "SMA100"]].hvplot(
    ylabel="Price in $",
    width=1000,
    height=400)

# Show the plot
moving_avgs
# Create the overlay plot
entry_exit_plot = security_close * moving_avgs * entry * exit

# Show the plot
entry_exit_plot.opts(
    title="NVDA - SMA50, SMA100, Entry and Exit Points"
)
    return "Signal-Buy or sell"


def strategy_three(Stock_data)finta:
   # Import
import pandas as pd
import numpy as np
import hvplot.pandas
from pathlib import Path
# Import the finta Python library and the TA module
from finta import TA
# Read in CSV file in from the resources folder into a Pandas DataFrame
# Set the date as the DateTimeIndex
ixn_df = pd.read_csv(
    Path("../Resources/ixn_ohlcv.csv"),
    index_col = "date", 
    parse_dates = True, 
    infer_datetime_format = True
)

# Review the DataFrame
ixn_df.head()
# Plot the DataFrame with hvplot
ixn_df["close"].hvplot()
# Setting these options will allow for reviewing more of the DataFrames
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 1000)
# Create a signals_df DataFrame that is a copy of the ixn_df Dataframe
signals_df = ixn_df.copy()

# Set the short window and long windows
short_window = 15
long_window = 50

# Add the SMA technical indicators for the short and long windows
signals_df["Short"] = TA.SMA(signals_df, short_window)
signals_df["Long"] = TA.SMA(signals_df, long_window)

# # Replace the SMA moving average calculations with an alternative moving average 
# # calculation from the finta library
# signals_df["Short"] = TA.DEMA(signals_df, short_window)
# signals_df["Long"] = TA.DEMA(signals_df, long_window)

# Review the DataFrame
signals_df.iloc[95:105, :]
# Set the Signal column
signals_df["Signal"] = 0.0

# Generate the trading signal 1 or 0,
# where 1 is when the Short window is greater than (or crosses over) the Long Window
# where 0 is when the Short window is under the Long window
signals_df["Signal"][short_window:] = np.where(
    signals_df["Short"][short_window:] > signals_df["Long"][short_window:], 1.0, 0.0
)

# Calculate the points in time at which a position should be taken, 1 or -1
signals_df["Entry/Exit"] = signals_df["Signal"].diff()

# Review the DataFrame
signals_df.iloc[95:105, :]
 Visualize entry position relative to close price
entry = signals_df[signals_df["Entry/Exit"] == 1.0]["close"].hvplot.scatter(
    color='purple',
    marker='^',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize exit position relative to close price
exit = signals_df[signals_df["Entry/Exit"] == -1.0]["close"].hvplot.scatter(
    color='orange',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
    )
    # Visualize moving averages
moving_avgs = signals_df[["Short", "Long"]].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400
)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot
PART 2 ( create a new trading algo using the bollinger bands technical indictor from the finta library)
# Create a new clean copy of the signals_df DataFrame
bb_signals_df = ixn_df.copy()

# Review the DataFrame
bb_signals_df.head()
# Determine the Bollinger Bands for the Dataset
bbands_df = TA.BBANDS(bb_signals_df)

# Review the DataFrame
bbands_df.iloc[17:25, :]
# Concatenate the Bollinger Bands to the DataFrame
bb_signals_df = pd.concat([bb_signals_df, bbands_df], axis=1)

# Review the DataFrame
bb_signals_df.iloc[17:25, :]
 Visualize close price for the investment
security_close = bb_signals_df[["close"]].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400
)

bb_upper = bb_signals_df[["BB_UPPER"]].hvplot(
    line_color='purple',
    ylabel='Price in $',
    width=1000,
    height=400
)
bb_middle = bb_signals_df[["BB_MIDDLE"]].hvplot(
    line_color='orange',
    ylabel='Price in $',
    width=1000,
    height=400
)

bb_lower = bb_signals_df[["BB_LOWER"]].hvplot(
    line_color='blue',
    ylabel='Price in $',
    width=1000,
    height=400
)

# Overlay plots
bbands_plot = security_close * bb_upper * bb_middle * bb_lower
bbands_plot
# Create a trading algorithm using Bollinger Bands
# Set the Signal column
bb_signals_df["Signal"] = 0.0

# Generate the trading signals 1 (entry) or -1 (exit) for a long position trading algorithm
# where 1 is when the Close price is less than the BB_LOWER window
# where -1 is when the Close price is greater the the BB_UPPER window
for index, row in bb_signals_df.iterrows():
    if row["close"] < row["BB_LOWER"]:
        bb_signals_df.loc[index, "Signal"] = 1.0
    if row["close"] > row["BB_UPPER"]:
        bb_signals_df.loc[index,"Signal"] = -1.0

# Review the DataFrame
bb_signals_df
# Visualize entry position relative to close price
entry = bb_signals_df[bb_signals_df["Signal"] == 1.0]["close"].hvplot.scatter(
    color='green',
    marker='^',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize exit position relative to close price
exit = bb_signals_df[bb_signals_df["Signal"] == -1.0]["close"].hvplot.scatter(
    color='red',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)
# Visualize close price for the investment
security_close = bb_signals_df[["close"]].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400
)

bb_upper = bb_signals_df[["BB_UPPER"]].hvplot(
    line_color='purple',
    ylabel='Price in $',
    width=1000,
    height=400
)
bb_middle = bb_signals_df[["BB_MIDDLE"]].hvplot(
    line_color='orange',
    ylabel='Price in $',
    width=1000,
    height=400
)

bb_lower = bb_signals_df[["BB_LOWER"]].hvplot(
    line_color='blue',
    ylabel='Price in $',
    width=1000,
    height=400
)


# Overlay plots
bbands_plot = security_close * bb_upper * bb_middle * bb_lower * entry * exit
bbands_plot
 Update the trading algorithm using Bollinger Bands

# Set the Signal column
bb_signals_df["Signal"] = 0.0

# Create a value to hold the initial trade signal
trade_signal = 0

# Update the DataFrame Signal column 1 (entry) or -1 (exit) for a long position trading algorithm
# where 1 is when the Close price is less than the BB_LOWER window
# where -1 is when the Close price is greater the the BB_UPPER window
# Incorporate a conditional in the if-statement, to evaluate the value of the trade_signal so the algorithm 
# plots only 1 entry and exit point per cycle.
for index, row in bb_signals_df.iterrows():
    if (row["close"] < row["BB_LOWER"]) and (trade_signal < 1):
        bb_signals_df.loc[index, "Signal"] = 1.0
        trade_signal += 1
        
    if (row["close"] > row["BB_UPPER"]) and (trade_signal > 0):
        bb_signals_df.loc[index, "Signal"] = -1.0
        trade_signal = 0


# Review the DataFrame
bb_signals_df 
def strategy_four(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"

def strategy_five(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"