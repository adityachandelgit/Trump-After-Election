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
            if data['lang'] == 'en' \
                    and data['user'] is not None \
                    and data['user']['location'] != '':
                print data['user']['location']
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


def clean(input_file, output_file):
    with open(output_file, 'wb') as f:
        writer = csv.writer(f)
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
        with open(input_file, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for r in reader:
                r1to6 = [r[0], r[1], r[2], r[3], r[4], r[5], r[6]]
                r8to13 = [r[8], r[9], r[10], r[11], r[12], r[13]]
                if 'AL' in r[7]:
                    writer.writerow(r1to6 + ['AL'] + r8to13)
                elif 'AK' in r[7]:
                    writer.writerow(r1to6 + ['AK'] + r8to13)
                elif 'AZ' in r[7]:
                    writer.writerow(r1to6 + ['AZ'] + r8to13)
                elif 'AR' in r[7]:
                    writer.writerow(r1to6 + ['AR'] + r8to13)
                elif 'CA' in r[7]:
                    writer.writerow(r1to6 + ['CA'] + r8to13)
                elif 'CO' in r[7]:
                    writer.writerow(r1to6 + ['CO'] + r8to13)
                elif 'CT' in r[7]:
                    writer.writerow(r1to6 + ['CT'] + r8to13)
                elif 'DE' in r[7]:
                    writer.writerow(r1to6 + ['DE'] + r8to13)
                elif 'DC' in r[7]:
                    writer.writerow(r1to6 + ['DC'] + r8to13)
                elif 'FL' in r[7]:
                    writer.writerow(r1to6 + ['FL'] + r8to13)
                elif 'GA' in r[7]:
                    writer.writerow(r1to6 + ['GA'] + r8to13)
                elif 'HI' in r[7]:
                    writer.writerow(r1to6 + ['HI'] + r8to13)
                elif 'ID' in r[7]:
                    writer.writerow(r1to6 + ['ID'] + r8to13)
                elif 'IL' in r[7]:
                    writer.writerow(r1to6 + ['IL'] + r8to13)
                elif 'IN' in r[7]:
                    writer.writerow(r1to6 + ['IN'] + r8to13)
                elif 'IA' in r[7]:
                    writer.writerow(r1to6 + ['IA'] + r8to13)
                elif 'KS' in r[7]:
                    writer.writerow(r1to6 + ['KS'] + r8to13)
                elif 'KY' in r[7]:
                    writer.writerow(r1to6 + ['KY'] + r8to13)
                elif 'LA' in r[7]:
                    writer.writerow(r1to6 + ['LA'] + r8to13)
                elif 'ME' in r[7]:
                    writer.writerow(r1to6 + ['ME'] + r8to13)
                elif 'MD' in r[7]:
                    writer.writerow(r1to6 + ['MD'] + r8to13)
                elif 'MA' in r[7]:
                    writer.writerow(r1to6 + ['MA'] + r8to13)
                elif 'MI' in r[7]:
                    writer.writerow(r1to6 + ['MI'] + r8to13)
                elif 'MN' in r[7]:
                    writer.writerow(r1to6 + ['MN'] + r8to13)
                elif 'MS' in r[7]:
                    writer.writerow(r1to6 + ['MS'] + r8to13)
                elif 'MO' in r[7]:
                    writer.writerow(r1to6 + ['MO'] + r8to13)
                elif 'MT' in r[7]:
                    writer.writerow(r1to6 + ['MT'] + r8to13)
                elif 'NE' in r[7]:
                    writer.writerow(r1to6 + ['NE'] + r8to13)
                elif 'NV' in r[7]:
                    writer.writerow(r1to6 + ['NV'] + r8to13)
                elif 'NH' in r[7]:
                    writer.writerow(r1to6 + ['NH'] + r8to13)
                elif 'NJ' in r[7]:
                    writer.writerow(r1to6 + ['NJ'] + r8to13)
                elif 'NM' in r[7]:
                    writer.writerow(r1to6 + ['NM'] + r8to13)
                elif 'NY' in r[7]:
                    writer.writerow(r1to6 + ['NY'] + r8to13)
                elif 'NC' in r[7]:
                    writer.writerow(r1to6 + ['NC'] + r8to13)
                elif 'ND' in r[7]:
                    writer.writerow(r1to6 + ['ND'] + r8to13)
                elif 'OH' in r[7]:
                    writer.writerow(r1to6 + ['OH'] + r8to13)
                elif 'OK' in r[7]:
                    writer.writerow(r1to6 + ['OK'] + r8to13)
                elif 'OR' in r[7]:
                    writer.writerow(r1to6 + ['OR'] + r8to13)
                elif 'PA' in r[7]:
                    writer.writerow(r1to6 + ['PA'] + r8to13)
                elif 'RI' in r[7]:
                    writer.writerow(r1to6 + ['RI'] + r8to13)
                elif 'SC' in r[7]:
                    writer.writerow(r1to6 + ['SC'] + r8to13)
                elif 'SD' in r[7]:
                    writer.writerow(r1to6 + ['SD'] + r8to13)
                elif 'TN' in r[7]:
                    writer.writerow(r1to6 + ['TN'] + r8to13)
                elif 'TX' in r[7]:
                    writer.writerow(r1to6 + ['TX'] + r8to13)
                elif 'UT' in r[7]:
                    writer.writerow(r1to6 + ['UT'] + r8to13)
                elif 'VT' in r[7]:
                    writer.writerow(r1to6 + ['VT'] + r8to13)
                elif 'VA' in r[7]:
                    writer.writerow(r1to6 + ['VA'] + r8to13)
                elif 'WA' in r[7]:
                    writer.writerow(r1to6 + ['WA'] + r8to13)
                elif 'WV' in r[7]:
                    writer.writerow(r1to6 + ['WV'] + r8to13)
                elif 'WI' in r[7]:
                    writer.writerow(r1to6 + ['WI'] + r8to13)
                elif 'WY' in r[7]:
                    writer.writerow(r1to6 + ['WY'] + r8to13)


clean('Tweets-2000mi-HashTrump-OP.csv', 'Tweets-2000mi-HashTrump-OP-Cleaned.csv')
# extract_tweet_fields('Tweets-2000mi-HashTrump.txt', 'Tweets-2000mi-HashTrump-OP.csv')
