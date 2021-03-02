#!/usr/bin/env python3

import pprint
import requests
import sys

url      = 'https://en.wikipedia.org/w/api.php' # Discuss: APIs
                                                # Discuss: join strings
params   = {'action': 'query', 'list': 'search', 'format': 'json', 'srsearch': sys.argv[1]}
result   = requests.get(url, params=params)     # Review: keyword arguments
data     = result.json()                        # Discuss: json

#pprint.pprint(data)                            # Discuss: pretty printing

articles = data['query']['search']              # Discuss: sorting by key, lambda
#articles = sorted(data['query']['search'], key=lambda o: o['wordcount'])

for index, entry in enumerate(articles, 1):
    print(f"{index:4}. {entry['title']}")
