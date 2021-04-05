import typing

import pandas
import pandas as pd
from pandas.io.parsers import TextFileReader

tesla_shares: typing.Union[typing.Union[TextFileReader, pandas.Series, pandas.DataFrame, None], typing.Any] = \
    pd.read_csv("HistoricalData_1617616889783.csv")

print(tesla_shares.head())

print(tesla_shares.info())

print(tesla_shares.shape)

print(tesla_shares.describe())

musk_tweets: typing.Union[typing.Union[TextFileReader, pandas.Series, pandas.DataFrame, None], typing.Any] = \
    pd.read_csv("2021.csv")

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
