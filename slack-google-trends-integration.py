import pandas as pd
from pytrends.request import TrendReq
import requests
from datetime import date

# Set up the Slack API token and channel name
SLACK_API_TOKEN = 'YOUR_SLACK_API_TOKEN'
SLACK_CHANNEL_NAME = 'trending-search-terms'

# Define a function to send a message to the Slack channel
def send_slack_message(message):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {'Authorization': f'Bearer {SLACK_API_TOKEN}'}
    data = {'channel': SLACK_CHANNEL_NAME, 'text': message}
    response = requests.post(url, headers=headers, json=data)
    if not response.ok:
        raise Exception('Error sending Slack message')
    print(response.json())

# Define countries
countries = ['india', 'germany', 'united_states', 'united_kingdom']
trending_keywords = {}

# Connect to Google Trends
pytrend = TrendReq()

# Get trending searches for each country
for country in countries:
    df = pytrend.trending_searches(pn=country)
    trending_keywords[f"*{country.capitalize().replace('_', ' ')}*"] = list(df.iloc[:20, 0])

# Format the results as a message
today = date.today().strftime("%B %d, %Y")
message = f"\nHere are the trending keywords from Google on {today}:\n\n"
for country, keywords in trending_keywords.items():
    message += f"{country}:\n\n"
    for keyword in keywords:
        message += f"• {keyword}\n"
    message += "\n"

# Print the message to the console
print(message)

# Send the message to the Slack channel
send_slack_message(message)

