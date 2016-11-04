#!/usr/bin/env python
# -*-coding:utf-8-*-
# !/usr/bin/env python
# This script requires an existing SQLite DB for output from Facebook Graph API, it should be stored in the same folder of this script if you do not specify the path to DB

import sys
import string
import simplejson
import sqlite3

from pprint import pprint

import sqlalchemy
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from types import *
from time import strptime
from datetime import datetime, date, time

import csv
import re

from sqlalchemy import update

import urllib2
from BeautifulSoup import BeautifulSoup

import \
    dateutil.parser as dateparser  # This is for converting ISO-8601 formatted date information (returned by Facebook Graph API) https://developers.facebook.com/docs/reference/api/dates/

Base = declarative_base()


###########################
class STATUS(Base):
    __tablename__ = 'entries'  # the table name should correspond to the existing table for Facebook Graph API output
    # All following columns need to existant already in the DB, for any tables called in the script, you need to define here.
    id = Column(Integer, primary_key=True)
    feed_id = Column(Integer)  # NEW VARIABLE, MANUALLY DEFINE THE COLUMN IN SQLITE DATABASE BROWSER
    content = Column(String)
    status_link = Column(String)  #
    content_full = Column(String)
    link = Column(String)
    date = Column(String)
    author = Column(String)
    content_new = Column(String)
    like_count = Column(Integer)
    date_inserted = Column(DateTime)
    comment_count = Column(Integer)
    share_count = Column(Integer)
    published_date = Column(String)
    time_since_post_days = Column(String)
    like_count_7days = Column(Integer)
    comment_count_7days = Column(Integer)
    share_count_7days = Column(Integer)
    time_since_post_14days = Column(String)
    like_count_14days = Column(Integer)
    comment_count_14days = Column(Integer)
    share_count_14days = Column(Integer)
    last_comment = Column(String)
    content_cycle = Column(String)  # NEW VARIABLE, MANUALLY DEFINE THE COLUMN IN SQLITE DATABASE BROWSER
    content_cycle_new = Column(String)  # NEW VARIABLE, MANUALLY DEFINE THE COLUMN IN SQLITE DATABASE BROWSER

    def __init__(self, id, feed_id, last_comment, date_inserted, content, status_link, content_full, link, date, author,
                 content_new, like_count, comment_count, share_count, published_date,
                 time_since_post_14days, like_count_14days, comment_count_14days, share_count_14days, content_cycle,
                 content_cycle_new,
                 ):
        self.feed_id = feed_id
        self.content = content
        self.content_full = content_full
        self.status_link = status_link
        self.link = link
        self.date = date
        self.author = author
        self.content_new = content_new
        self.like_count = like_count
        self.comment_count = comment_count
        self.date_inserted = date_inserted
        self.share_count = share_count
        self.published_date = published_date
        self.time_since_post_days = time_since_post_days
        self.like_count_7days = like_count_7days
        self.comment_count_7days = comment_count_7days
        self.share_count_7days = share_count_7days
        self.time_since_post_14days = time_since_post_14days
        self.like_count_14days = like_count_14days
        self.comment_count_14days = comment_count_14days
        self.share_count_14days = share_count_14days
        self.content_cycle = content_cycle
        self.last_comment = last_comment
        self.content_cycle_new = content_cycle_new

    def __repr__(self):
        return "<Organization, Sender('%s', '%s')>" % (self.id, self.link)


engine = sqlalchemy.create_engine("sqlite:///PASTE YOUR OWN SQLITE DATABASE NAME HERE.sqlite", echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

all_statuses = session.query(STATUS).all()

# for row in all_statuses[9400:9500]:
for row in all_statuses:

    url = row.status_link
    posted_date = row.published_date
    last_user_comment = row.last_comment
    posted_date_new = dateparser.parse(posted_date, ignoretz=True)
    posted_date_object = datetime.strptime(str(posted_date_new), '%Y-%m-%d %H:%M:%S')  # % posted_date
    last_user_comment_new = dateparser.parse(row.last_comment, ignoretz=True)
    last_user_comment_new_object = datetime.strptime(str(last_user_comment_new), '%Y-%m-%d %H:%M:%S')
    content_cycle = last_user_comment_new_object - posted_date_object

    time_since_post = datetime.now() - posted_date_object
    row.time_since_post_days = time_since_post.days
    content_cycle_day = content_cycle.days
    content_cycle_hr = (content_cycle.seconds / (3600))
    content_cycle_input = content_cycle_day * 24 + content_cycle_hr

    time_since_post_day = time_since_post.days
    time_since_post_hr = (time_since_post.seconds / (3600))
    time_since_post_input = time_since_post_day * 24 + time_since_post_hr
    row.content_cycle_new = content_cycle_input / time_since_post_input

    row.content_cycle = content_cycle_input

    id = row.id
    if time_since_post.days > 7 and not row.like_count_7days:
        print "WILL TRY TO INSERT SOME DATA NOW..........", "looking at row: ", id
        request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)

        except urllib2.HTTPError as e:
            print e.code
            continue
        soup = BeautifulSoup(response)
        test = soup.find('span', {'class': 'userContent'})
        if test:
            content = soup.findAll('span', {'class': 'userContent'})[0].string
            if content:
                content_new = content.replace('&#x27;', "'").replace('&amp;', "&").replace('&quot;', "'").replace(
                    '&amp', "&")
                content_new = content_new.replace('[', "(").replace(']', ")")
                row.content_new = content_new
            else:
                content = soup.find('span', {'class': 'userContent'})
                if content:
                    content_new2 = content.findAll(text=True)
                    content_new3 = " ".join(content_new2)
                    content_new3 = content_new3.replace('&#x27;', "'").replace('&amp;', "&").replace('&quot;',
                                                                                                     "'").replace(
                        '&amp', "&")
                    content_new3 = content_new3.replace('[', "(").replace(']', ")")
                    row.content_new = content_new3

        wilma = soup.findAll(text=re.compile("commentcount"))
        if wilma:
            bob = soup.findAll(text=re.compile("commentcount"))[0].string
            fred = bob.lower()
            splitcommas = fred.split(",")

            likecount = []
            sharecount = []
            commentcount = []
            for word in splitcommas:
                if word.startswith('"likecount"'):  # problem - two 'likecounts'
                    likecount.append(word)
                if word.startswith('"commentcount"'):  # problem - two 'likecounts'
                    commentcount.append(word)
                if word.startswith('"sharecount"'):  # problem - two 'likecounts'
                    sharecount.append(word)
            likecountX = likecount[0]
            likecountY = likecountX.split(':')
            likecount = likecountY[1]
            print likecount
            row.like_count_7days = likecount  ### NEW VARIABLE

            sharecountX = sharecount[0]
            sharecountY = sharecountX.split(':')
            sharecount = sharecountY[1]
            print sharecount
            row.share_count_7days = sharecount  ### NEW VARIABLE

            commentcountX = commentcount[0]
            commentcountY = commentcountX.split(':')
            commentcount = commentcountY[1]
            print commentcount
            row.comment_count_7days = commentcount  ### NEW VARIABLE
        session.commit()
    else:
        print "time_since_post_days <7 OR COUNTS ALREADY INSERTED"

session.close()



