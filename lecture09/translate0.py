#!/usr/bin/env python3

# cat /etc/passwd | cut -d : -f 1 | grep d$ | wc -l

count = 0
for line in open('/etc/passwd'):
    user = line.rstrip().split(':')[0]
    if user.endswith('d'):
        count += 1

print(count)