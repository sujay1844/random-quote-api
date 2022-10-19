#!/usr/bin/env python

import redis
from csv import reader
import zstandard
import os
from flask import Flask, jsonify

r = redis.Redis()

if r.get('quote') == None:
    print("Importing data...")
    if not os.path.exists('quotes.csv'):
        # Decompress archive
        dctx = zstandard.ZstdDecompressor()
        with open('quotes.csv.zst', 'rb') as input:
            with open('quotes.csv', 'wb') as output:
                dctx.copy_stream(input, output)

    with open('quotes.csv', 'r') as input:
        file_reader = reader(input)
        for i in file_reader:
            r.set(i[0], i[1])
    print("Data import done.")

api = Flask(__name__)

@api.route("/")
def random():
    quote = r.randomkey().decode('utf-8')
    author = r.get(quote).decode('utf-8')
    return jsonify({
        'quote': quote,
        'author': author
    })

# /ping is just for testing purposes
@api.route("/ping")
def hello():
    return "pong"

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)
