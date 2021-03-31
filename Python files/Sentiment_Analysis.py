def sentiment_analysis(dataframe):
    
    #SentimentIntensityAnalyzer initialization
    analyser = SentimentIntensityAnalyzer()
    
    #creating an empty list to store the sentiment of the tweets
    sentiment_val = []
    polarity_score = []
    #extracting the tweets from the content column of the dataframe 
    for senti in dataframe['content']:
        
        #passing the tweets to the model to get the polarity score of the tweet
        sentiment_dict = analyser.polarity_scores(senti)   
        polarity_score.append(sentiment_dict['compound'])
        
        # # decide sentiment as positive, negative and neutral on the basis of compound score
        if sentiment_dict['compound'] >= 0.05 :
            val = 'Positive'
            sentiment_val.append(val)

        elif sentiment_dict['compound'] <= - 0.05 :
            val = 'Negative'
            sentiment_val.append(val)

        else :
            val = 'Neutral'
            sentiment_val.append(val)
    
    return sentiment_val, polarity_score