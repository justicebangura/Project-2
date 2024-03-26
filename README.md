# Group 1 (Justice Bangura, Joanne Laomoc, Katie Nieuwhof , Gandhi Sahib )

![Python Trading bot](https://static.wixstatic.com/media/1938a7_bbb79b18becc4fcab343725d12ae2598~mv2.jpg/v1/fit/w_1000%2Ch_768%2Cal_c%2Cq_80/file.jpg)

### Overview:

Our goal was to create a trading bot to predict the future performance of a stock profitability, using different trading strategies combined with LSTM (LongShort-Term Memory) networks. This project aims to provide a tool for traders to make informed decisions based on predictive analytics.

### Features:
- **Feature Engineering**: Manipulated data to curate mulitple features to feed into the model to generate internal structures.
- **Multiple Trading Strategies**: Implemented various trading strategies such as simple momemtum, DMAC (Dual Moving Average Crossover), Finta, Bollinger Bands and Pairs Trading.
- **Data Processing and Cleaning**:
- **Model Engineering**: LSTM 
- **Backtesting**: Utilized a variety of methods, Risk and Rewards evaluation metrics such as Annualized Return, Cumulative Returns, Annual Volatility, Sharpe Ratio and Sortino Ratio. Enables backtesting of trading strategies to evaluate their performance over historical data using visual displays. 



#### Steps: 

1. Data collection - using Api or Alpaca to gather stock information, and get env and gitignore

2. Feature engineering - find the best combination of additional features and trading strategy we want to use to make the model better to increase profitability and find out the optimal training window size using the rolling window function. including different features like pct change(daily), annual returns, cumulative change, and simple moving averages using the rolling window. 

3. Backtesting - Try out different models to see which model performs best, with our trading Strategy as well as different trading features.

4. Predictions - profitability, Volatility, 

5. nnModel evaluations - we can use neural networks, lstm, log_reg,  and evaluate the classification reports, etc

6. Metrics/Plotting - See if Our Deep learning model beats the baseline using an overlay graph *, and also if our trading strategy is better than say Buy and Hold and S&p500 index which is an average of 8.5%

Files:

AlgoTrading_bot.ipynb (we all work together on the main file)
imports -------Feauture engineering! 
a function that chooses the best trading strategy but combines strategy in the Def function[import strategy from strategy.py as a list]
a function that chooses the best nn Model or combines model in the Def function[import models from models.py as a list]
Plots--------------------------using hvplot
function to place a trade


strategy.py

models.py 

backtesting.py

plotting.py

put more focus on neuro networking and lstm Models 
### Usage and Installation:
- ! pip install tensorflow
- ! 

### Findings: 


### Conclusion:

### Next Steps:
- **Stock Prediction**
- **Real-Time Trading**
