import tweepy
import time

auth = tweepy.OAuthHandler('O0tUMKETeHk6LhGCEqdH5J43g','qbBqjCRSNrpmqGjOaRZ6rdAxFoYHdjqdrEKx0KGEISUGpUxfAn')
auth.set_access_token('1211753853185449984-ePLQKAVGH7F5PIuWTXKIV8VosxhfNu','m5l55FefVv958JoI6RCN9mXAaXEaDiLVXBJV0agPsDG7J')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'robloxDev', 'roblox'
nrTweets = 2000

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break