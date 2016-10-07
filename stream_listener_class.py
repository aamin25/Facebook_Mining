# Stream Listener class
import tweepy
import sys

#pass security information to variables
consumer_key="7jbj51PhiMzlA50SpM0KTgARB"
consumer_secret="sTjKyEeUojCDG8ja7EY00uk6BwlUavCEzlocgrhoC6NsO8mKsL"
access_key = "155989537-TomVnKsSP49FIICZxIXc98DDqGLbsTCqf0Oh1lJt"
access_secret = "yBXY1XUZ2p1v1537oSboFl0byRXPaKAhUfKIPKdoLZOD4"

#filter the tweets on the basis of below filter
#filter_words = "Enter the words that you want to filter your tweets on"
filter_words = '#iphone7'

#use variables to access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#create an object called 'customStreamListener'

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        #count = 0
        count = 0
        #while count < 10:
        while count < 1:
            #print (status.author.screen_name, status.created_at, status.text)
            print status
            count += 1


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# open the stream using auth validation and Custom Stream Listener
streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())

# filter the stream based on the string mentioned below
filterd_tweets_json = streamingAPI.filter(track=[filter_words])
