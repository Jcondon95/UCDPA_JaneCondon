import pandas as pd
from Tesla_Shares_Analysis import tesla_share_data as tesla_shares
from Elon_Musk_Tweets_Analysis import tesla_tweets as tesla_tweets
import numpy as np
import matplotlib.pyplot as plt

print(tesla_shares)
print(tesla_tweets)

tesla_tweets = pd.read_csv("2020-2021.csv")
tesla_shares = pd.read_csv("HistoricalData_1617705358646.csv")

# Merge Tesla tweet data and Tesla share data together
left = tesla_tweets[["date", "tweet", "nlikes", "nreplies", "nretweets"]]
right = tesla_shares[["date", "close/last", "open"]]

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

# Subset rows for when the share price was greater than the mean
mean_share_price = 323.69
high_share_price = Tesla_data[Tesla_data["close/last"] > 323.69]

print(high_share_price)

# Sort tweets by share price in descending order
high_share_price_srt = high_share_price.sort_values("close/last", ascending=False)

# Select the tweet, share price and number of likes columns
result = high_share_price_srt[["tweet", "close/last", "nlikes"]]

print(result)

# Create a correlation graph between Tesla's share price and engagement with Elon Musk's tweets related to Tesla

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = Tesla_data["close/last"]
y = Tesla_data["nlikes"]
y2 = Tesla_data["nretweets"]
colors = Tesla_data["nlikes"]
area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

fig, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

# Use automatic StrMethodFormatter
ax.xaxis.set_major_formatter('${x:1.2f}')

plt.scatter(x, y, y2, alpha=0.5, c=colors)

xlab = 'Tesla Share Price ($)'
ylab = 'Engagement with Tesla Tweets (likes/retweets)'
title = "Twitter Engagement and Tesla Share Price Correlation"

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.show()

# Create a correlation graph between Tesla's share price and high engagement with Elon Musk's tweets related to Tesla

# Create above average engagement for Tesla: observations with merged_data between mean and max number of likes
print(merged_data.describe())
tweets = merged_data['nlikes']
between = np.logical_and(tweets > 40000, tweets < 120000)
above_average_tweets = merged_data[between]

# Filter for data specific to Tesla
Tesla_data = above_average_tweets[above_average_tweets['tweet'].str.contains("@Tesla")]
# Fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = Tesla_data["close/last"]
y = Tesla_data["nlikes"]
y2 = Tesla_data["nretweets"]
colors = Tesla_data["nlikes"]
area2 = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

fig2, ax = plt.subplots()
ax.plot(100 * np.random.rand(20))

# Use automatic StrMethodFormatter
ax.xaxis.set_major_formatter('${x:1.2f}')

plt.scatter(x, y, y2, alpha=0.5, c=colors)

xlab = 'Tesla Share Price ($)'
ylab = 'Engagement with Tesla Tweets (likes/retweets)'
title = "High Twitter Engagement and Tesla Share Price Correlation"

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.show()
