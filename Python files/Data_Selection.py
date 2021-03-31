def data_selection(mcl, raw_tweet_collection):
    
    #creating the connection with MongoDB using the pymongo library
    #passing the information to the object
    client = pymongo.MongoClient(mcl)
    
    #Loop to retrieve selected columns from the raw data stored inside the database
    query = raw_tweet_collection.find({},{'_id':0, 'created_at':1, 'id':1, 'full_text':1, 
                                    'entities.hashtags.text':1, 'entities.user_mentions.screen_name':1, 
                                    'entities.user_mentions.id':1, 'user.id':1, 'user.name':1 , 'user.screen_name':1, 
                                    'user.location':1, 'user.protected':1, 'user.followers_count':1, 'user.friends_count':1, 
                                    'user.listed_count':1, 'user.created_at':1, 'user.favourites_count':1, 'user.statuses_count':1, 
                                    'retweeted_status.created_at':1, 'retweeted_status.id':1, 'retweeted_status.full_text':1,
                                    'retweeted_status.user_mentions.screen_name':1, 
                                    'retweet_count':1, 'favorite_count':1, 
                                    'possibly_sensitive':1, 'lang':1, 'category_name':1})
    
    #creating a new database in MongoDB to store the selected data extracted from MongoDB
    selected_tweet_columns_db = client['selected_tweet_columns_db']
    
    #creating the collection to store the selected information inside new collection
    selected_tweet_columns_collection = selected_tweet_columns_db['selected_tweet_columns_collection']
    
    #Loop to parse through the selected data and store inside new collection
    for q in query:
        
        #printing the selected data
        print(json.dumps(q, indent = 3))
        
        #inserting the selected tweets inside new collection in MongoDB Database
        selected_tweet_columns_collection.insert_one(q)
    
    return selected_tweet_columns_db, selected_tweet_columns_collection