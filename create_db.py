#! -*-python2.7-*-
# -*- utf-8 -*-
import sqlite3

# Location of database file
db_loc = 'C:\db_files\/test.db'

# Initiate database connection
cursor = sqlite3.connect(db_loc)

def create_twitter_db ():
    """
    Function : Create table for creating database for top ten tweets.
    Param : NONE.
    Return : NONE.
    Dependencies : sqlite3.
    """
    # Create tablet for twitter database.
    cursor.execute('CREATE TABLE IF NOT EXISTS twitter_data (tweetid BIGINT,'
                                              'retweet TEXT,'
                                              'username TEXT,'
                                              'favorited TEXT,'
                                              'user_followers BIGINT,'
                                              'user_friends BIGINT,'
                                              'retweet_count BIGINT,'
                                              'sentiment_score INT(02),'
                                              'sentiment_mean TEXT,'
                                              'timestamp DATETIME)')

    # Commit the changes in the database
    cursor.commit()

def create_top10_db ():
    """
    Function : Create table for creating database for top ten tweets.
    Param : NONE.
    Return : NONE.
    Dependencies : sqlite3.
    """
    cursor.execute('CREATE TABLE IF NOT EXISTS top_ten_tweets (tweetid BIGINT,'
                                                'tweet_text TEXT(140),'
                                                'tweet_image TEXT,'
                                                'tweet_url VARCHAR(512))')

    # Commit the changes in the database
    cursor.commit()

if __name__ == '__main__':
    create_twitter_db()
    create_top10_db()
