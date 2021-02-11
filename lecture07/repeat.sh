#!/bin/sh

N=1

if [ $# -ge 1 ]; then
    N=$1
    shift
else
    echo "Usage: $(basename $0) N message..."
    exit 1
fi

for i in $(seq $N); do
    echo "$@"
done
