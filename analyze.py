"""
A simple script that takes in a GRE essay and provides a list of basic metrics.

Usage
-----
python analyze.py document_name.txt
"""

from collections import Counter
import re
import sys

file_name = sys.argv[1]

if not file_name:
    print("Please provide a file name. e.g. python analyze.py document_name.txt")
    exit()

with open(file_name) as file:
    body = file.read()
    body = [ re.sub(r"[,.]", "", word.lower()) for word in body.split() ]
    counter = Counter(body)

    print("Total word count: {}".format(len(body)))
    print("Total number of different words: {}".format(len(counter)))
    print("The 10 most common words:")
    for word, count in counter.most_common(10):
        print("{0}: {1}".format(word, count))