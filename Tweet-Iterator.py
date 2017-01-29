import json

with open('csvfile.csv', 'wb') as file:
    with open('tweets.txt') as f:
        for line in f:
            data = json.loads(line)
            if data['user']['location'] != '':
                print data['user']['location']
                file.write(data['user']['location'].encode('utf-8') + '\n')