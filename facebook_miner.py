#!/usr/bin/env python
# -*-coding:utf-8-*-
# !/usr/bin/env python
# This script requires an existing SQLite DB for output from Facebook Graph API, it should be stored in the same folder of this script if you do not specify the path to DB

"""
Facebook Graph API Explorer (http://developers.facebook.com/tools/explorer)

GO HERE FOR DEFINITIONS OF VARIABLES RETURNED BY API:
https://developers.facebook.com/docs/reference/api/post/

JSON Viewer (http://jsonviewer.stack.hu/)

"""
# import necessary Python libraries
import sys
import urllib
import string
import simplejson
import sqlite3

import time
import datetime
from datetime import datetime, date, time
from pprint import pprint

import sqlalchemy
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import update
from types import *

import re

Base = declarative_base()


###########################
class STATUS(Base):
    __tablename__ = 'entries'  # change table name for your preference.

    id = Column(Integer, primary_key=True)
    org_name = Column(String)  # the name of a Facebook page; useful when you are mining content from multiple pages.
    content_full = Column(String)
    date = Column(String)
    author = Column(String)
    content_new = Column(String)
    date_inserted = Column(DateTime)
    FB_org_id = Column(String)  # Page id, an unique identifier for a Facebook page.
    location = Column(String)
    link = Column(String)  # The URL to a Facebook page post.
    message_id = Column(String)  # Unique identifier for a Facebook page post, formatted as 'Page ID_Message ID'
    org_id = Column(String)  # same as page id
    status_id = Column(String, unique=True)  # Unique identifier for a Facebook page post, without page ID.
    status_link = Column(String)  # same as link
    content = Column(String)  # The textual content of a post
    published_date = Column(String)  # When a Facebook page post is sent.
    date_inserted = Column(
        DateTime)  # When a post is retrieved and stored on your SQLite database. Literally, the time of your data-mining.
    last_comment = Column(String)
    type = Column(String)  # The type of post – status, link, photo, video, etc.
    status_type = Column(String)  # More detailed status post type  (e.g. mobile_status_update, added_photo)
    video_source = Column(String)  # Included URL to a video
    picture_link = Column(String)  # The name of the webpage that the included URL is linking to.
    link_name = Column(String)
    link_caption = Column(String)
    link_description = Column(String)  # Description of the webpage that the included URL is linking to.
    num_mentions = Column(Integer)  # The number of mentions in a post.
    mentions = Column(String)  # The mentioned page/people in a post.
    num_likes = Column(Integer)
    like_count = Column(Integer)
    comment_count = Column(Integer)
    share_count = Column(Integer)
    hashtag_count = Column(Integer)
    hashtags = Column(String)
    mentions_count = Column(Integer)
    actions = Column(String)
    application = Column(String)
    properties = Column(String)
    message_output = Column(
        String)  # The entire JSON raw output, including information not parsed to the existing columns.
    time_since_post_days = Column(String)
    like_count_7days = Column(Integer)
    comment_count_7days = Column(Integer)
    share_count_7days = Column(Integer)
    time_since_post_14days = Column(Integer)
    like_count_14days = Column(Integer)
    comment_count_14days = Column(Integer)
    share_count_14days = Column(Integer)
    images = Column(Integer)
    urls_count = Column(Integer)
    urls_count_true = Column(Integer)
    first_page_comment = Column(String)  # Comments (including sender, content and posted time) on the first page.
    comments_beyond_pageone = Column(String)  # Comments on the second page and beyond.

    def __init__(self, id, org_name, FB_org_id, content_full, date, author, content_new, location, link, message_id,
                 org_id, status_id, status_link,
                 content, published_date, date_inserted, last_comment, type, status_type, video_source, picture_link,
                 link_name, link_caption, link_description, num_mentions, mentions, num_likes, like_count,
                 comment_count, share_count, hashtag_count, hashtags, mentions_count,
                 actions, application, properties, message_output,
                 time_since_post_days, like_count_7days, comment_count_7days, share_count_7days,
                 time_since_post_14days, like_count_14days, comment_count_14days, share_count_14days,
                 images, urls_count, urls_count_true, first_page_comment, comments_beyond_pageone,
                 ):
        self.org_name = org_name
        self.FB_org_id = FB_org_id
        self.location = location
        self.link = link
        self.message_id = message_id
        self.org_id = org_id
        self.content_full = content_full  # added for reaction count
        self.date = date  # added for reaction count
        self.author = author  # added for reaction count
        self.content_new = content_new  # added for reaction count
        self.date_inserted = date_inserted  # added for reaction count
        self.status_id = status_id
        self.status_link = status_link
        self.content = content
        self.published_date = published_date
        self.date_inserted = date_inserted
        self.last_comment = last_comment
        self.type = type
        self.status_type = status_type
        self.video_source = video_source
        self.picture_link = picture_link
        self.link_name = link_name
        self.link_caption = link_caption
        self.link_description = link_description
        self.num_mentions = num_mentions
        self.mentions = mentions
        self.num_likes = num_likes
        self.like_count = like_count
        self.comment_count = comment_count
        self.share_count = share_count
        self.hashtag_count = hashtag_count
        self.hashtags = hashtags
        self.mentions_count = mentions_count
        self.actions = actions
        self.application = application
        self.properties = properties
        self.message_output = message_output
        self.time_since_post_days = time_since_post_days
        self.like_count_7days = like_count_7days
        self.comment_count_7days = comment_count_7days
        self.share_count_7days = share_count_7days
        self.time_since_post_14days = time_since_post_14days
        self.like_count_14days = like_count_14days
        self.comment_count_14days = comment_count_14days
        self.share_count_14days = share_count_14days
        self.images = images
        self.urls_count = urls_count
        self.urls_count_true = urls_count_true
        self.first_page_comment = first_page_comment  # added for comments on page 1
        self.comments_beyond_pageone = comments_beyond_pageone  # added for comments beyond page 1

    def __repr__(self):
        return "<Organization, Sender('%s', '%s')>" % (self.id, self.link)


