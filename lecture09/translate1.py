#!/usr/bin/env python3

# curl -sL https://yld.me/raw/Hk1 | cut -d , -f 2 | grep -Eo '^B.*' | sort

import requests

response   = requests.get('https://yld.me/raw/Hk1')
last_names = []
for line in response.text.splitlines():
    last_name = line.split(',')[1]
    if last_name.startswith('B'):
        last_names.append(last_name)

for last_name in sorted(last_names):
    print(last_name)
