import pandas as pd
from pandas.plotting import register_matplotlib_converters
import numpy as np
import matplotlib.pyplot as plt

register_matplotlib_converters()

musk_tweets = pd.read_csv("2020-2021.csv")

print(musk_tweets.info())

print(musk_tweets.head())

print(musk_tweets.shape)

print(musk_tweets.describe())

print(musk_tweets.values)

print(musk_tweets.columns)

print(musk_tweets.index)

# Filter for Elon Musk tweets specific to Tesla
tesla_tweets1 = musk_tweets[musk_tweets['tweet'].str.contains("@Tesla")]


def tesla_tweets():
    print(tesla_tweets1)


tesla_tweets()

# Sort Elon Musk's tweets by number of likes in descending order
musk_tweets_sorted = musk_tweets.sort_values(['nlikes'], ascending=[False])
print(musk_tweets_sorted.head())

# Create a list of most liked Elon Musk tweets with corresponding date
musk_top_tweets = musk_tweets_sorted[["date", "tweet", "nlikes", "nreplies", "nretweets"]]
print(musk_top_tweets.head())

# Filter for Elon Musk tweets specific to Tesla
tesla_tweets = musk_tweets_sorted[musk_tweets_sorted['tweet'].str.contains("@Tesla")]
print(tesla_tweets.head)
print(tesla_tweets.info())

# Cleaned data - filled missing values to the value that comes next in the same column
tesla_tweets_filled = tesla_tweets.fillna(method="bfill", axis=0).fillna(0)
print(tesla_tweets.shape, tesla_tweets_filled.shape)
print(tesla_tweets_filled.info())

# Cleaned data - dropped columns with missing values
tesla_tweets_dropped = tesla_tweets.dropna(axis=1)
print(tesla_tweets_filled.shape, tesla_tweets_dropped.shape)
print(tesla_tweets_dropped.info())

# Filter for tesla tweets where likes are greater than 10000
tesla_tweets_10k = tesla_tweets_dropped[tesla_tweets_dropped["nlikes"] > 10000]

assert isinstance(tesla_tweets_10k.shape, object)
print(tesla_tweets_10k.shape)

# Create a list of popular Elon Musk tweets related to tesla where number of likes is greater than 10k
tesla_tweets_pop = tesla_tweets_10k[["date", "tweet", "nlikes", "nreplies", "nretweets"]]
print(tesla_tweets_pop)

# Create a DataFrame from popular Tesla Tweets
Tesla = pd.DataFrame(tesla_tweets_pop)
print(Tesla)

# Filter for tweets specific to SpaceX
SpaceX_tweets = musk_tweets_sorted[musk_tweets_sorted['tweet'].str.contains("@SpaceX")]
print(SpaceX_tweets.head)
print(SpaceX_tweets.info())

# Filter for Space X tweets where likes are greater than 10000
SpaceX_tweets_10k = SpaceX_tweets[SpaceX_tweets["nlikes"] > 10000]
print(SpaceX_tweets_10k.shape)

# Create a list of popular Elon Musk tweets related to Space X where number of likes is greater than 10k
SpaceX_tweets_pop = SpaceX_tweets_10k[["date", "tweet", "nlikes", "nreplies", "nretweets"]]
print(SpaceX_tweets_pop)

# Create a DataFrame from popular Space X Tweets
SpaceX = pd.DataFrame(SpaceX_tweets_pop)
print(SpaceX)


# Create a function for calling SpaceX data
def spacex_data():
    print(SpaceX_tweets_pop)


spacex_data()


# Create a function for calling Tesla data
def tesla_tweet_data():
    print(tesla_tweets_pop)


tesla_tweet_data()

# Create above average engagement for Space X: observations with SpaceX_tweets_pop between mean and max number of likes
print(SpaceX_tweets_pop.describe())
tweets = SpaceX_tweets_pop['nlikes']
between = np.logical_and(tweets > 27334, tweets < 235245)
above_average_spacex = SpaceX_tweets_pop[between]

print(above_average_spacex)
print(above_average_spacex.describe())

# Build a for loop for each tweet with above average likes
for tweet in above_average_spacex:
    print('Elon Musks tweet about Space X on ' + above_average_spacex["date"] + ' received ' + str(
        above_average_spacex['nlikes']) + 'likes ')

# Create above average engagement for Tesla: observations with tesla_tweets_pop between mean and max number of likes
print(tesla_tweets_pop.describe())
tweets = tesla_tweets_pop['nlikes']
between = np.logical_and(tweets > 27334, tweets < 235245)
above_average_tesla = tesla_tweets_pop[between]

print(above_average_tesla)
print(above_average_tesla.describe())

# Build a for loop for each tweet with above average likes
for tweet in above_average_tesla:
    print('Elon Musks tweet about Tesla on ' + above_average_tesla["date"] + ' received ' + str(
        above_average_tesla['nlikes']) + 'likes ')

df = pd.read_csv("2020-2021.csv",
                 parse_dates=['date'], dayfirst=True)

tesla_tweets = df[df['tweet'].str.contains("@Tesla")]
spacex_tweets = df[df['tweet'].str.contains("@SpaceX")]

# Data for plotting
x = tesla_tweets["date"]
y = tesla_tweets["nlikes"]
x2 = spacex_tweets["date"]
y2 = spacex_tweets["nlikes"]

fig, ax = plt.subplots()
ax.plot(x, y, color='lightseagreen', label="Tesla", alpha=0.7)
ax.plot(x2, y2, color='darkslateblue', label="SpaceX", alpha=0.7)

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

ax.set(xlabel='Date', ylabel='Number of Likes',
       title='Engagement with Elon Musks Tweets (2020-2021)')
ax.legend(loc='upper right')

ax.grid()
fig.tight_layout()

plt.show()

