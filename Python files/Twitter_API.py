#Creating function to generate twitter API
def create_api():
    
    #Getting input from the user like:
    #Twitter Consumer Key
    consumer_key = input("Enter Consumer Key: ")
    #Twitter Consumer Secret Key
    consumer_secret = input("Enter Consumer Secret: ")
    #Twitter Access Token
    access_token = input("Enter Access Token: ")
    #Twitter Access Token Secret
    access_secret = input("Enter Access Secret: ")
        
    #Authenticating the twitter consumer key and secret using tweepy library
    authenticate = tpy.OAuthHandler(consumer_key, consumer_secret)
    #Authenticating the twitter access token and secret using tweepy library
    authenticate.set_access_token(access_token, access_secret)
    
    #Creating the twitter API using tweepy library
    api = tpy.API(authenticate)
    
    return api