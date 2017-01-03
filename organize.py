import pandas as pd 
import json
import ast
from plots import top_10_languages
import re



def data_frame(file):

    tweets_data = []
    
    with open(file, "r") as twitter_file:
        tweets_data = [ast.literal_eval(line) for line in twitter_file]
    
    
    tweets = pd.DataFrame()

    tweets['text'] = [tweet.get('text', '') for tweet in tweets_data]
    tweets['happy'] = tweets['text'].apply(lambda tweet: word_in_text('happy', tweet))
    tweets['glad'] = tweets['text'].apply(lambda tweet: word_in_text('glad', tweet))
    tweets['pleased'] = tweets['text'].apply(lambda tweet: word_in_text('pleased', tweet))
    tweets['content'] = tweets['text'].apply(lambda tweet: word_in_text('content', tweet))
    tweets['sad'] = tweets['text'].apply(lambda tweet: word_in_text('sad', tweet))
    tweets['unhappy'] = tweets['text'].apply(lambda tweet: word_in_text('unhappy', tweet))
    tweets['sorrowfull'] = tweets['text'].apply(lambda tweet: word_in_text('sorrowfull', tweet))
    tweets['feeling'] = tweets['text'].apply(lambda tweet: word_in_text('feeling', tweet))
    tweets['happy_relevante'] = lista_feliz(tweets_data)
    tweets['sad_relevante'] = lista_triste(tweets_data)
    tweets['feliz'] = tweets['text'].apply(lambda tweet: word_in_text('feliz', tweet))
    tweets['infeliz'] = tweets['text'].apply(lambda tweet: word_in_text('infeliz', tweet))
    tweets['alegre'] = tweets['text'].apply(lambda tweet: word_in_text('alegre', tweet))
    tweets['triste'] = tweets['text'].apply(lambda tweet: word_in_text('triste', tweet))
    tweets['contente'] = tweets['text'].apply(lambda tweet: word_in_text('contente', tweet))
    tweets['descontente'] = tweets['text'].apply(lambda tweet: word_in_text('descontente', tweet))
    tweets['contenido'] = tweets['text'].apply(lambda tweet: word_in_text('contenido', tweet))
    tweets['descontento'] = tweets['text'].apply(lambda tweet: word_in_text('descontento', tweet))
    tweets['lang'] = [tweet.get('lang', '') for tweet in tweets_data]
    tweets['country'] = lista_country(tweets_data)




    return tweets


def word_in_text(word, text):
    
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True

    return False


def lista_feliz(tweets_data):
    happy_list = []
    for tweet in tweets_data:
        try:
            if (word_in_text('happy', tweet['text']) == True or word_in_text('glad', tweet['text'])==True\
                or word_in_text('pleased', tweet['text'])==True or word_in_text('content', tweet['text'])==True\
                or word_in_text('feliz', tweet['text'])==True\
                or word_in_text('alegre', tweet['text'])==True\
                or word_in_text('contente', tweet['text'])==True\
                or word_in_text('contenido', tweet['text'])==True)\
                and word_in_text('feeling', tweet['text']) == True:

                happy_list.append(True)

            else:
                happy_list.append(False)

        except KeyError:
            happy_list.append(None)
            continue

    return happy_list

def lista_triste(tweets_data):
    sad_list = []
    for tweet in tweets_data:
        try:
            if (word_in_text('sad', tweet['text']) == True or word_in_text('glad', tweet['text'])==True\
                or word_in_text('unhappy', tweet['text'])==True or word_in_text('sorrowfull', tweet['text'])==True\
                or word_in_text('infeliz', tweet['text'])==True\
                or word_in_text('triste', tweet['text'])==True\
                or word_in_text('descontente', tweet['text'])==True\
                or word_in_text('descontento', tweet['text'])==True)\
                and word_in_text('feeling', tweet['text']) == True:

                sad_list.append(True)

            else:
                sad_list.append(False)


        except KeyError:
            sad_list.append(None)
            continue

    return sad_list

def lista_country(tweets_data):
    country_list = []
    for tweet in tweets_data:

        try:
            if tweet['place'] != None:
                country_list.append(tweet.get("country", ''))

            elif tweet['place'] == None:
                country_list.append(None)
    
        except KeyError:
            country_list.append(None)
            continue

    return country_list