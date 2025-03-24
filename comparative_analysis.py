from collections import Counter

def comparative_analysis(sentiments):
    """Generates a summary of sentiment distribution."""
    sentiment_counts = Counter(sentiments)
    return {
        "Positive": sentiment_counts.get("Positive", 0),
        "Negative": sentiment_counts.get("Negative", 0),
        "Neutral": sentiment_counts.get("Neutral", 0)
    }
