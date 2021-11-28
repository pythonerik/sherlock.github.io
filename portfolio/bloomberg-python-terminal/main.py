from twilio.rest import Client
import requests 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_USERNAME = "pythonerik@gmail.com"
NEWS_API_KEY = "4b78101dfe214b309b06c3e961a5c882"
STOCK_API_KEY = "VUI20AN89RSWZF6J"
TWILIO_SID = "ACaae3e00d23dbc4d225523c8fcf28cb8d"
TWILIO_AUTH_TOKEN = "6984c9a5f0ab9ed2043db27b943a3323"
FROM_PHONE = "+19388883833"
TO_PHONE = "+14153421282"

#Use https://www.alphavantage.co/documentation/#daily
#When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

responce = requests.get(STOCK_ENDPOINT, params=stock_params)
data = responce.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[8]
yesterdays_closing_price = yesterday_data["4. close"]
print(yesterdays_closing_price)

#Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = round((difference / float(yesterdays_closing_price)) * 100)
print(diff_percent)

#If percentage is greater than 5 then print("Get News").
#https://newsapi.org/ 
#Get the first 3 news pieces for the COMPANY_NAME. 

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

#Use the News API to get articles related to the COMPANY_NAME.

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[:3]
print(three_articles)

#STEP 3: Use twilio.com/docs/sms/quickstart/python to send a separate message with each article's title and description to your phone number. 

#Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#Send each article as a separate message via Twilio.

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body = article,
        from_ = FROM_PHONE,
        to = TO_PHONE,
    )
