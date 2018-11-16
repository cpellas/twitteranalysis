with open ("hashtag_macron_n.txt","r") as hashtagM:
    requete=hashtagM.readlines()

def get_candidate_queries(candidate_keywords,candidate_hashtag):
    queries=[]
    with open (candidate_keywords,"r") as keywords:
        queries=keywords.readlines()

    with open (candidate_hashtag,"r") as hashtag:
        queries += hashtag.readlines()

    for str in queries:
        str.replace('\n','')
    queriesbis=[]
    for str in queries:
        queriesbis.append(str.replace("\n",""))
    print(queriesbis)

get_candidate_queries("keywords_macron_n.txt", "hashtag_macron_n.txt")

