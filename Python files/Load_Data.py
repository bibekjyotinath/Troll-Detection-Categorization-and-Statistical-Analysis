#Function to load the data to pandas dataframe 
def load_data(selected_tweet_columns_db, selected_tweet_columns_collection, mongo_client_link):
    
    #creating the connection with MongoDB using the pymongo library
    #passing the information to the object
    client = pymongo.MongoClient(mongo_client_link)
    
    #assigining MongoDB database to a variable
    #mongo_db = selected_tweet_columns_db
    mongo_db = client['selected_tweet_columns_db']
    
    #assigning MongoDB database collection to a variable
    #collection = mongo_db.selected_tweet_columns_collection
    collection = mongo_db['selected_tweet_columns_collection']
    
    tweets_df = pd.json_normalize(collection.find({},{'_id':0}), max_level=2)
    
    #dropping all the duplicate rows from
    rd_tweets_df = tweets_df.drop_duplicates(subset = ['full_text'])
    
    #Extracting only the tweets from the exisisting dataframe and creating a new dataframe
    data = [rd_tweets_df['full_text'], rd_tweets_df['category_name']]
    header = ['content', 'category_name']
    new_tweet_df = pd.concat(data, axis = 1, keys = header)
    
    location = input("Please enter the path where you want to save the file: ")
    
    fname = input("Please enter the file name: ")
    
    #saving the dataframe as csv
    rd_tweets_df.to_csv(location+fname)
    
    return rd_tweets_df, new_tweet_df