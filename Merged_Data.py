import pandas as pd

from Elon_Musk_Tweets_Analysis import Tesla_tweets as Tesla_tweets

print(Tesla_tweets)

from Tesla_Shares_Analysis import Tesla_share_data as Tesla_shares

print(Tesla_shares)

Tesla_tweets = pd.read_csv("2020-2021.csv")
Tesla_shares = pd.read_csv("HistoricalData_1617705358646.csv")

# Merge Tesla tweet data and Tesla share data together
left = Tesla_tweets[["date", "tweet", "nlikes", "nreplies", "nretweets"]]
right = Tesla_shares[["date", "close/last", "open"]]

merged_data = pd.merge(left, right, on="date")

print(left.shape, right.shape)
print(merged_data.describe())
print(merged_data.columns)
print(merged_data.shape)

print(merged_data)

# Filter for data specific to Tesla
Tesla_data = merged_data[merged_data['tweet'].str.contains("@Tesla")]

print(Tesla_data.head)
print(Tesla_data.describe())

# For every tweet where the share price is higher than average, print the tweet
mean_share_price = 323.69

# Subset rows for when the share price was greater than the mean
high_share_price = Tesla_data[Tesla_data["close/last"] > 323.69]

print(high_share_price)

# Sort tweets by share price in order of descending value
high_share_price_srt = high_share_price.sort_values("close/last", ascending=False)

# Select the tweet, share price and number of likes columns
result = high_share_price_srt[["tweet", "close/last", "nlikes"]]

print(result)

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = Tesla_data["close/last"]
y = Tesla_data["nlikes"]
y2 = Tesla_data["nretweets"]
colors = Tesla_data["nlikes"]
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

fig, ax = plt.subplots()
ax.plot(100*np.random.rand(20))

# Use automatic StrMethodFormatter
ax.xaxis.set_major_formatter('${x:1.2f}')

plt.scatter(x, y, y2, alpha=0.5, c=colors)

xlab = 'Tesla share price'
ylab = 'Engagement with Tesla tweets (likes/retweets)'
title = "Correlation between engagement with Tesla tweets and Tesla share price in 2020/2021"

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.show()