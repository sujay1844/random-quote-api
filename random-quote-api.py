#!/bin/python

from flask import Flask, jsonify
import pandas as pd

# If this is not set, then pandas will truncate the data
pd.set_option('display.max_colwidth', None)

# Data parsing takes about 3 secs
# It could be faster if I used dask instead of pandas
# You can also speed it up to 1 sec if you decompress the dataset
df = pd.read_csv("quotes.csv.zip",
                 usecols=["quote", "author"]) # ignore other columns

api = Flask(__name__)

@api.route("/")
def random():
    random_quote = df.sample()
    msg = {
        'quote': random_quote["quote"].to_string(index=False),
        'author': random_quote["author"].to_string(index=False),
    }
    return jsonify(msg)

# /ping is just for testing purposes
@api.route("/ping")
def hello():
    return "pong"

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)
