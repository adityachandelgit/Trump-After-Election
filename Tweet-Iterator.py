import csv
import json
import preprocessor

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
            if data['lang'] == 'en' \
                    and data['user'] is not None \
                    and data['user']['location'] != '':
                if data['place'] is not None:
                    country = data['place']['country']
                else:
                    country = ''
                try:
                    cleaned_tweet = preprocessor.clean(data['text'])
                    location = clean_location(data['user']['location'])
                    if location != 'NA':
                        writer.writerow([data['created_at'],
                                         data['id'],
                                         cleaned_tweet,
                                         data['geo'],
                                         data['coordinates'],
                                         data['user']['id'],
                                         data['user']['name'],
                                         location,
                                         data['lang'],
                                         data['user']['time_zone'],
                                         country,
                                         data['user']['friends_count'],
                                         data['user']['followers_count'],
                                         TextBlob(cleaned_tweet).sentiment.polarity
                                         ])
                except Exception:
                    pass


def clean_location(location):
    if 'AL' in location:
        return 'AL'
    elif 'AK' in location:
        return 'AK'
    elif 'AZ' in location:
        return 'AZ'
    elif 'AR' in location:
        return 'AR'
    elif 'CA' in location:
        return 'CA'
    elif 'CO' in location:
        return 'CO'
    elif 'CT' in location:
        return 'CT'
    elif 'DE' in location:
        return 'DE'
    elif 'DC' in location:
        return 'DC'
    elif 'FL' in location:
        return 'FL'
    elif 'GA' in location:
        return 'GA'
    elif 'HI' in location:
        return 'HI'
    elif 'ID' in location:
        return 'ID'
    elif 'IL' in location:
        return 'IL'
    elif 'IN' in location:
        return 'IN'
    elif 'IA' in location:
        return 'IA'
    elif 'KS' in location:
        return 'KS'
    elif 'KY' in location:
        return 'KY'
    elif 'LA' in location:
        return 'LA'
    elif 'ME' in location:
        return 'ME'
    elif 'MD' in location:
        return 'MD'
    elif 'MA' in location:
        return 'MA'
    elif 'MI' in location:
        return 'MI'
    elif 'MN' in location:
        return 'MN'
    elif 'MS' in location:
        return 'MS'
    elif 'MO' in location:
        return 'MO'
    elif 'MT' in location:
        return 'MT'
    elif 'NE' in location:
        return 'NE'
    elif 'NV' in location:
        return 'NV'
    elif 'NH' in location:
        return 'NH'
    elif 'NJ' in location:
        return 'NJ'
    elif 'NM' in location:
        return 'NM'
    elif 'NY' in location:
        return 'NY'
    elif 'NC' in location:
        return 'NC'
    elif 'ND' in location:
        return 'ND'
    elif 'OH' in location:
        return 'OH'
    elif 'OK' in location:
        return 'OK'
    elif 'OR' in location:
        return 'OR'
    elif 'PA' in location:
        return 'PA'
    elif 'RI' in location:
        return 'RI'
    elif 'SC' in location:
        return 'SC'
    elif 'SD' in location:
        return 'SD'
    elif 'TN' in location:
        return 'TN'
    elif 'TX' in location:
        return 'TX'
    elif 'UT' in location:
        return 'UT'
    elif 'VT' in location:
        return 'VT'
    elif 'VA' in location:
        return 'VA'
    elif 'WA' in location:
        return 'WA'
    elif 'WV' in location:
        return 'WV'
    elif 'WI' in location:
        return 'WI'
    elif 'WY' in location:
        return 'WY'
    else:
        return 'NA'


# extract_tweet_fields('Tweets-2000mi-HashTrump.txt', 'Tweets-2000mi-HashTrump-OP.csv')

with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    tweets = list(reader)

seen = set()
uniques = [x for x in tweets if x[2] not in seen and not seen.add(x[2])]

with open("no-dupes.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(uniques)