url = "https://graph.facebook.com/%s/posts?access_token=EAAXDriKJZA0IBAC2APJjJBKwCTbcXpzBQrWNsycPEG1fPQ8L1tzZC6YqntqWyjqTxBm9i4ZAQJcTMblSHBh12gZBV42aEgkbPwW8vM0xkRwfdh1TrZCsjm6MSZBOkHVXUIu3cX83iZBNLS5DXnd1aQpdBpB9ZCJdloMZD&include_hidden=true"  # paste your own access token here.


def get_data(kid):
    try:
        d = simplejson.loads(urllib.urlopen(url % (kid)).read())
    except Exception, e:
        print "Error reading id %s, exception: %s" % (kid, e)
        return None
    print "d.keys(): ", d.keys()
    return d


def write_data(self, d):
    date_inserted = datetime.now()
    messages = d['data']
    number_on_page = len(messages)
    print "NUMBER OF MESSAGES IN THIS SET OF RESULTS:", len(messages)

    for message in d['data']:
        message_output = str(message)

        if 'from' in message:
            org_name = message['from']['name']
            FB_org_id = message['from']['id']
        else:
             org_name   = ''
             FB_org_id  = ''

        if 'place' in message:
            location = str(message['place'])
        else:
            location = ''

        if 'actions' in message:
            actions = str(message['actions'])
        else:
            actions = ''

        if 'link' in message:
            link = message['link']
        else:
            link = ''

        if 'name' in message:
            link_name = message['name']
        else:
            link_name = ''

        if 'caption' in message:
            link_caption = message['caption']
        else:
            link_caption = ''

        if 'description' in message:
            link_description = message['description']
        else:
            link_description = ''

        if 'shares' in message:
            num_shares = message['shares']['count']

        if 'message' in message:
            content = message['message']
            content = content.replace('\n', '')
        else:
            content = ''

        last_comment = message['updated_time']

        published_date = message['created_time']
        type = message['type']
        message_id = message['id']
        org_id = message_id.split('_')[0]
        status_id = message_id.split('_')[1]

        status_link = 'https://www.facebook.com/%s/posts/%s' % (org_id, status_id)

        if 'status_type' in message:
            status_type = message['status_type']
        else:
            status_type = ''

        if 'properties' in message:
            properties = str(message['properties'])
        else:
            properties = ''

        if 'application' in message:
            application = str(message['application'])
        else:
            application = ''

        if 'picture' in message:
            picture_link = message['picture']
        else:
            picture_link = ''

        if 'source' in message:
            video_source = message['source']
        else:
            video_source = ''

        first_page_comment = []
        comments_beyond_pageone = []

        if 'comments' in message:
            user_comment_onepage = []  # temporary for comments on page 1.
            for each_comment in message['comments']['data']:
                comment = each_comment['message']
                user_comment_onepage.append(comment)
                first_page_comment = user_comment_onepage

                user_comment_morepages = []  # temporary for comments beyond page 1.

                if 'next' in message['comments']['paging']:
                    next_comment_url = message['comments']['paging']['next']

                    if next_comment_url:
                        count = 2
                        while count < 80:
                            try:
                                get_more_comment = simplejson.loads(urllib.urlopen(next_comment_url).read())
                                for more_comments in get_more_comment['data']:
                                    comment_plus = more_comments['message']
                                    user_comment_morepages.append(comment_plus)
                            except Exception, e:
                                print "Error reading"
                                break

                            if not 'data' in get_more_comment:
                                print "ok, move on"
                                continue

                            if len(get_more_comment['data']) == 0:
                                print "ok, move on"
                                continue
                            if 'paging' in get_more_comment:
                                if 'next' in get_more_comment['paging']:
                                    next_comment_url = get_more_comment['paging']['next']
                                    print "ok"
                                else:
                                    print "okay move on"
                                    print "ok"
                                    break

                            count += 1
                            if count > 50:
                                print "WE'RE AT PAGE 50!!!!!"
                                break

                        comments_beyond_pageone = user_comment_morepages
                    else:
                        first_page_comment = user_comment_onepage

        first_page_comment = string.join(first_page_comment, u"***")
        comments_beyond_pageone = string.join(comments_beyond_pageone, u"***")
        # Comments script ends
        mentions_list = []
        num_mentions = 0
        if 'to' in message:
            num_mentions = len(message['to']['data'])
            if num_mentions != 0:
                mentions_list = [i['name'] for i in message['to']['data'] if 'name' in i]
            else:
                mentions_list = ''
            mentions = ', '.join(mentions_list)
        else:
            mentions = ''

        upd = STATUS(None, org_name, FB_org_id, None, None, None, None, location, link, message_id, org_id, status_id,
                     status_link,
                     content, published_date, date_inserted, last_comment, type, status_type, video_source,
                     picture_link,
                     link_name, link_caption, link_description, num_mentions, mentions, None, None, None, None, None,
                     None, None, actions, application, properties, message_output,
                     None, None, None, None, None, None, None, None, None, None, None, first_page_comment,
                     comments_beyond_pageone,
                     )

        self.session.add(upd)
        try:
            self.session.commit()
        except exc.SQLAlchemyError:
            self.session.rollback()
            print "     NOT INSERTING --> IT'S A DUPLICATE"


