import re
from textblob import TextBlob

def custom_sentiment_analysis(tweet):  # modify for productionization
    '''
    Function: Analyzes the sentiment of the text sent using sentiment140 api.
    Param: :text: Pass the pre parsed text to the function without any url or hashtags
    Return: Returns the Sentiment_score and sentiment mean of the text passed in list format
    Dependencies: textblob and re
    '''
    #   Use the regex method to filter out unecessary UTF-8 symbols from the tweet before calculating sentiment.
    tweet = re.sub(r"([\'|,|:|\-])", r' ', tweet)  # it\'s "this"  -- filter tweet()

    sentiment = TextBlob(tweet)
    
    sentiment_score = sentiment.sentiment.polarity
    
    # On the basis of sentiment_score set the values of postive,negative and neutral values for the Tweet.
    if sentiment_score > 0:
        sentiment_mean = 'Positive'
    elif sentiment_score == 0:
        sentiment_mean = 'Neutral'
    elif sentiment_score < 0:
        sentiment_mean = 'Negative'
    else:
        print 'Invalid Sentiment Value'

    # Return the sentiment_score and sentiment_mean
    return [sentiment_score, sentiment_mean]

if __name__ == '__main__':
    tweet = 'I '
    print custom_sentiment_analysis(tweet)
