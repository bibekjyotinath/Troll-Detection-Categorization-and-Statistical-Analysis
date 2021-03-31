#Function to extract twitter data
def twitter_extraction(api):
    
    #Getting the clinet link for MongoDB connection from the user
    mongo_client_link = input("Please enter the connectivity link: ")
    
    #creating the connection with MongoDB using the pymongo library
    #passing the information to the object
    client = pymongo.MongoClient(mongo_client_link)
    #creating the database in MongoDB to store the raw data extracted from twitter API
    raw_tweet_db = client['raw_tweet_db']
    #creating the collection to store the extracted information inside the database
    raw_tweet_collection = raw_tweet_db['raw_tweet_collection']
    
    #Getting the search string from the user
    tweet_search = input("Please enter the tweet you want to retrieve: ")
    
    #Getting the total number of records that you want retrive from twitter
    tweet_max = int(input("Please enter how many records you want to retrieve: "))
    
    #Getting the category name for an additional column in the database
    category_name = input("Please enter category name: ")
    
    #Loop where it is retrieving the data from twitter and parsing through each records to save it in MongoDB
    for tweet in tpy.Cursor(api.search, q = tweet_search, lang = 'en',
                            exclude='retweets', tweet_mode = 'extended').items(tweet_max):
        
        #converting the retrieve data into dictionary format and storing into variable
        raw_tweets = dict(tweet._json)
        
        indx = list(raw_tweets.values())[1]
        
        print(json.dumps(raw_tweets, indent = 3))
        
        #inserting each record retrieved from the Twitter API in MongoDB database
        raw_tweet_collection.insert_one(raw_tweets)
        #adding a new column in the extsting database for category
        raw_tweet_collection.update_many({'id': indx},{"$set": {'category_name': category_name}})
        
    return raw_tweet_collection, mongo_client_link