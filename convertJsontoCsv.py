# import twitter
import json

# created_at
# id
# id_str
# text
# truncated
# entities
# metadata
# source
# in_reply_to_status_id
# in_reply_to_status_id_str
# in_reply_to_user_id
# in_reply_to_user_id_str
# in_reply_to_screen_name
# user
# geo
# coordinates
# place
# contributors
# is_quote_status
# retweet_count
# favorite_count
# favorited
# retweeted
# lang

with open("city_tweets//test_party_glasgow.json", "r") as file:
    twitterJson = json.load(file)

    # for key, value in twitterJson["statuses"][0].items():
    print(twitterJson["statuses"][0]["text"])

    # for item in twitterJson["statuses"]:
    #     # for key, value in item.items() :
    #     #     print (key)
    #     print(item["geo"]) #json.dumps(twitterJson["statuses"][item]))

# print(creds)


# t = twitter.Api(consumer_key=creds['consumer_key'],
#                 consumer_secret=creds['consumer_secret'],
#                 access_token_key=creds['access_token'],
#                 access_token_secret=creds['access_token_secret'])

# query = {'q': "Labour Party OR Conservative Party OR Liberal Democrats OR Brexit Party",
#         'result_type': 'popular',
#         'count': 100,
#         'geocode': [55.85922,-4.26088, "50mi"],
#         }

# print(t.VerifyCredentials())

# # Import the Twython class
# from twython import Twython
# import json
# import pandas as pd

# # Load credentials from json file
# with open("config.json", "r") as file:
#     creds = json.load(file)

# # Instantiate an object
# python_tweets = Twython(creds['consumer_key'], creds['consumer_secret'])

# # Create our query
# query = {'q': "Labour Party OR Conservative Party OR Liberal Democrats OR Brexit Party",
#         'result_type': 'popular',
#         'count': 100,
#         'geocode': [55.85922,-4.26088, "50mi"],
#         }

# # Search tweets
# dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
# for status in python_tweets.search(**query):
#     # dict_['user'].append(status['user']['screen_name'])
#     # dict_['date'].append(status['created_at'])
#     # dict_['text'].append(status['text'])
#     # dict_['favorite_count'].append(status['favorite_count'])

#     print(len(status))

# # Structure data in a pandas DataFrame for easier manipulation
# df = pd.DataFrame(dict_)
# df.sort_values(by='favorite_count', inplace=True, ascending=False)
# df.head(5)