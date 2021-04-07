import typing

import pandas
import pandas as pd
from pandas.io.parsers import TextFileReader

tesla_shares: typing.Union[typing.Union[TextFileReader, pandas.Series, pandas.DataFrame, None], typing.Any] = \
    pd.read_csv("HistoricalData_1617705358646.csv")

print(tesla_shares.head())

print(tesla_shares.info())

print(tesla_shares.shape)

print(tesla_shares.describe())

import pandas as pd

df = pd.read_csv("HistoricalData_1617705358646.csv")

df_time = pd.to_datetime(df['date'])

print(df)

print(df.head())

print(df.tail())

close = df["close/last"]

print(close)

print(close.max())

print(df["volume"].mean())

# cleaned data - filled missing values to the value that comes next in the same column
df_cleaned = df.fillna(method="bfill", axis=0).fillna(0)
print(df.shape, df_cleaned.shape)

# Create a function for calling Tesla shares data
def Tesla_share_data():
    print(df_cleaned)


Tesla_share_data()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

# Data for plotting
x = df_cleaned["date"]
y = df_cleaned["close/last"]

fig, ax = plt.subplots()
ax.plot(x, y, color='teal')
ax.invert_xaxis()

# Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.2f}')
# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

ax.set(xlabel='Date', ylabel='Share Price',
       title='Tesla (TSLA) Closing Share Price')
ax.grid()
fig.tight_layout()

plt.show()