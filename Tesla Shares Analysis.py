import typing

import pandas
import pandas as pd
import pip
import yfinance as yfinance
from pandas.io.parsers import TextFileReader

tesla_shares: typing.Union[typing.Union[TextFileReader, pandas.Series, pandas.DataFrame, None], typing.Any] = \
    pd.read_csv("HistoricalData_1617705358646.csv")

print(tesla_shares.head())

print(tesla_shares.info())

print(tesla_shares.shape)

print(tesla_shares.describe())

import pandas as pd

df = pd.read_csv("HistoricalData_1617705358646.csv")

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

import matplotlib.pyplot as plt

plt.plot(df_cleaned['date'], df_cleaned['close/last'])
plt.plot(figsize=(12, 7))
plt.show()