class Scrape:
    def __init__(self):
        engine = sqlalchemy.create_engine("sqlite:///curiositybits_testing.sqlite",
                                          echo=False)  # enter your database name here and its file path.

        Session = sessionmaker(bind=engine)

        self.session = Session()
        Base.metadata.create_all(engine)

    def main(self):

        keys = []
        ids = ['6096008671']  # if a page name contains multiple words, separated by space (e.g. SPOT Coffee); it will show up as words connected by hyphens in URL. For example, SPOT Cofee as in "Spot-Coffee-Elmwood." If so, it is recommended that you use page id. You can find page id in the URL - it is the string of numbers after page name in URL.  (e.g. https://www.facebook.com/pages/Spot-Coffee-Elmwood/316579834919)
        for feed in ids:
            kid = feed
            d = get_data(kid)

            if not d:
                print "THERE WAS NO 'D' RETURNED........MOVING TO NEXT ID"
                continue  ##### RETURN TO THE BEGINNING OF THE LOOP
            if not "data" in d:
                print "THERE WAS NO 'D['DATA']' RETURNED........MOVING TO NEXT ID"  #
                continue  ##### RETURN TO THE BEGINNING OF THE LOOP
            if len(d['data']) == 0:
                print "THERE WERE NO STATUSES RETURNED........MOVING TO NEXT ID"
                continue  ##### RETURN TO THE BEGINNING OF THE LOOP

            write_data(self, d)

            self.session.commit()

            paging = d['paging']

            if 'next' in paging:
                next_page_url = paging['next']
                print "HERE IS THE NEXT PAGE URL:", next_page_url
            else:
                print "THERE AIN'T NO NEXT PAGE FOR", feed_id

            if next_page_url:
                print "THERE WERE STATUSES ON THE FIRST PAGE! NOW MOVING TO GRAB EARLIER POSTS"
                count = 2
                while count < 100:
                    print "------XXXXXX------ STARTING PAGE", count
                    try:
                        d = simplejson.loads(urllib.urlopen(next_page_url).read())
                    except Exception, e:
                        print "Error reading id %s, exception: %s" % (kid, e)
                        break
                    print "d.keys(): ", d.keys()  ##### d.keys():  [u'paging', u'data'] NEW KEYS IN UPDATED API FOR TWYTHON
                    if not d:
                        print "THERE WERE NO STATUSES RETURNED........MOVING TO NEXT ID"
                        # continue	##### RETURN TO THE BEGINNING OF THE WHILE LOOP
                        break
                    if not 'data' in d:
                        print "THERE WERE NO STATUSES RETURNED........MOVING TO NEXT ID"
                        print d
                        break  ##### STOP CURRENT WHILE LOOP AND GO TO NEXT STATEMENT
                    if len(d['data']) == 0:
                        print "THERE WERE NO STATUSES RETURNED........MOVING TO NEXT ID"
                        print d
                        break  ##### STOP CURRENT WHILE LOOP AND GO TO NEXT STATEMENT
                    write_data(self, d)
                    self.session.commit()

                    print "------XXXXXX------ FINISHED WITH PAGE", count

                    if 'paging' in d:
                        if 'next' in d['paging']:
                            next_page_url = d['paging']['next']
                            print "AND HERE IS THE NEXT PAGE URL:", next_page_url
                        else:
                            print "THERE AIN'T NO NEXT PAGE FOR", feed_id
                            print "--------------> WE'VE REACHED THE LAST PAGE!!!! MOVING TO NEXT ID"
                            break
                    count += 1
                    if count > 100:
                        print "WE'RE AT PAGE 50!!!!!"
                        break

            else:
                print "THERE AIN'T NO NEXT_PAGE_URL FOR FEED_ID", feed_id, " ---- GOING ON TO NEXT ID"

            self.session.commit()

        self.session.close()


if __name__ == "__main__":
    s = Scrape()
    s.main()
