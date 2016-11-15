#!C:/Python2.7 python
# -*- coding: utf-8 -*-

import sqlite3
import requests
import datetime
import exceptions
import facebook as fb
import dateutil.parser as dateparser
from sentiment_analysis_textblob import custom_sentiment_analysis

# Location of database -- Create the file name dummy file with this file name
db_path = 'sqlite:///test.db'

# access token for facebook graphAPI
access_token = 'Enter Your Facebook Access Token'

# Location of database  <-- Currently on the root directory of the progaram
cursor = sqlite3.connect('test.db')

graph = fb.GraphAPI(access_token=access_token, version=2.7)

key = 'L10nbridge'

def get_fb_posts(page):
	
	# Count variables for reporting purposes
	post_count = 0
    page_count = 0

	api_output = graph.get_object(id=key+'/feed',fields='id,message,created_time,from,message_tags,status_type,name,updated_time')

	while(True):
		try:
			if (len(api_output['data']) > 0):

				for post in api_output['data']:

					if 'id' in post:
						id = post['id']
					else:
						raise KeyError('Error while get_post_data')

					if 'message' in post:
						message = post['message']
					else:
						message = ''

					if 'created_time' in post:
						created_time = dateparser.parse(post['created_time'], ignoretz=True)
					else:
						created_time = ''

					if 'from' in post:
						post_from_name = post['from']['name']
						post_from_id = post['from']['id']
					else:
						post_from_name = ''
						post_from_id = ''

					if 'message_tags' in post:
						message_tags_name = post['message_tags'][0]['name']
						message_tags_id = post['message_tags'][0]['id']
					else:
						message_tags_name = ''
						message_tags_id = ''

					if 'status_type' in post:
						status_type = post['status_type']
					else:
						status_type = ''

					if 'name' in post:
						name = post['name']
					else:
						name = ''

					if 'updated_time' in post:
						updated_time = dateparser.parse(post['updated_time'], ignoretz=True)
					else:
						updated_time = ''

					# Calculate the sentiment score of the Post
					sentiment_value = custom_sentiment_analysis(message)
					sentiment_score = sentiment_value[0]_
					sentiment_mean= sentiment_value[1]
					inserted_time = datetime.datetime.now()

					page_name = page

					cursor.execute('''insert into posts_data (id, message, created_time, posted_from_name, posted_from_id, status_type, page_name, name, date_updated, message_tags_id, message_tags_name, post_sentiment_score, post_sentiment_mean,data_inserted) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(id, message, created_time, post_from_name, post_from_id, status_type, page_name, name, updated_time, message_tags_id, message_tags_name, sentiment_score, sentiment_mean, inserted_time))

					try:
						cursor.commit()
					except exceptions as e:
						print 'insert error' , e

					post_count += 1
					print 'Post Count: ', post_count

				page_count += 1
				api_output = get_next_page(api_output['paging']['next'])

			else:
				raise KeyError

		except KeyError:
			print 'All Posts Extracted!!!'
			print 'post-count: ', post_count
			print 'page-count: ', page_count
			break

# Function returns call the next facebook using pagination cursor.
def get_next_page(url):
    return requests.get(url).json()

# Function checks for encoding of text.  <-- for testing purposes
def whatisthis(s,value):
    if isinstance(s, str):
        pass
        # print "ordinary string: " , value
    elif isinstance(s, unicode):
        pass
        # print "unicode string: " , value
    else:
        print "not a string"

if __name__ == '__main__':
	get_fb_posts(key)
	
