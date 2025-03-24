import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def fetch_news(company):
    """Fetches news articles using Google News RSS."""
    rss_url = f"https://news.google.com/rss/search?q={company}&hl=en-IN&gl=IN&ceid=IN:en"

    response = requests.get(rss_url)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.content, "xml")  # RSS is XML, not HTML
    articles = []

    for item in soup.find_all("item")[:10]:  # Get top 10 news articles
        title = item.title.text
        link = item.link.text
        pub_date = item.pubDate.text  # Optional: Get the publish date

        articles.append({"title": title, "link": link, "date": pub_date})

    return articles if articles else {"error": "No news articles found"}

def summarize_text(text, num_sentences=3):
    """Summarizes the given text using Sumy's LSA method."""
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, num_sentences)
        return " ".join(str(sentence) for sentence in summary) if summary else text
    except:
        return text  # If summarization fails, return original text
