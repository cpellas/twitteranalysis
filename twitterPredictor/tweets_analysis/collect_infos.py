from twitterPredictor.twitter_collect.twitter_connection_setup import twitter_setup
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from twitterPredictor.twitter_collect.tweets_collect import *

def max_RTs(dataframe):# quel est le tweet avec le plus de RTs dans dataframe?

    rt_max  = np.max(dataframe['Nbr_RTs'])
    rt  = dataframe[dataframe.Nbr_RTs == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(dataframe['text'][rt].encode('utf-8'))) #attention:rajouter le .encode()
    print("Number of retweets: {}".format(rt_max))

def Nbr_hashtag(hashtag): #Nbr de tweets avec le hashtag voulu
    data= collect_in_dataframe(hashtag,"french",100)
    print(len(data.index))

data=collect_in_dataframe("Macron","french", 100)

tfav = pd.Series(data=data['Nbr_favorites'].values, index=data['date'])
tret = pd.Series(data=data['Nbr_RTs'].values, index=data['date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
