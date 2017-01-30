import csv
import json

from textblob import TextBlob


def extract_tweet_fields(input_file, output_file):
    writer = csv.writer(open(output_file, 'wb'))
    writer.writerow(['Created_At',
                     'Tweet_Id',
                     'Text',
                     'GeoLocation',
                     'Coordinates',
                     'User_Id',
                     'User_Name',
                     'User_Location',
                     'Language',
                     'Time_Zone',
                     'Country',
                     'Friends_Count',
                     'Followers_Count',
                     'Sentiment_Polarity'])
    with open(input_file) as f:
        for line in f:
            data = json.loads(line)
            if data['lang'] == 'en':
                if data['place'] is not None:
                    country = data['place']['country']
                else:
                    country = ''
                try:
                    writer.writerow([data['created_at'],
                                     data['id'],
                                     data['text'].encode('utf-8'),
                                     data['geo'],
                                     data['coordinates'],
                                     data['user']['id'],
                                     data['user']['name'],
                                     data['user']['location'],
                                     data['lang'],
                                     data['user']['time_zone'],
                                     country,
                                     data['user']['friends_count'],
                                     data['user']['followers_count'],
                                     TextBlob(data['text'].encode('utf-8').strip()).sentiment.polarity
                                     ])
                except Exception:
                    pass


extract_tweet_fields('tweets.txt', 'tweets-op-1.csv')
