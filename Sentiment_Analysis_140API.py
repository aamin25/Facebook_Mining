import urllib2
import json
import re

def sentiment_analysis(tweet):  # modify for productionization
    '''
    Function: Analyzes the sentiment of the text sent using sentiment140 api.
    Param: :text: Pass the pre parsed text to the function without any url or hashtags
    Return: Returns the Sentiment_score and sentiment mean of the text passed in list format
    Dependencies: urllib2, json, re
    '''
    #   Use the regex method to filter out unecessary UTF-8 symbols from the tweet before sending it to sentiment API.
    tweet = re.sub(r"([\'|,|:|\-])", r' ', tweet)  # it\'s "this"  -- filter tweet()

    #   Prepare the data before sending it to sentiment API.
    a = {"data": [{"text": tweet, "query": filter_words[0]}]}

    #   Use the JSON module to convert the data in json format which is the standard input of sentiment API.
    text = json.loads(json.dumps(str(a)))

    #   Use the urllib2 module to sent the request to sentiment API.
    response = urllib2.urlopen('http://www.sentiment140.com/api/bulkClassifyJson?aapid=aamin25@gmail.com', text)

    #   Read the response from the sentiment API.
    page = response.read()  # get the response

    #   Use try or except to process the output
    try:
        sentiment_out_raw = json.loads(page)  # parse the result. The result is in JSON format
        sentiment_score = sentiment_out_raw['data'][0]['polarity']
    except Exception as e:
        print e
        print tweet
        sentiment_score = 2

    # On the basis of sentiment_score set the values of postive,negative and neutral values for the Tweet.
    if sentiment_score >= 3:
        sentiment_mean = 'Positive'
    elif sentiment_score >= 2:
        sentiment_mean = 'Neutral'
    elif sentiment_score <= 1:
        sentiment_mean = 'Negative'
    else:
        print 'Invalid Sentiment Value'

    # Return the sentiment_score and sentiment_mean
    return [sentiment_score, sentiment_mean]

  
if __name__ == '__main__':
     print sentiment_analysis('I love titanic')
