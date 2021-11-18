from collections import Counter

import json
import tweepy


class MySteamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet, word_counts = Counter() ):
        
        lines = tweet.text.split('\n')

 
        
        
        for line in lines:
            words = {"Python", "python", "code", "snake", "Snake"}    # words to keep counts for
            tweets = tweet.text
            print(tweet.text)
            tracked_words = [word for word in line.split() if word in words]
            word_counts.update(tracked_words)      
            print(*[f'{word}: {word_counts[word]}' for word in set(tracked_words)], sep=', ')
    

    def on_error(self, status):
        if status == 420:
            sys.stderr.write('Enhance Your Calm; The App Is Being Rate Limited For Making Too Many Requests')
            return True
        else:
            sys.stderr.write('Error {}n'.format(status))
            return True

###This area 2nd

# Authenticate to Twitter

auth = tweepy.OAuthHandler("1NhsRBZ4RsVKuh6C9YLagv5Ir", "e1HfsL3HnyZ6q9PG5JVJNuWfnqKG3Zt22TAEW85JlVTBZZvfDB")
auth.set_access_token("1355553264704450562-QUx3dq4I9WHZbZEznCkSa7J8OZRx4J", "1fgtfW2e8OaiLuVd3HM0qhOF4VYIoqvZNkDLtAG6Bp2jf")

#Bearer token AAAAAAAAAAAAAAAAAAAAAIB5MQEAAAAAmE3JXHjCJpAoteigsmQ3Ez1UazM%3DceeWRyXdT7f7Uc5vzAN6XVxxMgiRcNCoJQkd8CU337wUxcoNrt


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

stream.filter(track=["Python"], languages=["en"])
