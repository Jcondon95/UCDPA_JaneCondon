import pandas as pd

Elon_musk_tweets = pd.read_csv("2020-2021.csv")
Tesla_shares = pd.read_csv("HistoricalData_1617705358646.csv")

print(Elon_musk_tweets.head)
print(Elon_musk_tweets.shape)

Elon_musk_tweets_cleaned = Elon_musk_tweets.dropna(axis=1)

print(Elon_musk_tweets, Elon_musk_tweets_cleaned)

Tesla_tweets = Elon_musk_tweets_cleaned[Elon_musk_tweets_cleaned['tweet'].str.contains("@Tesla")]

print(Elon_musk_tweets_cleaned.shape, Tesla_tweets.shape)

print(Tesla_shares.head)
print(Tesla_shares.shape)

print(Tesla_tweets.shape, Tesla_shares.shape)

left = Tesla_tweets[["date", "tweet", "nlikes", "nreplies", "nretweets"]]
right = Tesla_shares[["date", "close/last", "open"]]

merged_data = pd.merge(left, right, on="date")

print(left.shape, right.shape)
print(merged_data.describe())
print(merged_data.columns)
print(merged_data.shape)

print(merged_data)

