import tweepy
import time

auth = tweepy.OAuthHandler('GpwqR6hKaV8jSGSHeXiFGggx5','kiSVu84kXANSVCTsMY050fpSF1VJ7R5r0TdfDlZoWxQtLtesOD')
auth.set_access_token('1211753853185449984-GPCADlRP3rgOF1dBc5wcFErXkG3jZz', 'R2MrX3gsjmmHSvaDZrQBrI8OrNwptIgxtya7UZlMJxHtm')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

ROBLOX = 'robloxDev', '#RobloxDev', 'RobloxDeveloper'
nrTweets = 750

for tweet in tweepy.Cursor(api.search, ROBLOX).items():
    try:
        tweet.retweet()
        print('tweet retweeted')
        time.sleep(20)
    except tweepy.TweepError as e:
        time.sleep(30)
        print(e.reason)
    except StopIteration:
        break
