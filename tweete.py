import tweepy
from telegram import Bot

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Telegram Bot credentials
telegram_token = "your_telegram_bot_token"
telegram_chat_id = "your_telegram_chat_id"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# List of user IDs to monitor
user_ids = [12345, 56789, 98765]

# Create a class that will handle Twitter Streaming API events
class MyStreamListener(tweepy.StreamListener):
    
    def on_event(self, status):
        if status.event == "favorite" and status.target_object.user.id_str in user_ids:
            # If a monitored user has liked a tweet, send a notification to Telegram
            bot = Bot(telegram_token)
            bot.send_message(chat_id=telegram_chat_id, text=f"User {status.source.screen_name} has liked a tweet: {status.target_object.text}")

# Create a Twitter Streaming API object
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Start the streaming
myStream.filter(follow=user_ids)
