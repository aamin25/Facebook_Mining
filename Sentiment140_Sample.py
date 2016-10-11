import urllib2
import json

s = '{"data": [{"text": "I love Titanic."},{"text": "I hate Titanic."}]}'  # 2 short text that we want to do sentiment analysis

response = urllib2.urlopen('http://www.sentiment140.com/api/bulkClassifyJson', s)  # request to server

page = response.read()  # get the response

print page  # print the result

json.loads(page)  # parse the result. The result is in JSON format
