# Imports

# check correlation of strategies the returns should be uncorelated to reduce overall portfolio risk - diversification

def strategy_one(Stock_data):
    #lets write logic for strategy
    return "Signal- Buy or sell"


def strategy_two(Stock_data):
    ## Read the aapl.csv file into a Pandas DataFrame
# Set the date column as the DateTimeIndex
aapl_df = pd.read_csv(
    Path("../Resources/aapl.csv"),
    index_col="date",
    parse_dates=True,
    infer_datetime_format=True
)
# Review the DataFrame
aapl_df.head()
# Filter the date index and close columns
signals_df = aapl_df.loc[:,["close"]]

# Review the DataFrame
signals_df.head()
short_window = 50
long_window = 100
# Generate the short and long window simple moving averages (50 and 100 days, respectively)
signals_df["SMA50"] = signals_df["close"].rolling(window=short_window).mean()
signals_df["SMA100"] = signals_df["close"].rolling(window=long_window).mean()

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
entry = signals_df[signals_df["Entry/Exit"] == 1.0]["close"].hvplot.scatter(
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
security_close = signals_df[["close"]].hvplot(
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
    title="Apple - SMA50, SMA100, Entry and Exit Points"
)
    return "Signal-Buy or sell"


def strategy_three(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"


def strategy_four(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"

def strategy_five(Stock_data):
    #lets write logic for strategy
    return "Signal-Buy or sell"