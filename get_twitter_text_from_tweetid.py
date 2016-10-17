#! python 2.7
# *-* UTF-8 *-*

from tweepy import OAuthHandler
from tweepy import API
import pyodbc

#pass security information to variables  <-- all the keys should be read from a file and should be removed from the code
consumer_key="7jbj51PhiMzlA50SpM0KTgARB"
consumer_secret="sTjKyEeUojCDG8ja7EY00uk6BwlUavCEzlocgrhoC6NsO8mKsL"
access_key = "155989537-TomVnKsSP49FIICZxIXc98DDqGLbsTCqf0Oh1lJt"
access_secret = "yBXY1XUZ2p1v1537oSboFl0byRXPaKAhUfKIPKdoLZOD4"

#Connection Parameter
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:personaltwitter.database.windows.net;PORT=1433;Database=Personal_TwitterDB;Uid=personaltwitteradmin;Pwd=Personal_Password')
cursor = cnxn.cursor()

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
    tweet_detail = {}
    tweet_detail['tweet_text'] =  results.text
    tweet_detail['user_image'] = results.user.profile_image_url_https
    return tweet_detail

cursor.execute('SELECT TOP 10 tweetid FROM personal_twitter_schema.tweets_data_test ORDER BY user_followers,user_friends DESC')
tweetsids = cursor.fetchall()

print tweetsids
for tweetid in tweetsids:
    id = tweetid.tweetid

    twitter_detail = get_status(id)
    cursor.execute('INSERT INTO personal_twitter_schema.tweets_data_top_tweet'
                   '(tweetid,'
                   'tweet_text,'
                   'tweet_image) VALUES (?,?,?)',id,twitter_detail['tweet_text'],twitter_detail['user_image'])
    cnxn.commit()


#example of invoking the function
#print get_status(786092888044232704)

#tweet_data =  get_status(787639298849845249)
#print tweet_data['tweet_text']

#printing raw data from the tweet
print repr(get_status(787639298849845249))
