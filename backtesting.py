# This file contains seperate functions for tuning and improving the models and strategies

# This file contains seperate functions for tuning and improving the models and strategies

### BackTesting is overlaying the model prediction plot with the historical stock data. This will help us visualize if our model can predict well and beat the return prices 
 # Portfolio Optimization strategies need to be backtested on historical data after predicting future stock prices to be absolutely sure about the model.
 # We can have plots to visualize if th 
    
    
### Tuning is not defining functions it's playing around with the model. 
# Once we create our baseline model (i.e determine our core features (feature engineering)) 
# We split the data into train and test (what will be our label from the features (y)
# Standardized  and clean the data 
# Build the LSTM & NN model
# Fit the Training Data
# Use the model to make predictions on the test set
# anaylze the data by using classfication report, visual the data, overlay with historical data

### Than we tune the baseline model by:
  # removing or adding more features to feed into the machine 
  # adding or removing layers (hidden, outer, nodes) into the NN model.
  # By creating our baseline function 