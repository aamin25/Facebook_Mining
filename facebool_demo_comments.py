#!C:/Python2.7 python
# -*- coding: utf-8 -*-

import sqlite3
import requests
import datetime
import exceptions
import facebook as fb
import dateutil.parser as dateparser
from sentiment_analysis_textblob import custom_sentiment_analysis


# access token for facebook graphAPI
access_token = 'EAAXDriKJZA0IBAC2APJjJBKwCTbcXpzBQrWNsycPEG1fPQ8L1tzZC6YqntqWyjqTxBm9i4ZAQJcTMblSHB' \
               'h12gZBV42aEgkbPwW8vM0xkRwfdh1TrZCsjm6MSZBOkHVXUIu3cX83iZBNLS5DXnd1aQpdBpB9ZCJdloMZD'

# Location of database -- Create the file name dummy file with this file name
cursor = sqlite3.connect('test.db')

# Graph API
graph = fb.GraphAPI(access_token=access_token, version=2.7)

# Post id for testing
# posts_key_id = '10203169968306663_10207864129697764'
posts_key_id = '6096008671_10154562240788672'

# Api Object testing
# api_output = graph.get_object(id=posts_key_id, fields='comments{id,user_likes,message_tags,message,from,created_time,comment_count}')
# print api_output['comments']

def get_next_page(url):
    return requests.get(url).json()

def whatisthis(s,value):
    if isinstance(s, str):
        pass
        # print "ordinary string: " , value
    elif isinstance(s, unicode):
        pass
        # print "unicode string: " , value
    else:
        print "not a string"

def get_fb_post_comments(posts):
    comment_mine_count = 0
    page_mine_count = 0

    # message_tags_name = []
    # message_tags_id= []

    api_output = graph.get_object(id=posts,
                                  fields='comments{id,user_likes,message_tags,message,from,created_time,comment_count}')

    if 'comments' in api_output:
        while(True):
            try:
                if 'comments' in api_output:
                    if len(api_output['comments']['data']) > 0:
                        for comment in api_output['comments']['data']:

                            if 'id' in comment:
                                id = comment['id']
                                print 'id ',id
                            else:
                                id = ''

                            if 'comment_count' in comment:
                                comment_count = comment['comment_count']
                                print 'comment_count ',comment_count
                            else:
                                comment_count = ''

                            if 'from' in comment:
                                from_name = comment['from']['name']
                                from_id = comment['from']['id']
                                print 'from_name ',from_name
                                print 'from_id ',from_id
                            else:
                                from_name = ''
                                from_id = ''

                            #handle created_time
                            if 'created_time' in comment:
                                created_time = dateparser.parse(comment['created_time'], ignoretz=True)
                                print 'created_time ',created_time
                            else:
                                created_time = ''

                            if 'user_likes' in comment:
                                user_likes = comment['user_likes']
                                print 'user_like ',user_likes
                            else:
                                user_likes = ''

                            # write logic to handle multiple user_tags
                            if 'message_tags' in comment:
                                message_tags_name = comment['message_tags'][0]['name']
                                message_tags_id = comment['message_tags'][0]['id']
                            else:
                                message_tags_name = ''
                                message_tags_id = ''

                            if 'message' in comment:
                                message = comment['message']
                            else:
                                message = comment['message']

                            # Handle with fetching the data from page info database
                            page_name = 'Lionbridge'

                            post_id = posts_key_id
                            sentiment_value = custom_sentiment_analysis(message)
                            sentiment_score = sentiment_value[0]
                            sentiment_mean = sentiment_value[1]
                            inserted_time = datetime.datetime.now()

                            cursor.execute('''insert into comments_data (id, post_id, message, comment_count, from_name, from_id, message_tags_id, message_tags_name, created_time, user_likes, sentiment_score, sentiment_mean, data_inserted) values (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(id,post_id,message,comment_count,from_name,from_id,message_tags_id,message_tags_name,created_time,user_likes,sentiment_score,sentiment_mean,inserted_time))

                            try:
                                cursor.commit()
                            except exceptions as e:
                                print 'INSERT ERROR: ',e

                            comment_mine_count += 1

                        page_mine_count += 1
                        next_url = api_output['comments']['paging']['next']
                        api_output.clear()
                        api_output['comments'] = get_next_page(next_url)

                    else:
                        raise KeyError

            except KeyError:
                # print 'All Comments Extracted!!!'
                # print 'comment_mine_count: ' , comment_mine_count
                # print 'page_mine-count: ', page_mine_count
                break


if __name__ == '__main__':
    row_count = 0
    for row in cursor.execute('''select id from posts_data'''):
        print 'Processing Post: ', row[0]
        get_fb_post_comments(row[0])
        row_count = row_count + 1
        # print 'Post Processed: ', row[0]
        print 'Row_Count: ',row_count

     # get_fb_post_comments('6096008671_10152797499983672')
