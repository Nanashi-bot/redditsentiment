import streamlit as st
import ULTIMATEFINALPYTHONCODE
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

plt.style.use('dark_background')
# Add a title
st.title("Sentiment Analysis app using reddit")

# Add some text
st.write("Which stock would you like to analyse today?")

# Text input
name = st.text_input("Enter the company name", "")
# ticker = st.text_input("Enter the company ticker name", "")
ticker = ULTIMATEFINALPYTHONCODE.sym(name)
st.write("Ticker name found to be: ",ticker)

if st.button('Submit'):
    df = ULTIMATEFINALPYTHONCODE.scrape_reddit(name)

    st.write("Reddit crawling done")

    #FROM HERE
    df_stock = ULTIMATEFINALPYTHONCODE.stockdata(ticker)
    fig, ax = plt.subplots()
    df_stock['Date'] = pd.to_datetime(df_stock['Date'])
    # print(df_stock)
    ax.plot(df_stock['Date'], df_stock['1. open'].astype(float))
    ax.set_xlabel('Date', color='white')
    ax.set_ylabel('Value', color='white')
    ax.set_title(f'Stock trend for {ticker}')
    # Rotate y-axis tick labels
    ax.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig)
    # fig_html = mpld3.fig_to_html(fig)
    # components.html(fig_html, height=600)
    st.write("Stock trend analysed")
    #TILL HERE


    df_label, df_sent = ULTIMATEFINALPYTHONCODE.perform_sentiment_analysis(df)

    # Create a figure and axes with two subplots
    fig0, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    # Create the first bar chart with 'date' on x-axis and 'pos' on y-axis
    # fig1, ax1 = plt.subplots()
    df_sent['Date'] = pd.to_datetime(df_sent['Date'])
    ax1.plot(df_sent['Date'], df_sent['Pos'], color='green')
    ax1.set_ylim(-df_sent['Pos'].max(), df_sent['Pos'].max())
    ax2.set_ylim(-df_sent['Negs'].max(), df_sent['Negs'].max())
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Positive')

    # # Create the second bar chart with 'date' on x-axis and 'negs' on y-axis
    # fig2, ax2 = plt.subplots()
    ax2.plot(df_sent['Date'], df_sent['Negs'], color='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Negative')

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the subplots in Streamlit
    st.pyplot(fig0)

    figtog, axtog = plt.subplots()
    # Plot the first line graph with 'Date' on the x-axis and 'Pos' on the y-axis
    axtog.plot(df_sent['Date'], df_sent['Pos'], color='green', label='Positive')

    # Plot the second line graph with 'Date' on the x-axis and 'Negs' on the y-axis
    axtog.plot(df_sent['Date'], -df_sent['Negs'], color='red', label='Negative')

    # Set the y-axis limits based on the maximum values
    y_max = max(df_sent['Pos'].max(), df_sent['Negs'].max())
    axtog.set_ylim(-y_max, y_max)

    # Set the x-axis and y-axis labels
    axtog.set_xlabel('Date')
    axtog.set_ylabel('Value')

    # Add a legend
    axtog.legend()

    st.pyplot(figtog)



    added=df_sent['Negs']+df_sent['Pos']
    figx,axx = plt.subplots()
    axx.plot(df_sent['Date'], added, color='blue')
    axx.set_xlabel('Date')
    axx.set_ylabel('Total mentions')
    axx.set_title(f'Total mentions of {name} by day')
    st.pyplot(figx)
    # Convert the 'subreddit' column to string data type


    df['subreddit'] = df['subreddit'].astype(str)
    df['label'] = df['label'].replace({'LABEL_0': 'Negative', 'LABEL_1': 'Positive'})
    st.dataframe(df.iloc[:, [1,7]])


# Run the app
# if __name__ == "__main__":
#     st.run()