
# coding: utf-8

# In[15]:

import requests #an http library written for humans
import tweepy


# In[16]:

# The get method is called when we
# want to GET json data from an API endpoint
#quotes = requests.get(headers) 

response = requests.get("https://andruxnet-random-famous-quotes.p.rapidapi.com/?cat=famous&count=10",
  headers={
    "X-RapidAPI-Key": "296b1be17bmsh911fb67efb47416p1126a8jsn7d5e388ce586"
  }
)


# In[17]:

print(response.json())


# In[18]:

def get_quote():
    response = requests.get("https://andruxnet-random-famous-quotes.p.rapidapi.com/?cat=famous&count=10",
    headers={
    "X-RapidAPI-Key": "296b1be17bmsh911fb67efb47416p1126a8jsn7d5e388ce586"
    }
    )
    json = response.json()[0]
    tweet = json['quote'] + '-' + json['author']
    return tweet


# In[19]:

print(get_quote())


# In[25]:

consumer_key = 'udM9QBdPULslrSXnxKMhTJnav'
consumer_secret = 'baOPQxUDp3ciuy001BXa10h9583lSjn9VqiyiOmafbCdTU7zGu'
access_token = '948607699897475072-JhDZJGvIxPTAjJ8SVNO0utzSyXe2Tij'
access_token_secret = 'DschGmvht76XYTGPdUTFSmS4vrCZ62lZDVd8SCTiSx4MW'


# In[26]:

# Twitter requires oAuth2 to access its API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[28]:

api.update_status('Hello world') # This will update our timeline with "Hello world"


# In[30]:

tweet = get_quote()
api.update_status(tweet) 
print('Done')    # This prints ‘Done’ whenever the update is successful


# In[34]:

def tweet_quote():
    tweet = get_quote()
    status = api.update_status(tweet)
    print(status.id)
    print('Done')


# In[35]:

print(tweet_quote())

