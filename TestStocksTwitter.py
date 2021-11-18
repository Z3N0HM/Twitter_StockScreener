
import json
import tweepy

from flask import Flask

from list import *

app = Flask(__name__)

class MySteamListener(tweepy.StreamListener):
    
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        #print(f"\033[1;34;m{tweet.user.name} \033[1;33;m--- \033[1;36;m{tweet.text}")
        global count
        print(str(stock) + " = " + str(count))
        count +=1 
        
    def on_error(self, status):
        print("Error Detected")



# Authenticate to Twitter

auth = tweepy.OAuthHandler("1NhsRBZ4RsVKuh6C9YLagv5Ir", "e1HfsL3HnyZ6q9PG5JVJNuWfnqKG3Zt22TAEW85JlVTBZZvfDB")
auth.set_access_token("1355553264704450562-QUx3dq4I9WHZbZEznCkSa7J8OZRx4J", "1fgtfW2e8OaiLuVd3HM0qhOF4VYIoqvZNkDLtAG6Bp2jf")

#Bearer token AAAAAAAAAAAAAAAAAAAAAIB5MQEAAAAAmE3JXHjCJpAoteigsmQ3Ez1UazM%3DceeWRyXdT7f7Uc5vzAN6XVxxMgiRcNCoJQkd8CU337wUxcoNrt


#Stocks
# - Make it possibel to have several stocks
stock = ("GME")
global count
count = 1
#Auth Verification 

try:
    api.verify_credentials()
    print("Authentication OK")

except:
    print("Error during authentication")
    


# Create API object



api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


tweets_listener = MySteamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

stream.filter(track=[stock], languages=["en"])


#Print +1 to Stock name if tweeted about
