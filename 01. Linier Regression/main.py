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
data_frame = data_frame[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

print(data_frame.head())
