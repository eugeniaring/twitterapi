!pip install searchtweets

############################# 1: Import libraries

from searchtweets import ResultStream, gen_rule_payload, load_credentials
from tweet_parser.tweet import Tweet
import pandas as pd
import itertools

############################ 2: Load credentials

premium_search_args = load_credentials("twitter_keys.yaml",
                                     yaml_key="search_tweets_api",
                                       env_overwrite=False)
                                       
########################### Download data

###################### 3: Generate rule i.e the search query, parameters and operators
                                       
rule = gen_rule_payload("#covid19 #giuseppeconte lang:it", results_per_call=100, from_date="2020-12-14", to_date="2020-12-21")
print(rule)

##################### 4: Get the result stream

rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=1,
                  **premium_search_args)

print(rs)

#####################  5: Check out the resulting Tweets

tweets = list(rs.stream())
print(tweets)

#####################  6: See fields accessible through Tweet Parser Tweet module

print(tweets[2].id)
print(tweets[2].screen_name)
print(tweets[2].user_id)
print(tweets[2].created_at_seconds)
print(tweets[2].tweet_type)
print(tweets[2].all_text)
print(tweets[2].embedded_tweet)
print(tweets[2].user_entered_text)
print(tweets[2].hashtags)

#################### 7: Clean Tweets

clean_tweets = []
fields = ["id","screen_name"]
for tweet in tweets:
    clean_tweet = [tweet.id,tweet.screen_name,tweet.user_id,tweet.created_at_seconds,tweet.tweet_type,tweet.all_text,tweet.user_entered_text,tweet.hashtags]
    clean_tweets.append(clean_tweet)
    
print(clean_tweets)

################# 8: create Pandas Dataframe

df = pd.DataFrame(clean_tweets)
df.columns = ['id', 'screenName',"userId","timestamp","type","text","userEnteredText","hashtags"]

df.head()

df.to_csv("hashtags.csv",header=True,index=False)
                                      
