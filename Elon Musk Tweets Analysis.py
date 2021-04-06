import typing

import pandas
import pandas as pd
from pandas.io.parsers import TextFileReader
# Date time conversion registration
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

musk_tweets: typing.Union[typing.Union[TextFileReader, pandas.Series, pandas.DataFrame, None], typing.Any] = \
    pd.read_csv("2020-2021.csv")

print(musk_tweets.info())

print(musk_tweets.head())

print(musk_tweets.info())

print(musk_tweets.shape)

print(musk_tweets.describe())

print(musk_tweets.values)

print(musk_tweets.columns)

print(musk_tweets.index)

musk_top_tweets = musk_tweets.sort_values(['nlikes'], ascending=[False])

print(musk_top_tweets.head())

most_liked_tweets = musk_top_tweets[["tweet", "nlikes", "date"]]

print(most_liked_tweets.head())

tesla_tweets = musk_tweets[musk_tweets['tweet'].str.contains("@Tesla")]

print(tesla_tweets.head)

print(tesla_tweets.info())

# cleaned data - filled missing values to the value that comes next in the same column
tesla_tweets_cleaned = tesla_tweets.fillna(method="bfill", axis=0).fillna(0)
print(tesla_tweets.shape, tesla_tweets_cleaned.shape)

print(tesla_tweets_cleaned.info())

import matplotlib.pyplot as plt

df = tesla_tweets_cleaned[["date", "nlikes"]]

plt.plot(figsize=(12, 7))
plt.plot(df['date'], df['nlikes'])
plt.xticks(rotation='vertical')
df = df.sort_values(['date'], ascending=True)

xlab = 'Date'
ylab = 'No. of likes'
title = 'Elon Musk tweets about Tesla 2020 - 2021'

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.show()
