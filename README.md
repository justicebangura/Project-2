# Group 1 (Justice Bangura, Joanne Laomoc, Katie Nieuwhof , Gandhi Sahib )

![Python Trading bot](https://static.wixstatic.com/media/1938a7_bbb79b18becc4fcab343725d12ae2598~mv2.jpg/v1/fit/w_1000%2Ch_768%2Cal_c%2Cq_80/file.jpg)

### Purpose:

Our goal was to create a trading bot to predict the future performance of a stock profitability, using different trading strategies combined with LSTM (LongShort-Term Memory) networks. This project aims to provide a tool for traders to make informed decisions based on predictive analytics.

### Overview:
- **Data Collection**: Utilized Alpaca API to fetch historical stock data for companies
- **Feature Engineering**: Manipulated data to curate mulitple features to feed into the model to generate internal structures.
- **Multiple Trading Strategies**: Implemented various trading strategies such as simple momemtum, DMAC (Dual Moving Average Crossover), Finta, Bollinger Bands and Pairs Trading.
- **Data Processing and Cleaning**: Used a variety of methods to clean, process and standardized the data such as, dropna, PCA, Standard Scaler. 
- **Model Engineering**: Engineered the LSTM to work functionally with our dataset by reshaping the model to fit a 3-D array.
- **Split, Train, Fit Data**: Split the data into Train and Test. Fit the data to feed into the model.
- **Predictions**: Use the model to make predictions on the test set.
- **Backtesting**: Utilized a variety of methods, Risk and Rewards evaluation metrics such as Annualized Return, Cumulative Returns, Annual Volatility, Sharpe Ratio and Sortino Ratio. Enables backtesting of trading strategies to evaluate their performance over historical data using visual displays. 

### Installation:
- ! pip install tensorflow
- ! pip install finta
- ! pip install install alpaca-trade-api
- install required dependencies
- Execute Jupyter Notebook

### Usage:
- Use fetch_stock_data to create a stock dataframe
- Use features to curate what features you want to add into your dataframe
- Clean and Process your data
- Create a buy/sell/hold Algorithim to feed into the model to make predictions
- Split the data into Train and Test sets
- Standarize and fit the data
- Feed into the LSTM Model
- Run analysis 


### Results and Summary:
- In summary, we found our model was biased towards the buy signal, and didn't produce as high of an accuracy score or return as we would have liked. This can be indentified in our backtesting and analysis portion of our notebook, with plots included in this section. 

### Challenges:
The major challenges we faced was engineering the LSTM model and understanding how to reshape and fit a 3D model. We also experienced challenges balancing the classes to avoid model bias.

### Conclusion:
- Overall, we have learnt a great deal and now have a strong understanding in builiding a trading bot and utilizing LSTM models. Despite the challenges we faced, we have the ground work complete and may continue fine tuning the model to achieve a more profitable outcome in future. 

### Next Steps:
- Curate our model into a continuous model.
- Knowing it predicts high buy signals, we could tune the model to randomly sell.
- Modify it to be a Stock Prediction Model
- Real-Time Trading


### Authors:
**Justice Bangura**: Risk/Rewards, created the basline for everything
**Joanne Laomoc**: Feature Engineering
**Katie Nieuwhof**: LSTM Model Engineering
**Gandhi Sahib**: Algorithium Trading
