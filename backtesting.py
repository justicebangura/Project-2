# This file contains seperate functions for backtesting 
def calculate_position(stock_df):
    # Set initial capital
    initial_capital = float(100000)

    # Set the share size
    share_size = 500
    
    # Buy a 500 share position when the dual moving average crossover Signal equals 1
    # Otherwise, `Position` should be zero (sell)
    stock_df['Position'] = share_size * stock_df['Model_Signal']
    return stock_df


def subset_around_crossovers(df, crossover_points):
    crossover_indices = np.where(crossover_points)[0]
    row_ranges = []
    for index in crossover_indices:
        start_row = max(index - 1, 0)
        end_row = min(index + 1, len(df))
        row_ranges.extend(range(start_row, end_row))
    unique_rows = sorted(set(row_ranges))
    return df.iloc[unique_rows]




import pandas as pd
import numpy as np

def portfolio_metrics(stock_df):
    # Calculate annualized return
    stock_df.loc["Annualized Return"] = (
        stock_df["Portfolio Daily Returns"].mean() * 252
    )

    # Calculate cumulative return
    stock_df.loc["Cumulative Returns"] = stock_df["Portfolio Cumulative Returns"].iloc[-1]

    # Calculate annual volatility
    stock_df.loc["Annual Volatility"] = (
        stock_df["Portfolio Daily Returns"].std() * np.sqrt(252)
    )

    # Create a DataFrame that contains the Portfolio Daily Returns column
    sortino_ratio_df = stock_df[["Portfolio Daily Returns"]].copy()

    # Create a column to hold downside return values
    sortino_ratio_df.loc[:, "Downside Returns"] = 0.0

    # Find Portfolio Daily Returns values less than 0,
    # square those values, and add them to the Downside Returns column
    sortino_ratio_df.loc[sortino_ratio_df["Portfolio Daily Returns"] < 0,
                         "Downside Returns"] = abs(sortino_ratio_df["Portfolio Daily Returns"])

    # Calculate the annualized return value
    annualized_return = (
        sortino_ratio_df["Portfolio Daily Returns"].mean() * 252
    )

    # Calculate the annualized downside standard deviation value
    downside_standard_deviation = (
        sortino_ratio_df["Downside Returns"].std() * np.sqrt(252)
    )

    # The Sortino ratio is reached by dividing the annualized return value
    # by the downside standard deviation value
    sortino_ratio = annualized_return / downside_standard_deviation

    # Add the Sortino ratio to the evaluation DataFrame
    stock_df.loc["Sortino Ratio"] = sortino_ratio

    return stock_df


def trade_evaluation(stock_df):
    trade_evaluation_df = pd.DataFrame(columns=[
        "Stock", "Entry Date", "Exit Date", "Shares", "Entry Share Price",
        "Exit Share Price", "Entry Portfolio Holding", "Exit Portfolio Holding",
        "Profit/Loss"
    ])

    for index, row in stock_df.iterrows():
        if row["Entry/Exit"] == 1:
            entry_date = index
            entry_portfolio_holding = row["Portfolio Holdings"]
            share_size = row["Entry/Exit Position"]
            entry_share_price = row["close"]

        elif row["Entry/Exit"] == -1:
            exit_date = index
            exit_portfolio_holding = abs(row["close"] * row["Entry/Exit Position"])
            exit_share_price = row["close"]
            profit_loss = exit_portfolio_holding - entry_portfolio_holding

            # Update stock_df with trade evaluation
            stock_df.at[index, "Stock"] = "AAPL"
            stock_df.at[index, "Entry Date"] = entry_date
            stock_df.at[index, "Exit Date"] = exit_date
            stock_df.at[index, "Shares"] = share_size
            stock_df.at[index, "Entry Share Price"] = entry_share_price
            stock_df.at[index, "Exit Share Price"] = exit_share_price
            stock_df.at[index, "Entry Portfolio Holding"] = entry_portfolio_holding
            stock_df.at[index, "Exit Portfolio Holding"] = exit_portfolio_holding
            stock_df.at[index, "Profit/Loss"] = profit_loss

    return stock_df


