import praw
import datetime
import pandas as pd
import torch
import requests
import json
import matplotlib.pyplot as plt
from transformers import pipeline
import numpy as np


def perform_sentiment_analysis(search_query):
    sentiment_pipeline = pipeline("sentiment-analysis")
    secret= "xV3O4nwRdpRhkp-q3wQEqAPgr3c2sQ"
    appid = "9zVDXji3QYmrL6_ZhmenNw"
    reddit = praw.Reddit(client_id=appid,client_secret=secret,user_agent='scraper_api')
    print("Authentication for " + str(reddit.user.me()) + " is verified.")
    # search_list = ['Tesla', 'ElonMusk', 'SpaceX', 'Elon', 'Grimm']
    search_list=[search_query]
    sortsub = "hot"

    def get_data_dict(search_term, sortsub):
        data_dict = {
        "subject": list(),
        "Title" : list(),
        "score": list(),
        "num_comments" : list(),
        "url" : list(),
        "domain" : list(),
        "selftext":list(),
        "permalink" : list(),
        "id" : list(),
        "subreddit" : list(),
        "time_stamp" : list()
        }
        print(f"this is the searchterm  {search_term}")

        for submission in reddit.subreddit('all').search(search_term.lower(), sort=sortsub,limit=500):
            
            data_dict["subject"].append(search_term.lower())
            data_dict["Title"].append(submission.title)
            data_dict["score"].append(submission.score)
            data_dict["num_comments"].append(submission.num_comments)
            data_dict["url"].append(submission.url)
            data_dict["domain"].append(submission.domain)
            data_dict["selftext"].append(submission.selftext)
            data_dict["permalink"].append(submission.permalink)
            data_dict["id"].append(submission.id)
            data_dict["subreddit"].append(submission.subreddit)
            data_dict["time_stamp"].append(datetime.datetime.utcfromtimestamp(submission.created).strftime('%m-%d-%Y'))

        return data_dict
    
    def get_dataframe(search_list):
        for search_term in search_list:
            df= pd.DataFrame(get_data_dict(search_term = search_term, sortsub = sortsub))
            df.to_csv(f"reddit_{search_term}_data.csv", index=False)

    get_dataframe(search_list)

    for search_term in search_list:
        df = pd.read_csv(f"reddit_{search_term}_data.csv")
    # df1 = pd.read_csv('reddit_ElonMusk_data.csv')
    # df2 = pd.read_csv('reddit_Elon_data.csv')
    # df3 = pd.read_csv('reddit_Elon_data.csv')
    # df4 = pd.read_csv('reddit_Grim_data.csv')

    def senti_analyze(text):
        a=sentiment_pipeline(text)
        return a

    df["sentiment"] = df["Title"].apply(senti_analyze)
    # df1["sentiment"] = df1["Title"].apply(senti_analyze)
    # df2["sentiment"] = df2["Title"].apply(senti_analyze)

    # FOR HUGGING FACE ANALYSIS
    idfk = df['sentiment'].to_numpy()
    label=[]
    score=[]
    for x in idfk:
        # print(x)
        label.append(x[0]['label'])
        score.append(x[0]['score'])
    df['label']=label
    df['score']=score
    # df['sentiment']
    df_new = df.iloc[:, [1,2,-3,-1]]
    # df_new1 = df1.iloc[:, [1,-1]]
    # df_new2 = df2.iloc[:, [1,-1]]

    # df_new.to_excel(r'D:\\New folder\\Tesla.xlsx', header=None, index=None)
    # df_new1.to_excel(r'D:\\New folder\\Elon.xlsx', header=None, index=None)
    # df_new2.to_excel(r'D:\\New folder\\SpaceX.xlsx', header=None, index=None)

    df_new=df_new.drop_duplicates()
    new_row = ["Title","Score","Date","Label"]
    df_new.loc[0] = new_row
    df_new.to_excel(r'D:\\New folder\\Tesla.xlsx', header=None, index=None)
    # df_new1.to_excel(r'D:\\New folder\\Elon.xlsx', header=None, index=None)
    # df_new2.to_excel(r'D:\\New folder\\SpaceX.xlsx', header=None, index=None)

    df_new.sort_values(by='time_stamp', inplace = True) 
    df_new.head()
    dates=[]
    negs=[]
    pos=[]
    c=-1
    for index, row in df_new.iterrows():
        if row['time_stamp'] not in dates:
            dates.append(row['time_stamp'])
            pos.append(0)
            negs.append(0)
            c+=1
        if row["label"]== "NEGATIVE":
            negs[c]+=1
        elif row["label"]== "POSITIVE":
            pos[c]+=1

    dfsent = pd.DataFrame()
    dfsent['Date']=dates
    dfsent['Pos']=pos
    dfsent['Negs']=negs
    dfsent = dfsent.iloc[:-1 , :]
    # dfsent.head()
    dfsent.to_excel(r'D:\\New folder\\teslasents.xlsx', header=None, index=None)

    api="PWCXEB3R143MU162"
    def adjusteddailyopen(symbol="TSLA"):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={api}'

        response = requests.get(url)
        data = response.json()

        # Extract the time series data from the response
        # time_series = data['Daily Time Series']
        # print(data)

        # Extract the time series data from the response
        time_series = data['Time Series (Daily)']

        # Convert the time series data into a pandas DataFrame
        dfx = pd.DataFrame.from_dict(time_series, orient='index')
        dfx = dfx[['1. open']]
        # Sort the DataFrame by date in ascending order
        dfx = dfx.sort_index(ascending=True)
        # Filter the DataFrame to include the last 2 years of data
        dfx = dfx.tail(2 * 365)
        
        dates = dfx.index
        dfx['Date']=dates
        dfx.to_excel(r'D:\\New folder\\tslastock.xlsx', header=None, index=None)

    adjusteddailyopen("TSLA")