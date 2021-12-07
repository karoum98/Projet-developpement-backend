#!pip install vaderSentiment
from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def french_sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

def french_sentiment_counter(comments):
    comments_positive = []
    comments_negative = []
    comments_neutre = []

    for comment in comments :
        sentiment_score = french_sentiment_analyzer_scores(comment)
        if sentiment_score['neg'] > 0.05:
            comments_negative.append(comment)
        elif sentiment_score['neu'] == 1.0:
            comments_neutre.append(comment)
        elif sentiment_score['pos'] > 0.3:
            comments_positive.append(comment)

    return ({
        "comments_positive" : comments_positive,
        "comments_negative" : comments_negative,
        "comments_neutre" : comments_neutre
    })
