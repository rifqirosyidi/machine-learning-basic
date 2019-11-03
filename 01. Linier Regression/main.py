import math

import pandas as pd
import quandl

data_frame = quandl.get("WIKI/GOOGL")

# Recreate the Data Frame Just to some Features
data_frame = data_frame[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Get The High Low Percentage
data_frame['HL_PCT'] = (data_frame['Adj. High'] - data_frame['Adj. Close']) / data_frame['Adj. Close'] * 100.0

# Get The Percentage Change
data_frame['PCT_CHANGE'] = (data_frame['Adj. Close'] - data_frame['Adj. Open']) / data_frame['Adj. Open'] * 100.0

# Get The Data That only we wanted
data_frame = data_frame[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]  # THIS IS FEATURES

# Data to be Forecasted
forecast_col = 'Adj. Close'  # Stock End Price
data_frame.fillna(-99999, inplace=True)

# Get The last 1 % of the all data to predict the next stock price
forecast_out = int(math.ceil(0.01*len(data_frame)))

# Shift the column to 1 of the data %
data_frame['label'] = data_frame[forecast_col].shift(-forecast_out)

print(data_frame.head())
