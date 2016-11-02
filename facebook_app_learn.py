#! Python 2.7
# *-* UTF-8 *-*

import json
import urllib2
import facebook
import sqlite3
import facebook
from facepy import GraphAPI

db_loc = 'D:\database\/facebook.db'

# API keys required for OATH
# app_id = '534565370028163'
# app_secret = '35e4b69f395f664ebffa9aafc24884c9'
# client_token = '6fc3696e738ce60b1f87afd827a54ca7'
# # access_token = '1622527554709314|kKlkyrt9HQgOcthBbYA10yoFX6U'
access_token = 'EAAXDriKJZA0IBAC2APJjJBKwCTbcXpzBQrWNsycPEG1fPQ8L1tzZC6YqntqWyjqTxBm9i4ZAQJcTMblSHBh12gZBV42aEgkbPwW8vM0xkRwfdh1TrZCsjm6MSZBOkHVXUIu3cX83iZBNLS5DXnd1aQpdBpB9ZCJdloMZD'
access_token_ = 'access_token='
# graph = GraphAPI(access_token)
graph = facebook.GraphAPI(access_token=access_token, version=2.7)
# cursor = sqlite3.connect(db_loc)
#
# cursor.execute('''CREATE TABLE facebook_page_data post_id BIGINT,
#                                                   ''')

def main():
     # test = graph.get('/sarcasmLOL/?fields=posts{name,message,created_time,comments}')
     message = graph.get_connections(id='1515871602074952_1760873754241401',connection_name='reactions')
     count = 0
     for i in message['data']:

         print i['type']
         if i['type'] == 'LIKE':
             count += 1
         else:
             count += 1
     print count


     # print message['data']
     # # print test['posts']['data']
     # filter_test = json.dumps(test['posts']['data'])
     # #
     # for post in test['posts']['data']:
     #     print post['name']
     #     print post['message']
     #     print post['created_time']
     #     print post['id']
     #     for comment in post['comments']['data']:
     #         print comment['created_time']
     #         #print comment['message']
     #         print comment['id']
     #         for user in comment['from']:
     #             print user['name']
     #             print user['id']

# def main():
#     graph_url = 'https://graph.facebook.com/v2.8/'
#     page_list = ['sarcasmLOL']
#     for page in page_list:
#         # make graph api url with company username
#         current_page = graph_url + page + '/feed?' + access_token_ + access_token
#         print current_page
#
#         # open public page in facebook graph api
#         web_response = urllib2.urlopen(current_page)
#         read_page = web_response.read()
#         fbpage = json.loads(read_page)
#
#         # print page data to console
#         for value in fbpage['data']:
#             fb_story =  value["story"]
#             fb_created_time = value["created_time"]
#             fb_posid = value["id"]
#             print fb_story
#             print fb_created_time
#             print fb_posid
#             print '-------------'
#
#             # #enter the initial values in the database
            # cursor.execute()

# def extract_info_from_postid(postid):




if __name__ == "__main__":
    main()
