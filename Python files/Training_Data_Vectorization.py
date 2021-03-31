def data_vectorizing(dataframe, train_x, valid_x):
    
    #Vectorizing the data using TF-IDF vectorizer
    tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=10000)
    tfidf_vect.fit(dataframe['content'])
    #transforming the training and testing data
    xtrain_tfidf =  tfidf_vect.transform(train_x)
    xvalid_tfidf =  tfidf_vect.transform(valid_x)
    
    return xtrain_tfidf, xvalid_tfidf