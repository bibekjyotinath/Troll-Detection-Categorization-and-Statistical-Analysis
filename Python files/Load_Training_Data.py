def load_trainingData(mongo_client_link):
#Making the connection between python and MongoDB

    client = pymongo.MongoClient(mongo_client_link)

    #Connecting to datbase and collection of MongoDB
    tclass = client['troll_classification']
    tcollec = tclass['collection_troll']

    #printing the connection to the collection from MongoDB
    print(tcollec)
    
    #Loading the records to pandas dataframe excluding the auto-generated id by MongoDB
    training_df = pd.json_normalize(tcollec.find({},{'_id':0, 'extras':0, 'annotation.notes': 0 }))
    
    #creating an empty list to store the troll label that we would be extracted from the array 
    troll_label = []

    for i in training_df['annotation.label']:
        for j in i:
            troll_label.append(j)
    training_df['Troll_label'] = troll_label
    
    training_df = training_df.drop(labels = 'annotation.label', axis=1)
    
    return training_df