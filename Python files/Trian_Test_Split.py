def train_test_split(dataframe):
    
    #randomizing the dataframe contents
    dataframe = dataframe.sample(frac = 1)
    
    #splitting the data into train and test
    train_x, valid_x, train_y, valid_y = model_selection.train_test_split(dataframe['content'],dataframe['Troll_label'])                                  
    
    return train_x, valid_x, train_y, valid_y