import tweepy
import json

# load keys from json
with open("keys.json", "r") as f:
    keys = json.load(f)

# set keys
auth = tweepy.OAuthHandler(keys["CONSUMER_KEY"], keys["CONSUMER_SECRET"])
auth.set_access_token(keys["ACCESS_TOKEN"], keys["ACCESS_SECRET"])
api = tweepy.API(auth)

# Tweet
while True:
    text = input("Tweet text: ")
    api.update_status(status=text)