#! python 2.7
# *-* UTF-8 *-*

from tweepy import OAuthHandler
from tweepy import API

#pass security information to variables  <-- all the keys should be read from a file and should be removed from the code
consumer_key="7jbj51PhiMzlA50SpM0KTgARB"
consumer_secret="sTjKyEeUojCDG8ja7EY00uk6BwlUavCEzlocgrhoC6NsO8mKsL"
access_key = "155989537-TomVnKsSP49FIICZxIXc98DDqGLbsTCqf0Oh1lJt"
access_secret = "yBXY1XUZ2p1v1537oSboFl0byRXPaKAhUfKIPKdoLZOD4"

#use variables to access twitter
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

#conect to search api usig the auth
api = API(auth)

def get_status(tweetid):
    '''
    Function: Uses the search api of twitter to return the tweet text using the tweetid of the post.

    Param text: When calling pass the tweet id thru the function.

    Return: Returns the tweet text as string value. 

    Dependencies: tweepy
    '''
    results = api.get_status(tweetid)
    return results.text

#example of invoking the function
print get_status(786092888044232704)
