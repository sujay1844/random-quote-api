#!/usr/bin/env python

import os
import sqlite3
import csv_to_sqlite
from flask import Flask, jsonify
import zstandard

api = Flask(__name__)

if not os.path.exists('quotes.db'):
    # Unzip the archive in current directory
    if not os.path.exists('quotes.csv'):
        # Decompress archive
        dctx = zstandard.ZstdDecompressor()
        with open('quotes.csv.zst', 'rb') as input:
            with open('quotes.csv', 'wb') as output:
                dctx.copy_stream(input, output)

    # Import csv into sqlite
    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="utf-8")
    csv_to_sqlite.write_csv(["quotes.csv"], "quotes.db", options)

@api.route("/")
def random():
    # Get one random quote
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1;")
    random_quote = cursor.fetchone()
    connection.close()

    # Send it to caller in json format
    return jsonify({
       'quote': random_quote[0],
       'author': random_quote[1]
    })

# /ping is just for testing purposes
@api.route("/ping")
def hello():
    return "pong"

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)
