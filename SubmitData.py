import markdown2
import datetime
import time

url = input("Enter url: ")
title = input("Enter title: ")
numOfTags = input("Enter number of tags: ")

tag = []
for x in range(numOfTags) :
    tag[x] = input("Enter a tag: ")
    
numOfSources = input("Enter number of sources: ")
source = []
for x in range(numOfTags) :
    tag[x] = input("Enter a tag: ")

#text

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')    