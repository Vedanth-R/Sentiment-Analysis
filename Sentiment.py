import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime

def run_sentiment_model(ticker: str):
    """
    Fetches recent news headlines for a stock ticker
    and returns the average VADER sentiment score.
    """

    url = f"https://finviz.com/quote.ashx?t={ticker}"
    response = requests.get(url, headers={"User-Agent": "sentiment-demo"})
    html = BeautifulSoup(response.content, "lxml")

    news_table = html.find(id="news-table")
    if news_table is None:
        return None

    analyzer = SentimentIntensityAnalyzer()
    scores = []

    for row in news_table.find_all("tr"):
        if row.a is None:
            continue

        headline = row.a.text
        sentiment = analyzer.polarity_scores(headline)["compound"]
        scores.append(sentiment)

    if len(scores) == 0:
        return None

    return round(sum(scores) / len(scores), 3)
