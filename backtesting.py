# This file contains seperate functions for backtesting 
import pandas as pd
import numpy as np



def subset_around_crossovers(stock_df, all_cross_points):
    # Extract buy and sell points from stock_df
    buy_points = stock_df['entry']
    sell_points = stock_df['exit']

    # Combine buy and sell points into all_cross_points
    all_cross_points = buy_points | sell_points

    # Find indices of crossover points
    crossover_indices = np.where(all_cross_points)[0]

    # Define row ranges around crossover points
    row_ranges = []
    for index in crossover_indices:
        start_row = max(index - 1, 0)  # Start one row before the crossover point
        end_row = min(index + 1, len(stock_df))  # End one row after the crossover point
        row_ranges.extend(range(start_row, end_row))

    # Remove duplicate rows and sort them
    unique_rows = sorted(set(row_ranges))

    # Extract subset DataFrame based on unique rows
    stock_df = stock_df.iloc[unique_rows]

    return stock_df

def calculate_position(stock_df):
    # Set the share size
    share_size = 3000
    
    # Calculate position based on major signal
    stock_df['Position'] = share_size * stock_df['Signal']
    
    return stock_df

def calculate_entry_exit_position(stock_df):
    # Calculate entry/exit position
    stock_df['Entry/Exit Position'] = stock_df['Position'].diff()
    
    return stock_df

def calculate_portfolio_holdings(stock_df):
    # Set initial capital
    initial_capital = float(100000)
    
    # Calculate portfolio holdings
    stock_df['Portfolio Holdings'] = stock_df['close'] * stock_df['Position']
    
    return stock_df

def calculate_cash_returns(stock_df):
    # Set initial capital
    initial_capital = float(100000)
    
    # Calculate portfolio cash
    stock_df['Portfolio Cash'] = initial_capital - (stock_df['close'] * stock_df['Entry/Exit Position']).cumsum() 
    
    # Calculate portfolio total
    stock_df['Portfolio Total'] = stock_df['Portfolio Cash'] + stock_df['Portfolio Holdings']
    
    # Calculate portfolio daily returns
    stock_df['Portfolio Daily Returns'] = stock_df['Portfolio Total'].pct_change()
    
    # Calculate portfolio cumulative returns
    stock_df['Portfolio Cumulative Returns'] = (1 + stock_df['Portfolio Daily Returns']).cumprod() - 1
    
    return stock_df

def portfolio_metrics(stock_df):
    # Initialize a new DataFrame to hold evaluation metrics
    portfolio_evaluation_df = pd.DataFrame(index=[
        "Annualized Return",
        "Cumulative Returns",
        "Annual Volatility",
        "Sharpe Ratio",
        "Sortino Ratio"
    ], columns=["Strategy Backtest"])

    # Calculate annualized return
    annualized_return = stock_df["Portfolio Daily Returns"].mean() * 252
    portfolio_evaluation_df.loc["Annualized Return", "Strategy Backtest"] = annualized_return

    # Calculate cumulative return
    cumulative_return = stock_df["Portfolio Cumulative Returns"].iloc[-1]
    portfolio_evaluation_df.loc["Cumulative Returns", "Strategy Backtest"] = cumulative_return

    # Calculate annual volatility
    annual_volatility = stock_df["Portfolio Daily Returns"].std() * np.sqrt(252)
    portfolio_evaluation_df.loc["Annual Volatility", "Strategy Backtest"] = annual_volatility

    # Calculate Sharpe Ratio (assuming risk-free rate of 2%)
    risk_free_rate = 0.02
    sharpe_ratio = (annualized_return - risk_free_rate) / annual_volatility
    portfolio_evaluation_df.loc["Sharpe Ratio", "Strategy Backtest"] = sharpe_ratio

    # Calculate Sortino Ratio
    sortino_ratio_df = stock_df[["Portfolio Daily Returns"]].copy()
    sortino_ratio_df["Downside Returns"] = np.where(sortino_ratio_df["Portfolio Daily Returns"] 
                                                    < 0, sortino_ratio_df["Portfolio Daily Returns"], 0)
    downside_standard_deviation = sortino_ratio_df["Downside Returns"].std() * np.sqrt(252)
    sortino_ratio = annualized_return / downside_standard_deviation
    portfolio_evaluation_df.loc["Sortino Ratio", "Strategy Backtest"] = sortino_ratio

    return portfolio_evaluation_df



def trade_evaluation(stock_df):
    trade_evaluation_df = pd.DataFrame(columns=[
        "Stock", "Entry Date", "Exit Date", "Shares", "Entry Share Price",
        "Exit Share Price", "Entry Portfolio Holding", "Exit Portfolio Holding",
        "Profit/Loss" ])

    for index, row in stock_df.iterrows():
        if row["Signal"] == 1:
            entry_date = index
            entry_portfolio_holding = row["Portfolio Holdings"]
            share_size = row["Entry/Exit Position"]
            entry_share_price = row["close"]

        elif row["Signal"] == -1:
            exit_date = index
            exit_portfolio_holding = abs(row["close"] * row["Entry/Exit Position"])
            exit_share_price = row["close"]
            profit_loss = exit_portfolio_holding - entry_portfolio_holding

            # Update trade evaluation DataFrame
            trade_evaluation_df = trade_evaluation_df.append({
                "Stock": "META",
                "Entry Date": entry_date,
                "Exit Date": exit_date,
                "Shares": share_size,
                "Entry Share Price": entry_share_price,
                "Exit Share Price": exit_share_price,
                "Entry Portfolio Holding": entry_portfolio_holding,
                "Exit Portfolio Holding": exit_portfolio_holding,
                "Profit/Loss": profit_loss }, ignore_index=True)

    return trade_evaluation_df


