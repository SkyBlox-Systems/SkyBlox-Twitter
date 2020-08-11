import tweepy
import time
import random

auth = tweepy.OAuthHandler('yzU6NBa8pWlhzpVGSo3Dc0Ahs','z7p7SBgEOwQg8n0qkkFbG9fkgjy5ZaJFZ4dQNm5cb0bUQFvAJp')
auth.set_access_token('1211753853185449984-6Wq0WGzWRNfm9OwdL40fI8eXvtDMyU','t6OrY9TyDyQdqZoRzhBn9UPBXCdTExgRmQT5lYLGVXKgQ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
followers = tweepy.Cursor(api.followers).items()