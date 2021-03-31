def custom_model_train_test(xtrain, ytrain, xtest, ytest):
    
    model = []
    
    multinomial = Pipeline([('m', naive_bayes.MultinomialNB(alpha=0.2))])
    model.append(('multinomial', multinomial))
    
    decision_tree = Pipeline([('m', DecisionTreeClassifier(random_state = 2))])
    model.append(('decisiontree', decision_tree))
    
    random_forest = Pipeline([('m', RandomForestClassifier())])
    model.append(('randomforest', random_forest))
    
    svc = Pipeline([('m', svm.SVC())])
    model.append(('svc', svc))
    
    passive_aggressive = Pipeline([('m', linear_model.PassiveAggressiveClassifier(C = 0.5, random_state = 5))])
    model.append(('passiveaggressive', passive_aggressive))
    
    ensemble = VotingClassifier(estimators = model, voting = 'hard')
    
    ensemble_fit = ensemble.fit(xtrain, ytrain)
    
    predictions = ensemble.predict(xtest)
    
    print("Prediction: ", predictions)
    
    print("Model Accuracy: ", accuracy_score(ytest, predictions)*100)
     
    print("Confusion Matrix: \n", confusion_matrix(ytest, predictions)) 
    
    return ensemble, ensemble_fit