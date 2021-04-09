import typing
import pandas
import pandas as pd
from pandas.io.parsers import TextFileReader
import matplotlib.pyplot as plt

tesla_shares: typing.Union[typing.Union[TextFileReader, pandas.Series, pandas.DataFrame, None], typing.Any] = \
    pd.read_csv("HistoricalData_1617705358646.csv")

print(tesla_shares.head())

print(tesla_shares.info())

print(tesla_shares.shape)

print(tesla_shares.describe())

# cleaned data - filled missing values to the value that comes next in the same column
df_cleaned = tesla_shares.fillna(method="bfill", axis=0).fillna(0)
print(tesla_shares.shape, df_cleaned.shape)


# Create a function for calling cleaned Tesla shares data
def tesla_share_data():
    print(df_cleaned)


tesla_share_data()

# Plot a graph with Tesla share data

df = pd.read_csv("HistoricalData_1617705358646.csv",
                 parse_dates=['date'], dayfirst=True)

print(df)

print(df.head())

print(df.tail())

close = df["close/last"]

print(close)

print(close.max())

print(df["volume"].mean())

# Data for plotting
x = df["date"]
y = df["close/last"]

fig, ax = plt.subplots()
ax.plot(x, y, color='teal')

# Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.2f}')
# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

ax.set(xlabel='Date', ylabel='Share Price ($)',
       title='Tesla (TSLA) Closing Share Price')
ax.grid()
fig.tight_layout()

plt.show()
