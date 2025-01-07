# Sentiment Analysis on Reddit for Stock Price Correlation

This project analyzes sentiment from Reddit posts about companies and compares it with their stock price trends. Due to recent changes in Reddit's API pricing model, this tool is no longer functional.
## Overview

The project scraped Reddit data using the Reddit API to find posts mentioning specific companies. It performed sentiment analysis on these posts and compared the sentiment with real-time stock price trends to identify correlations. However, due to Reddit's transition to a paid API model, the project is currently non-functional.
## Installation (Before Reddit API Changes)

    1. Clone the repo:

    git clone https://github.com/Nanashi-bot/redditsentiment.git cd redditsentiment

    2. Install dependencies:

    pip install -r requirements.txt

    3. Set up Reddit API credentials (client_id, client_secret, user_agent).

    4. Run the sentiment analysis script (if functional):

    streamlit run display.py

## Dependencies

    streamlit - Frontend
    praw - Reddit API
    transformers, torch - Sentiment analysis
    json, requests - Stock price data
    matplotlib - Visualization
    pandas - Data analysis
