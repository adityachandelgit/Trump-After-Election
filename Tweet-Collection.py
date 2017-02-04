import sys

import jsonpickle
import tweepy

auth = tweepy.AppAuthHandler('paHY2eshhxrBAwY6laiZCSeVy', '7lH0BTCPwFtJvcavIRjXWkCeq2NgHLSC7aQ8phTIxDKxbTQH7S')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if not api:
    print ("Can't Authenticate")
    sys.exit(-1)

searchQuery = 'Donald Trump'
maxTweets = 10000000
tweetsPerQry = 100
fName = 'Tweets-2000mi-DonaldTrump.txt'
sinceId = None
max_id = -1L

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if max_id <= 0:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, lang='en', geocode='39.198205,-97.646484,2000mi',
                                            count=tweetsPerQry, since='2016-11-08')
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en', geocode='39.198205,-97.646484,2000mi',
                                            since_id=sinceId, since='2016-11-08')
            else:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en', geocode='39.198205,-97.646484,2000mi',
                                            max_id=str(max_id - 1), since='2016-11-08')
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en', geocode='39.198205,-97.646484,2000mi',
                                            max_id=str(max_id - 1),
                                            since_id=sinceId, since='2016-11-08')
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
