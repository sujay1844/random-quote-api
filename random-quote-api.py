#!/bin/python

from flask import Flask, jsonify
import pandas as pd
import zstandard
import os
import time

if not os.path.exists('quotes.csv'):
    # Decompress archive
    dctx = zstandard.ZstdDecompressor()
    with open('quotes.csv.zst', 'rb') as input:
        with open('quotes.csv', 'wb') as output:
            dctx.copy_stream(input, output)

# If this is not set, then pandas will truncate the data
pd.set_option('display.max_colwidth', None)

# Data parsing takes about 3 secs
# It could be faster if I used dask instead of pandas
# You can also speed it up to 1 sec if you decompress the dataset
df = pd.read_csv("quotes.csv") 

api = Flask(__name__)

@api.route("/")
def random():
    random_quote = df.sample()
    return jsonify({
        'quote': random_quote["quote"].to_string(index=False),
        'author': random_quote["author"].to_string(index=False),
    })

# /ping is just for testing purposes
@api.route("/ping")
def hello():
    return "pong"

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)
