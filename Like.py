import tweepy
import time

auth = tweepy.OAuthHandler('PkBAwHA9bQJTmFdbtvHRIUZlW','Nwtyfbt3kd3Oyl5eBM08hL4cM4aKEVRK1IwegEEGXWwZGhbUbn')
auth.set_access_token('1211753853185449984-OzqDKMk8Xgm2y3TqcTAv2C3WcrS0Uc','Algq4266sPpW54oYBklCglIXUGtRgrwHJviFB5OCFOImj')

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
        time.sleep(30)
        print(e.reason)
    except StopIteration:
        break
