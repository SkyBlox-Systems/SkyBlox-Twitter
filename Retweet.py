import tweepy
import time

auth = tweepy.OAuthHandler('2pZBE81oZ9KGjOn28By6SzblQ','L5q73xBiVWMWnr7YuZktnHw5rVO8qVkwce29ZJ1s7XJhdrSCR6')
auth.set_access_token('1211753853185449984-jGhuOp7NrnVkAN7AZYjvutWMyBhOn9', 'jFRTcj6h0szfhXQdVV57yMov6OadnDo7StB7Niu8gpDUf')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

ROBLOX = 'robloxDev', '#RobloxDev'
nrTweets = 750

for tweet in tweepy.Cursor(api.search, ROBLOX).items():
    try:
        tweet.retweet()
        print('tweet retweeted')
        time.sleep(25)
    except tweepy.TweepError as e:
        time.sleep(5)
        print(e.reason)
    except StopIteration:
        break
