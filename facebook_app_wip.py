#! Python 2.7
# *-* UTF-8 *-*

import simplejson
import urllib2
import json
import facebook
import requests
# from facepy import GraphAPI

# API keys required for OATH
app_id = '534565370028163'
app_secret = '35e4b69f395f664ebffa9aafc24884c9'
client_token = '6fc3696e738ce60b1f87afd827a54ca7'
#access_token = '1622527554709314|kKlkyrt9HQgOcthBbYA10yoFX6U'
access_token = 'EAAXDriKJZA0IBAC2APJjJBKwCTbcXpzBQrWNsycPEG1fPQ8L1tzZC6YqntqWyjqTxBm9i4ZAQJcTMblSHBh12gZBV42aEgkbPwW8vM0xkRwfdh1TrZCsjm6MSZBOkHVXUIu3cX83iZBNLS5DXnd1aQpdBpB9ZCJdloMZD'
access_token_= 'access_token='

graph = facebook.GraphAPI(access_token=access_token, version=2.7)

# message = graph.get_connections(id='6096008671', connection_name=('about'))
# me = facebook.GraphAPI.get_object()
# message =  graph.get_object(id='6096008671', fields='id,name,about,description_html,talking_about_count,single_line_address,picture{url},cover,website,username')
posts = graph.get_object(id='6096008671',fields='')
print posts
# print json.dumps(message)

def get_data_fb(url):
    return requests.get(url).json()

posts = posts['posts']
print posts
# while (posts['posts']['paging'] != ''):
#     get_data_fb(posts['posts']['paging']['next'])

# if posts['posts']['paging'] != '':
count_posts = 0
count_page = 1
while(True):
    try:
        count_posts = count_posts + len(posts['data'])

        if (len(posts['data']) > 0 ):
            idx = len(posts['data']) - 1
            print posts['data'][idx]['created_time']
            posts = get_data_fb(posts['paging']['next'])
            count_page += 1
        else:
            print 'no data to process'
            raise KeyError('End')

    except KeyError:
        print 'Coming Out of Try'
        break

print count_page
print count_posts
# idx = len(posts['data']) - 1
# print idx
# print posts['data'][idx]['created_time']

# print message
# mak =  json.loads(posts)
# print mak

# def main():
#     graph_url = 'https://graph.facebook.com/v2.8/'
#     page_list = ['sarcasmLOL']
#     for page in page_list:
#         #make graph api url with company username
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
#             print value["story"]
#             print value["created_time"]
#             print value["id"]
#             print "            "


# if __name__ == "__main__":
#     main()
