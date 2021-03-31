#Testing new dataset extracted from twitter

def new_data_test(ensemble, ensemble_fit, xtest):
    
    #model fit values
    ensemble_fit
    
    #predicting if the tweet is troll or not
    predictions = ensemble.predict(xtest)

    return predictions