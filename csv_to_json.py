#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import json

csvfile = open('country.csv', 'r')
jsonfile = open('country.json', 'w')
fieldnames = ("name", "alpha-2", "alpha-3")

reader = csv.DictReader(csvfile, fieldnames)
jsonfile.write('[')
for row in reader:
    item = {}
    for field in fieldnames:
        item[field] = row[field]
    json.dump(item, jsonfile)
    jsonfile.write(',\n')
jsonfile.write(']')

