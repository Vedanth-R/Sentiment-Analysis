# Sentiment-Analysis
A basic beginner friendly sentiment analysis. 

# Stock Sentiment Analysis Demo
A simple, local web demo that analyzes the sentiment of recent news headlines for a stock ticker using natural language processing (NLP).
This project is designed to be:
- beginner-friendly
- easy to understand
- easy to run locally
- educational (not production-focused)

# What Does This Do?
You enter a stock ticker (e.g. AAPL)
The app will then:
- scrape recent news headlines from Finviz
- analyze each headline using VADER sentiment analysis
- average the results into a single sentiment score
The website then displays:
- the sentiment score (−1 to +1)
- a simple label: Bullish, Neutral, or Bearish

⚠️ This tool does not predict stock prices.
It measures language tone, not future returns.

# Sentiment Score Meaning
Score Range	Interpretation:
- +1.0	Strongly positive sentiment
- 0.0	Mixed or neutral sentiment
- −1.0	Strongly negative sentiment

# Project Structure
sentiment_demo/
│
├── sentiment.py     # Sentiment model logic
├── main.py          # Local FastAPI server
└── index.html       # Frontend web page

# How to Run Locally
1. Install Dependencies
- pip install fastapi uvicorn requests beautifulsoup4 vaderSentiment lxml

2. Start the Server
- From inside the project folder: uvicorn main:app --reload
- You should see: Uvicorn running on http://127.0.0.1:8000
- Leave this terminal running.

3. Open the Website
- Open index.html in your browser (double-click or right-click → open with browser).

4. Try It Out
- Enter a ticker like AAPL or MSFT and click Analyze to see the sentiment score.
