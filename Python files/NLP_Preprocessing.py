#function to preprocess the text data
def nlp_preprocessing(dataframe):
    
    abbr_dict={"dunno": "do not know", "wanna": "want to", "what's":"what is", "what're":"what are","who's":"who is","who're":"who are","where's":"where is",
    "where're":"where are","when's":"when is","when're":"when are","how's":"how is","how're":"how are",
    "i'm":"i am","we're":"we are","you're":"you are","they're":"they are","it's":"it is","he's":"he is",
    "she's":"she is","that's":"that is","there's":"there is","there're":"there are","i've":"i have","we've":"we have",
    "you've":"you have","they've":"they have","who've":"who have","would've":"would have","not've":"not have",
    "i'll":"i will","we'll":"we will","you'll":"you will","he'll":"he will","she'll":"she will",
    "it'll":"it will","they'll":"they will","I'll":"i will","isn't":"is not","wasn't":"was not","aren't":"are not","weren't":"were not",
    "can't":"can not","couldn't":"could not","don't":"do not","didn't":"did not","shouldn't":"should not",
    "wouldn't":"would not","doesn't":"does not","haven't":"have not","hasn't":"has not","hadn't":"had not",
    "won't":"will not","u":"you","ur":"your", "rolf": "rolling on floor laughing", "stfu": "shut the fuck up", 
    "icymi": "in case you missed it", "tl;dr": "too long, didn’t read", "lmk": "let me know","nvm": "nevermind",
    "tgif": "thank goodness it’s Friday", "tbh": "to be honest", "tbf": "to be frank", "rn": "right now",
    "qotd": "quote of the day", "brb": "be right back", "btw": "by the way", "lol": "laugh out loud", 
    "ttyl": "talk to you later", "hmu": "hit me up", "fwiw": "for what it’s worth",
    "imo": "in my opinion", "imho": "in my humble opinion", "idk": "i do not know", "tba": "to be announced",
    "tbd": "to be decided", "faq": "frequently asked question", "asap": "as soon as possible", 
    "aka": "also known as", "diy": "do it yourself", "np": "o problem", "ty": "thank you", "hifw": "how i feel when",
    "bts": "behind the scenes", "cmv": "change my view", "dyk": "did you know", "eli5" : "explain it to me like i am five",
    "ftw": "for the win", "irl": "in real life", "nbd": "no big deal", "oc": "original content", "tftf": "thanks for the follow",
    "tfw": "that feeling when", "tigf": "thank god it is friday", "f*ck": "fuck", "f***k": "fuck", "s**k": "suck",
    "b***h": "bitch", "b**ch": "bitch", "a**": "ass", "a**h*le": "asshole", "fu*k": "fuck", "sh*t": "shit", "s**t": "shit",
    "omg": "oh my god", "ily": "i love you", "lmao": "laughing my ass off", "wtf": "what the fuck", "ppl": "people",
    "thx": "thanks", "ffs": "for fuck's sake", "fml": "fuck my life", "stfu": "shut the fuck up", "jj": "just joking",
    "jk": "just kidding", "bff": "best friend forever", "ftw": "for the win", "txt": "text", "hbd": "happy birthday",
    "gtfo": "get the fuck out", "dgaf": "do not give a fuck", "dtf": "down to fuck", "smfh": "shaking my fucking head",
    "roflmao": "rolling on floor laughing my ass off", "ptfo": "passed the fuck out", "ttys": "talk to you soon",
    "fbo": "facebook official", "ttyn": "talk to you never", "b4": "before", "bae": "before anyone else", "btaim": "be that as it may",
    "cx": "customer experience", "dm": "direct message", "f2f": "face to face", "b2b": "business to business",
    "b2c": "business to customer", "fb": "facebook", "ftfy": "fixed that for you", "g2g": "got to go", "gr8": "great",
    "hmb": "hit me back", "hmu": "hit me up", "hth": "happy to help", "ianad": "i am not a doctor", "ianal": "i am not a lawyer",
    "idc": "i do not care", "ig": "instagram", "rss": "really simple syndication", "rt": "retweet", "motherf**ker": "motherfucker",
    "motherfu*cker": "motherfucker", "'em": "them", "ik": "i know", "what&;s":"what is", "what&;re":"what are",
    "who&;s":"who is","who&;re":"who are","where&;s":"where is",
    "where&;re":"where are","when&;s":"when is","when&;re":"when are","how&;s":"how is","how&;re":"how are",
    "i&;m":"i am","we&;re":"we are","you&;re":"you are","they&;re":"they are","it&;s":"it is","he&;s":"he is",
    "she&;s":"she is","that&;s":"that is","there&;s":"there is","there&;re":"there are","i&;ve":"i have","we&;ve":"we have",
    "you&;ve":"you have","they&;ve":"they have","who&;ve":"who have","would&;ve":"would have","not&;ve":"not have",
    "i&;ll":"i will","we&;ll":"we will","you&;ll":"you will","he&;ll":"he will","she&;ll":"she will",
    "it&;ll":"it will","they&;ll":"they will","I&;ll":"i will","isn&;t":"is not","wasn&;t":"was not",
    "aren&;t":"are not","weren&;t":"were not",
    "can&;t":"can not","couldn&;t":"could not","don&;t":"do not","didn&;t":"did not","shouldn&;t":"should not",
    "wouldn&;t":"would not","doesn&;t":"does not","haven&;t":"have not","hasn&;t":"has not","hadn&;t":"had not",
    "won&;t":"will not", "gonna": "got to", "gotcha": "i have got you", "d": "the", "n": "and", "amp": "and"}
    
    #Removing of URL, Mentions, Hastages, Reserved Words (RT and FAV), Emoji, Smiley and Number
    p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)
    dataframe['content'] = dataframe['content'].apply(lambda x: " ".join(p.clean(x) for x in x.split()))
    
    #converting the contents in lower case
    dataframe['content'] = dataframe['content'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    
    #normalizing short words
    dataframe['content'] = dataframe['content'].apply(lambda x: ' '.join([abbr_dict[x] if x in abbr_dict else x for x in x.split()]))
    
    #removing any character which is not alphabets from the string
    dataframe['content'] = dataframe['content'].apply(lambda x: " ".join(x for x in x.split() if x.isalpha()))
    
    #removing the stopwords from the contents
    stop = stopwords.words('english')
    dataframe['content'] = dataframe['content'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    
    #lemmatization of the words from the content
    dataframe['content'] = dataframe['content'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    
    return dataframe