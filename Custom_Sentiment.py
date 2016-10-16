import math
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
from nltk import sent_tokenize

nltk.download('punkt')
nltk.download('vader_lexicon')

def sentiment_analysis(tweet):
# Find the average sentiment for the tweet as a whole
    lines_list = sent_tokenize(tweet)  # takes tweet text and takes out individual words and separates them into an array
    sid = SentimentIntensityAnalyzer()  # instantiates the class that will do sentiment analysis
    composite = 0  # initiates initial starting score
    for line in lines_list:
        ss = sid.polarity_scores(line)  # give you the sentiment for a line
        composite += float(ss['compound'])  # adds up all the sentiments

        # for now, just average the scores together
        sentiment = composite / len(lines_list)  # finds average sentiment
        sentimentBin = math.floor(sentiment * 10) / 10.0  # discretiez score
        if sentiment > 0:
            sentimentPosNeg = 'Positive'
        elif sentiment < 0:
            sentimentPosNeg = 'Negative'
        else:
            sentimentPosNeg = 'Neutral'
            msftaccount = ''  # only applicable if following accounts - checking tweet - whether it was sent to account, from account , etc.

    print sentimentBin
    print sentiment
    print sentimentPosNeg


sentiment_analysis('I love titanic #love')
