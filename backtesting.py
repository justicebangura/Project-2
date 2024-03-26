# This file contains seperate functions for backtesting 
import pandas as pd
import numpy as np


def calculate_position(stock_df):
    # Set the share size
    share_size = 300
    
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
    
    trade_evaluation_list = []    
    entry_date = None
    entry_portfolio_holding = 0
    share_size = None

    for index, row in stock_df.iterrows():
        if row["entry"] == 1:
            entry_date = index
            entry_portfolio_holding = row["close"]
            share_size = row["Signal"]

        elif row["exit"] == -1:
            exit_date = index
            exit_portfolio_holding = abs(row["close"] * row["Signal"])
            exit_share_price = row["close"]
            profit_loss = exit_portfolio_holding - entry_portfolio_holding

            # Append data to the trade evaluation list
            trade_evaluation_list.append({
                "Symbol": row["symbol"],
                "Entry Date": entry_date,
                "Exit Date": exit_date,
                "Shares": share_size,
                "Entry Share Price": entry_portfolio_holding,
                "Exit Share Price": exit_share_price,
                "Entry Portfolio Holding": entry_portfolio_holding,
                "Exit Portfolio Holding": exit_portfolio_holding,
                "Profit/Loss": profit_loss })

    trade_evaluation_df = pd.DataFrame(trade_evaluation_list)
    return trade_evaluation_df





