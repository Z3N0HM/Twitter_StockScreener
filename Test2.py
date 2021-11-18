from collections import Counter

import json
import tweepy


class MySteamListener(tweepy.StreamListener):
    print("1") ###Takes this area first
    def __init__(self, api):
        print("2")
        self.api = api
        print("3")
        self.me = api.me()
        print("4")
        
    def on_status(self, tweet, word_counts = Counter() ):
        
        lines = tweet.text.split('\n')

 
        
        
        for line in lines:
            print("5")
            words = {"Python", "python", "code", "snake", "Snake"}    # words to keep counts for
            print("6")
            print("7")
            tweets = tweet.text
            
            print("8")
            tracked_words = [word for word in line.lower().split() if word in words]
            
            print("9")
            print("10")
            #print(line, tracked_words)
            print("11")
            word_counts.update(tracked_words)
            print("12")
            #print(tweets)
            print(*[f'{word}: {word_counts[word]}' for word in set(tracked_words)], sep=', ')
            print("13")
    

    def on_error(self, status):
        if status == 420:
            sys.stderr.write('Enhance Your Calm; The App Is Being Rate Limited For Making Too Many Requests')
            return True
        else:
            sys.stderr.write('Error {}n'.format(status))
            return True

###This area 2nd

# Authenticate to Twitter
print("14")
auth = tweepy.OAuthHandler("1NhsRBZ4RsVKuh6C9YLagv5Ir", "e1HfsL3HnyZ6q9PG5JVJNuWfnqKG3Zt22TAEW85JlVTBZZvfDB")
auth.set_access_token("1355553264704450562-QUx3dq4I9WHZbZEznCkSa7J8OZRx4J", "1fgtfW2e8OaiLuVd3HM0qhOF4VYIoqvZNkDLtAG6Bp2jf")
print("15")
#Bearer token AAAAAAAAAAAAAAAAAAAAAIB5MQEAAAAAmE3JXHjCJpAoteigsmQ3Ez1UazM%3DceeWRyXdT7f7Uc5vzAN6XVxxMgiRcNCoJQkd8CU337wUxcoNrt

print("16")


print("17")


try:
    api.verify_credentials()
    print("Authentication OK")  #3rd
    print("18")
except:
    print("Error during authentication")
    print("19")


# Create API object


print("20")
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

print("21")  #Goes to 2, 3, 4, 22
tweets_listener = MySteamListener(api)
print("22")
stream = tweepy.Stream(api.auth, tweets_listener)
print("23")
stream.filter(track=["Python"], languages=["en"])
print("24")