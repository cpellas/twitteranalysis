# coding=utf-8
from twitterPredictor.twitter_collect.twitter_connection_setup import twitter_setup
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# création d'un dataframe pour 10 tweets contenant le#EmmanuelMacron, avec les infos: auteur,dates,textes,hashtags et comme index l'index du tweet:
def collect_in_dataframe(str_in_tweets,language, nbr_of_tweets):
    connexion = twitter_setup()
    tweets = connexion.search(str_in_tweets, language=language, rpp=nbr_of_tweets)
    names=[]
    dates=[]
    texts=[]
    hashtag=[]
    favorite=[]
    RTs=[]
    index=[]
    for status in tweets:
        names.append(status.user.name)
        dates.append(status.created_at)
        texts.append(status.text)
        index.append(status.id_str)
        RTs.append(status.retweet_count)
        favorite.append(status.favorite_count)
        if len(status.entities.get('hashtags'))> 0:
            hashtag.append(status.entities.get('hashtags')[0].get("text"))
        else:
            hashtag.append("None")
    tweet=pd.DataFrame({"name":names,"date":dates,"text":texts,"hashtags":hashtag,"Nbr_favorites":favorite,"Nbr_RTs":RTs},index=index)
    print(tweet.Nbr_favorites)

### Pour obtenir les tweets avec un certain hashtag depuis une certaine date: faire une boucle en prenant a chaque fois l'ID du premier tweet et
###demander les 100 tweets plus vieux que cet id etc...

collect_in_dataframe("Macron","French",100)

# collecter les 200 derniers tweets de l'utilisateur avec l'ID d'utilisateur= user_id
def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id=user_id, count=1)
    for status in statuses:
        print(status.entities.get('hashtags')[0].get("text"))
    return statuses

import tweepy
from tweepy.streaming import StreamListener


class StdOutListener(StreamListener):
    # on vérifie que le listener n'a pas tenté d'acceder trop de fois en un
    # certain temps aux API en streaming, si c'est le cas: message d'erreur
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


def collect_by_streaming():  # on collecte les tweets en direct grâce à un listener (objet de la classe que l'on vient de créer)

    connexion = twitter_setup()
    listener = StdOutListener()
    stream = tweepy.Stream(auth=connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])


def max_RTs(dataframe):# quel est le tweet avec le plus de RTs dans dataframe?

    rt_max  = np.max(dataframe['Nbr_RTs'])
    rt  = dataframe[dataframe.Nbr_RTs == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(dataframe['text'][rt].encode('utf-8'))) #attention:rajouter le .encode()
    print("Number of retweets: {}".format(rt_max))
