def newdata_vectorizing(dataframe):
    
    #Vectorizing the data using TF-IDF vectorizer
    tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=10000)
    tfidf_vect.fit(dataframe['content'])
    #transforming the dataframe
    tweet_tfidf =  tfidf_vect.transform(dataframe['content'])
    
    return tweet_tfidf