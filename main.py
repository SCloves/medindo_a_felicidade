
from plots import top_10_languages, top_10_countrys
from organize import data_frame


tweets = data_frame('data_2.txt')
top_10_languages(tweets)
top_10_countrys(tweets)



