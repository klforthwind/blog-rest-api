import markdown2
import datetime
import time

import os

def get_file_data(filename):
    if os.path.exists(filename):
        fp = open(filename, "r")
        content = fp.read()
        fp.close()
        return content

url = input("Enter url: ")
title = input("Enter title: ")
numOfTags = input("Enter number of tags: ")

tag = []
for x in range(int(numOfTags)) :
    tag[x] = input("Enter a tag: ")
    
numOfSources = input("Enter number of sources: ")
source = []
for x in range(int(numOfSources)) :
    tag[x] = input("Enter a tag: ")

link = input("Enter file name: ")
content = get_file_data(link)

html = markdown2.markdown(content)

print(html)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')    