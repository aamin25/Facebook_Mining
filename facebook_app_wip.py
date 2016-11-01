#! Python 2.7
# *-* UTF-8 *-*

import json
import urllib2
from facepy import GraphAPI

# API keys required for OATH
app_id = '534565370028163'
app_secret = '35e4b69f395f664ebffa9aafc24884c9'
client_token = '6fc3696e738ce60b1f87afd827a54ca7'
#access_token = '1622527554709314|kKlkyrt9HQgOcthBbYA10yoFX6U'
access_token = 'EAAXDriKJZA0IBABVak2BSRBPd9YVdzLQcyTuxeRYu3feXiGYG7vZA8XRshumE5hZCsyPDm6dKQDznDw2T03QrZAzt7jifCOVJZBCZCkMyiTdIpLG6zrGICaKaUTXAUaKj024iUGXUDkx6aCpDYYJB2JrZBNz0RBNGSdNR36CNj9qgZDZD'
access_token_= 'access_token='
# graph = GraphAPI(access_token)
#
# posts = graph.get(path='sarcasmLOL/feed', page=True)
# mak =  json.dumps(posts)
# print mak

def main():
    graph_url = 'https://graph.facebook.com/v2.8/'
    page_list = ['sarcasmLOL']
    for page in page_list:
        #make graph api url with company username
        current_page = graph_url + page + '/feed?' + access_token_ + access_token
        print current_page

        # open public page in facebook graph api
        web_response = urllib2.urlopen(current_page)
        read_page = web_response.read()
        fbpage = json.loads(read_page)

        # print page data to console
        for value in fbpage['data']:
            print value["story"]
            print value["created_time"]
            print value["id"]
            print "            "
            

if __name__ == "__main__":
    main()
