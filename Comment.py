import tweepy
import time

auth = tweepy.OAuthHandler('m7bxRtNvSoiEESjWZs1JseKfz','8rY9YQvTSzznViUa5MoGti1JzfZZBleVlP5LagZlLKjPCktmfl')
auth.set_access_token('1211753853185449984-NIshQh4KEiTs951sLyteptaqG6DBvG','gOKUHK8xKVGoVTdBNnAtdldBNGRGSIgawFyY14fQuQ2pL')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'robloxDev', 'roblox'
nrTweets = 2000