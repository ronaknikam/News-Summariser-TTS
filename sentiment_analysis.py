from textblob import TextBlob

def analyze_sentiment(text):
    """Classifies sentiment as Positive, Negative, or Neutral."""
    sentiment_score = TextBlob(text).sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
