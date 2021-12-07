#!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def english_sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

def english_sentiment_counter(comments):
    comments_positive = []
    comments_negative = []
    comments_neutre = []

    for comment in comments :
        sentiment_score = english_sentiment_analyzer_scores(comment)
        if sentiment_score['neg'] > 0.3:
            comments_negative.append(comment)
        elif sentiment_score['neu'] == 1.0:
            comments_neutre.append(comment)
        else:
            comments_positive.append(comment)

    return ({
        "comments_positive" : comments_positive,
        "comments_negative" : comments_negative,
        "comments_neutre" : comments_neutre
    })
