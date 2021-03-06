import tweepy
from tweepy import OAuthHandler
import pandas as pd

"""I like to have my python script print a message at the beginning. This helps me confirm whether everything is set up correctly. And it's nice to get an uplifting message ;)."""

print("You got this!")

access_token = '1355553264704450562-L2AIngcMqFPAr6Oex5jnkv4RDRD9nZ'
access_token_secret = 'YMCgLMEeoAXpVafSfUQvI7vYa10yYEBaL8kEkQU7LULsy'
consumer_key = 'MDBBLLoxIu0tUmFl0hbjmXoTr'
consumer_secret = 'FPKpbYZfXhtOwfMwvIci8dI23jRHDYbe2OXEgY3WZYtSFSBE4k'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []

count = 1

"""Twitter will automatically sample the last 7 days of data. Depending on how many total tweets there are with the specific hashtag, keyword, handle, or key phrase that you are looking for, you can set the date back further by adding since= as one of the parameters. You can also manually add in the number of tweets you want to get back in the items() section."""

for tweet in tweepy.Cursor(api.search, q="@BNonnecke", count=450, since='2020-02-28').items(50000):
	
	print(count)
	count += 1

	try: 
		data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
		data = tuple(data)
		tweets.append(data)

	except tweepy.TweepError as e:
		print(e.reason)
		continue

	except StopIteration:
		break

df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date', 'urls'])

"""Add the path to the folder you want to save the CSV file in as well as what you want the CSV file to be named inside the single quotations"""
df.to_csv(path_or_buf = '/Users/Name/Desktop/FolderName/FileName.csv', index=False) 
