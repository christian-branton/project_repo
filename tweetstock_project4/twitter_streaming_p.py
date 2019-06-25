#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1126922520022663168-wDMrTsaR6ji4YqyPdt0YT5ZVHzAIQ8"
access_token_secret = "RF2jZH1Iqyp3uFjv7nCAbjC7TQUCyFz4c0KL7X2EViP1y"
consumer_key = "ul03JC4FaongxIgxWmITweAGD"
consumer_secret = "SR8StrdA85hdqDkKBmyP7uUAxT4cWqKIl7nRGwsj6O7Q7dAXAW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['apple','iphone','mac','macbook','ipad','itunes','apple watch','ipod',
    'amazon','amazon prime','prime video','prime music',
    'google','google pixel','chrome','google maps','google drive',
    'disney','disneyland','disneyworld',
    'ford','f150','ford mustang','ford focus','ford fiesta','ford fusion','ford explorer'])
