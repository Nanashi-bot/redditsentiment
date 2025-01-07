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

## License

MIT License

Copyright (c) 2025 Aditya Ghosh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
