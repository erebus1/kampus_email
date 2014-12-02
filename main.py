from __future__ import print_function
from numpy import size

__author__ = 'user'
import json

f = open("DB.txt", "r")

for line in f.read().split("\n"):
    if line == "":
        continue
    st = line
    parsed_json = json.loads(st)

    for v in parsed_json['rows']:
        if len(v['cell'][7]) != 8:
            for i in v['cell']:
                print(i, end=" ")
            print()



