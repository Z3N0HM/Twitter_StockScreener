import json
import tweepy

from collections import Counter

import os

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")


        words = {"Python", "python", "code", "snake", "Snake"}    # words to keep counts for
        word_counts = Counter()
        tweet = tweet.text
        lines = tweet.split('\n')





        '''
        counter = 0
        for x in tweet.split():
            if x == words:
                counter += 1
        print(counter)

        '''

        print(lines)
        
        for line in lines:
            print("1")
            tracked_words = [w for word in line.split() if (w:=word.lower()) in words]
            print(line, tracked_words)
            print("2")
            word_counts.update(tracked_words)
            print("3")
            print(*[f'{word}: {word_counts[word]}' for word in set(tracked_words)], sep=', ')
            print("4")
            file_object = open("Count.txt", "w")
            file_object.write(str(line) + str(tracked_words))
            file_object.close()
            

        

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("1NhsRBZ4RsVKuh6C9YLagv5Ir", "e1HfsL3HnyZ6q9PG5JVJNuWfnqKG3Zt22TAEW85JlVTBZZvfDB")
auth.set_access_token("1355553264704450562-QUx3dq4I9WHZbZEznCkSa7J8OZRx4J", "1fgtfW2e8OaiLuVd3HM0qhOF4VYIoqvZNkDLtAG6Bp2jf")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python"], languages=["en"])




words = {'and', 'the', 'in', 'of', 'had', 'is'}    # words to keep counts for
word_counts = Counter()
lines = ['The rabbit and the mole live in the ground',
         'Here is a sentence with the word had in it',
         'Oh, it also had in in it. AND the and is too']

for line in lines:
    tracked_words = [w for word in line.split() if (w:=word.lower()) in words]
    word_counts.update(tracked_words)
    print(*[f'{word}: {word_counts[word]}'
            for word in set(tracked_words)], sep=', ')