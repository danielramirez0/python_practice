from env.config import STOCK_API_KEY, NEWS_API_KEY, TO_NUMBER, TW_ACCT, TW_KEY, FROM_NUMBER
import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY 
}

NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# today = dt.datetime.now().date()

# for temp testing
today = dt.datetime(2022,6,17).date()

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then get news related to Stock
# Get yesterday's closing stock price
res = requests.get(STOCK_ENDPOINT, STOCK_PARAMS)
data = res.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_close = float(data_list[0]["4. close"])
# Get the day before yesterday's closing stock price
day_before_yesterday_close = float(data_list[1]["4. close"])
# The difference between 1 and 2
difference = yesterday_close - day_before_yesterday_close
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# The percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (difference / yesterday_close) * 100

if abs(percentage_difference) > 1:
    # Use the News API to get articles related to the COMPANY_NAME
    r = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    articles = r.json()["articles"]
    # Create a list that contains the first 3 articles
    top_three = articles[:3]
    # New list of the first 3 article's headline and description using list comprehension.
    formatted_list = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in top_three]
    # Send each article as a separate message via Twilio. 
    for article in formatted_list:
        client = Client(TW_ACCT, TW_KEY)

        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )

        print(message.sid, message.status)
